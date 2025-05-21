from util.utility import UtilityMixin
from util.globalvariable import priceMapping

class price(UtilityMixin):
    global priceMapping
    def __init__(self, ticker):
        self._url = self.pric_url(ticker)
        self._raw = self.from_url(self._url)

        self._date = self.loadkey(self._raw, priceMapping['date'])
        self._open = self.loadts(self._raw, priceMapping['open'], self._date)
        self._high = self.loadts(self._raw, priceMapping['high'], self._date)
        self._low = self.loadts(self._raw, priceMapping['low'], self._date)
        self._close = self.loadts(self._raw, priceMapping['close'], self._date)
        self._volume = self.loadts(self._raw, priceMapping['volume'], self._date)
        self._change = self.loadts(self._raw, priceMapping['change'], self._date)
        self._changePercent = self.loadts(self._raw, priceMapping['changePercent'], self._date)
        self._vwap = self.loadts(self._raw, priceMapping['vwap'], self._date)


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
    def open(self):
        return self._open
    
    @property
    def high(self):
        return self._high
    
    @property
    def low(self):
        return self._low
    
    @property
    def close(self):
        return self._close
    
    @property
    def change(self):
        return self._change
    
    @property
    def changePercent(self):
        return self._changePercent
    
    @property
    def vwap(self):
        return self._vwap
