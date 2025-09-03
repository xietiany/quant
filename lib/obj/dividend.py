from lib.util.utility import UtilityMixin
from lib.util.globalvariable import dividendMapping
from datetime import datetime
import akshare as ak

class dividend(UtilityMixin):
    global dividendMapping
    def __init__(self, ticker):
        # self._url = self.div_url(ticker)
        ticker = ticker[2:] # only keep the last six digits
        self._raw = ak.stock_dividend_cninfo(symbol=ticker)
        self._data = self._divTransfer(self._raw)

        self._mapping = dividendMapping

        self._dateStr = self.loadkey(self._data, self._mapping["date"])
        self._date = [self.dateConversion(each, withAppendix=False) for each in self._dateStr]
        # self._divAdj = self.loadts(self._raw, self._mapping["divAdj"], self._date)
        self._div = self.loadts(self._data, self._mapping["div"], self._date)
        # self._divType = self.loadts(self._raw, self._mapping["divType"], self._date)
        self._shareAdd = self.loadts(self._data, self._mapping["shareAdd"], self._date)
        self._shareConvert = self.loadts(self._data, self._mapping["shareConvert"], self._date)
        # self._recordDate = self.loadts(self._raw, self._mapping["recordDate"], self._date)
        # self._paymentDate = self.loadts(self._raw, self._mapping["paymentDate"], self._date)
        # self._declarationDate = self.loadts(self._raw, self._mapping["declarationDate"], self._date)

    def _func(self, x):
        if x["报告时间"]:
            return datetime(int(x["报告时间"][0:4]), 12, 31)
        else: # if 报告时间 is None
            return datetime(int(x["实施方案公告日期"].year), 12, 31) 

    def _divTransfer(self, df):
        '''
        Be careful, the date is hard coded to be 12-31 of the year
        This is because the data is reported at the end of the year, and we want to
        use the date as the end of the year for dividend calculations.  

        Be careful the date is None and not continuous.
        '''
        df["date"] = df.apply(lambda x: self._func(x), axis=1)  # hard code, dealing with None values in 报告时间
        df = df.fillna(0) # other None value will be filled with 0
        result = df.groupby("date")[["送股比例", "转增比例", "派息比例"]].sum().reset_index("date").to_dict('index')
        return result

    @property
    def raw(self):
        return self._raw

    # @property
    # def url(self):
    #     return self._url

    @property
    def date(self):
        return self._date

    # @property
    # def payoutRatio(self):
    #     return self._payoutRatio

    # @property
    # def divAdj(self):
    #     return self._divAdj

    @property
    def div(self):
        return self._div / 10
    
    # @property
    # def divType(self):
    #     return self._divType

    @property
    def shareAdd(self):
        return self._shareAdd

    @property
    def shareConvert(self):
        return self._shareConvert

    # @property
    # def record(self):
    #     return self._recordDate

    # @property
    # def payment(self):
    #     return self._paymentDate

    # @property
    # def declare(self):
    #     return self._declarationDate
