from lib.util.utility import UtilityMixin
import pandas as pd
import numpy as np
import akshare as ak

class price(UtilityMixin):
    def __init__(self, ticker, start_date="20000101", end_date="20501231", adjust="qfq"):
        self._raw = ak.stock_zh_a_daily(symbol=ticker, start_date=start_date, end_date=end_date, adjust=adjust)
        
        self._raw["date"] = pd.to_datetime(self._raw["date"])
        self._raw['Year'] = self._raw['date'].dt.year
        self._raw['Quarter'] = self.raw['date'].dt.quarter

    @property
    def raw(self):
        return self._raw

    @property
    def latestQuarterMarketPrice(self):
        return self._current

    def _groupQuarter(self):
        return self._raw.groupby(['Year', 'Quarter'])

    def _groupYear(self):
        return self._raw.groupby(['Year'])
    
    def Max(self, period='quarter'):
        if period == 'quarter':
            groupData = self._groupQuarter()
        elif period == 'annual':
            groupData = self._groupYear()
        return groupData["close"].max()

    def Mean(self, period='quarter'):
        if period == 'quarter':
            groupData = self._groupQuarter()
        elif period == 'annual':
            groupData = self._groupYear()
        return groupData["close"].mean()
    
    def topTenMax(self, period='quarter'):
        if period == 'quarter':
            groupData = self._groupQuarter()
        elif period == 'annual':
            groupData = self._groupYear()
        return groupData["close"].apply(lambda x: x.nlargest(10).max())
    
    def topTenMean(self, period='quarter'):
        if period == 'quarter':
            groupData = self._groupQuarter()
        elif period == 'annual':
            groupData = self._groupYear()
        return groupData["close"].apply(lambda x: x.nlargest(10).mean())

    def _latestQuarterMarketPriceCalc(self, start="2025-04-01", end="2025-06-30"):
        '''
        to-do: fix the hard code problem
        '''
        selected = self._raw[(self._raw["date"].dt.date >= start) & (self._raw["date"].dt.date <= end)]
        self._current = np.mean(selected.close)

        return self._current
