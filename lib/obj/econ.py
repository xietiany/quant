from lib.util.utility import UtilityMixin
from lib.util.globalvariable import mapping
import akshare as ak
import pandas as pd
import numpy as np

class econ(UtilityMixin):
    def __init__(self, taxRate = 25, rf = 1.64):
        self._tax = taxRate
        self._rf = rf
        self._lowestMarketReturn = 6.0 # for wacc calculation purpose, set a lowest market return

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

    def _indexCalc(self, index="sh000001"):
        self._index = ak.stock_zh_index_daily_em(symbol=index)

    def _marketReturnCalc(self, index="sh000001", period=12):
        '''
        Use smooth method to calculate latest one year market return
        '''
        raw = self._index
        raw["date"] = pd.to_datetime(raw.date)
        monthlyIndex = raw.groupby([raw['date'].dt.year, raw['date'].dt.month])['close'].mean().to_list()
        returnList = []
        for i in range(period):
            returnList.append(monthlyIndex[-1-i] / monthlyIndex[-1-i-12] - 1)
        self._marketReturn = np.mean(returnList) * 100

    