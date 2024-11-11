import requests
import pandas as pd
from util.config import config

class UtilityMixin(object):
    ### to-do: need to change the hard code part
    config = config('demo.config')
    apikey = config.api
    base_url = "https://financialmodelingprep.com/api/v3"
    v4_url = "https://financialmodelingprep.com/api/v4"
    advancedvaluation_url = "advanced_discounted_cash_flow"
    leveredvaluation_url = "advanced_levered_discounted_cash_flow"
    dividend_url = "https://financialmodelingprep.com/api/v3/historical-price-full/stock_dividend"

    
    @classmethod
    def from_url(cls, url):
        response = requests.get(url)
        data = response.json()
        return data
    
    @classmethod
    def combine_url(cls, ticker, period, datatype):
        return f'{UtilityMixin.base_url}/{datatype}/{ticker}?period={period}&apikey={UtilityMixin.apikey}'

    @classmethod
    def valuation_url(cls, ticker, Levered=False):
        if Levered:
            valuationURL = UtilityMixin.leveredvaluation_url
        else:
            valuationURL = UtilityMixin.advancedvaluation_url
        return f'{UtilityMixin.v4_url}/{valuationURL}?symbol={ticker.upper()}&apikey={UtilityMixin.apikey}'

    @classmethod
    def div_url(cls, ticker):
        return f'{UtilityMixin.dividend_url}/{ticker}?apikey={UtilityMixin.apikey}'
    
    @classmethod
    def loadts(cls, raw, target, key):
        res = []
        for item in raw:
            res.append(item[target])
        return pd.Series(res, index=key)
    
    @classmethod
    def loadsingle(cls, raw, target):
        return raw[0][target]
    
    @classmethod
    def loadkey(cls, raw, target):
        res = []
        for item in raw:
            res.append(item[target])
        return res