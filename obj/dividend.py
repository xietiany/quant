from util.utility import UtilityMixin
from util.globalvariable import dividendMapping

class dividend(UtilityMixin):
    global dividendMapping
    def __init__(self, ticker):
        self._url = self.div_url(ticker)
        self._raw = self.from_url(self._url)["historical"]

        self._mapping = dividendMapping

        self._date = self.loadkey(self._raw, self._mapping["date"])
        self._divAdj = self.loadts(self._raw, self._mapping["divAdj"], self._date)
        self._div = self.loadts(self._raw, self._mapping["div"], self._date)
        self._recordDate = self.loadts(self._raw, self._mapping["recordDate"], self._date)
        self._paymentDate = self.loadts(self._raw, self._mapping["paymentDate"], self._date)
        self._declarationDate = self.loadts(self._raw, self._mapping["declarationDate"], self._date)

    @property
    def raw(self):
        return self._raw

    @property
    def url(self):
        return self._url

    @property
    def date(self):
        return self._date

    @property
    def divAdj(self):
        return self._divAdj

    @property
    def div(self):
        return self._div

    @property
    def record(self):
        return self._recordDate

    @property
    def payment(self):
        return self._paymentDate

    @property
    def declare(self):
        return self._declarationDate
