from util.utility import UtilityMixin
import pandas as pd
import numpy as np
import akshare as ak

class price(UtilityMixin):
    def __init__(self, ticker, start_date="20000101", end_date="20251231", adjust="qfq"):
        self._raw = ak.stock_zh_a_daily(symbol=ticker, start_date=start_date, end_date=end_date, adjust=adjust)

        self._latestQuarterMarketPriceCalc()

    @property
    def raw(self):
        return self._raw

    @property
    def latestQuarterMarketPrice(self):
        return self._current

    def _latestQuarterMarketPriceCalc(self, start="2025-04-01", end="2025-06-30"):
        '''
        to-do: fix the hard code problem
        '''
        selected = self._raw[(self._raw["date"].astype(str) >= start) & (self._raw["date"].astype(str) <= end)]
        self._current = np.mean(selected.close)

