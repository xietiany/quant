import requests
import pandas as pd
from config import config

class UtilityMixin(object):
    config = config('demo.config')
    apikey = config.api
    base_url = "https://financialmodelingprep.com/api/v3"
    
    @classmethod
    def from_url(cls, url):
        response = requests.get(url)
        data = response.json()
        return data
    
    @classmethod
    def combine_url(cls, ticker, period, datatype):
        return f'{UtilityMixin.base_url}/{datatype}/{ticker}?period={period}&apikey={UtilityMixin.apikey}'
    
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