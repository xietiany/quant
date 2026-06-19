from lib.util.utility import UtilityMixin
import akshare as ak
import pandas as pd
import numpy as np

class econ(UtilityMixin):

    MARKET_RETURN_METHODS = ["historical", "implied_erp", "fixed_erp"]

    def __init__(self, taxRate=25, rf=1.64, lowestMarketReturn=6.0, marketReturnMethod="historical", n_years=10, fixed_erp=7.5):
        self._tax = taxRate
        self._rf = rf
        self._lowestMarketReturn = lowestMarketReturn
        self._marketReturnMethod = marketReturnMethod
        self._n_years = n_years
        self._fixed_erp = fixed_erp

        self._indexCalc()
        self._marketReturnCalc()

    def taxRate(self):
        return self._tax

    def riskFreeRate(self):
        return self._rf

    def marketReturn(self):
        return self._marketReturn

    def getLowestMarketReturn(self):
        return self._lowestMarketReturn

    def index(self):
        return self._index

    def setMarketReturnMethod(self, method, n_years=None, fixed_erp=None):
        """
        Switch the expected market return calculation method and recompute.

        Options:
          "historical"  — arithmetic mean of annual returns over n_years (default 10).
                          Stable long-run estimate; standard for DCF valuation.
          "implied_erp" — earnings yield of SSE composite (1/PE) plus a long-term
                          nominal growth assumption (5%). Forward-looking but noisier.
          "fixed_erp"   — rf + fixed equity risk premium (default 7.5%, Damodaran China).
                          Simple and transparent; good when market data is unreliable.
        """
        if method not in self.MARKET_RETURN_METHODS:
            raise ValueError(f"method must be one of {self.MARKET_RETURN_METHODS}")
        self._marketReturnMethod = method
        if n_years is not None:
            self._n_years = n_years
        if fixed_erp is not None:
            self._fixed_erp = fixed_erp
        self._marketReturnCalc()
        return self._marketReturn

    def _indexCalc(self):
        self._index = ak.stock_zh_a_daily(symbol='sh000001')

    def _marketReturnCalc(self):
        if self._marketReturnMethod == "historical":
            self._marketReturn = self._historicalMarketReturn()
        elif self._marketReturnMethod == "implied_erp":
            self._marketReturn = self._impliedERPReturn()
        elif self._marketReturnMethod == "fixed_erp":
            self._marketReturn = self._fixedERPReturn()
        else:
            raise ValueError(f"Unknown market return method: {self._marketReturnMethod}")

    def _historicalMarketReturn(self):
        """Arithmetic mean of annual returns over the past n_years."""
        raw = self._index.copy()
        raw["date"] = pd.to_datetime(raw["date"])
        raw = raw.sort_values("date")
        annual_returns = []
        latest = raw["date"].max()
        for i in range(self._n_years):
            end = latest - pd.DateOffset(years=i)
            start = end - pd.DateOffset(years=1)
            period = raw[(raw["date"] >= start) & (raw["date"] <= end)]
            if len(period) < 2:
                continue
            r = period.iloc[-1]["close"] / period.iloc[0]["close"] - 1
            annual_returns.append(r)
        if not annual_returns:
            raise ValueError("Not enough index data for historical market return calculation")
        return float(np.mean(annual_returns) * 100)

    def _impliedERPReturn(self):
        """
        Earnings yield of SSE composite + long-term nominal growth.
        Expected Rm = (1 / PE) * 100 + long_term_growth
        Falls back to historical if PE data is unavailable.
        """
        try:
            pe_data = ak.stock_market_pe_lng(symbol="上证综指")
            latest_pe = float(pe_data.iloc[-1, 1])
            if latest_pe <= 0:
                raise ValueError("Invalid PE value")
            earnings_yield = (1 / latest_pe) * 100
            long_term_growth = 5.0  # nominal GDP growth assumption for China
            return earnings_yield + long_term_growth
        except Exception as e:
            print(f"Implied ERP fetch failed ({e}), falling back to historical method")
            return self._historicalMarketReturn()

    def _fixedERPReturn(self):
        """Risk-free rate plus a fixed equity risk premium (Damodaran China estimate)."""
        return self._rf + self._fixed_erp
