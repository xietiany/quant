import requests
import pandas as pd
from datetime import datetime
from lib.util.config import config

class UtilityMixin(object):
    ### to-do: need to change the hard code part
    # config = config('demo.config') # path needs to be changed when used in different project
    # apikey = config.api
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
        # for item in raw:
        #     res.append(item[target])
        # return pd.Series(res, index=key)
        warning = False
        for _, value in raw.items():
            if target in value:
                res.append(value[target])
            else:
                if not warning:
                    print(f"Warning: {target} not found in data for key {key}. Returning None.")
                    warning = True
                res.append(None)
        return pd.Series(res, index=key).sort_index(ascending=False)
    
    @classmethod
    def loadsingle(cls, raw, target):
        if not raw:
            print(f"Warning: No data available for target {target}. Returning None.")
            return None
        return raw[0][target]
    
    @classmethod
    def loadkey(cls, raw, target):
        res = []
        # for item in raw:
        #     res.append(item[target])
        # return res
        warning = False
        for key, value in raw.items():
            if target in value:
                res.append(value[target])
            else:
                if not warning:
                    warning = True
                    print(f"Warning: {target} not found in data for key {key}. Returning None.")
                res.append(None)
        return res

    @classmethod
    def dateConversion(cls, date_str, withAppendix=True):
        if withAppendix:
            format_string = "%Y-%m-%d %H:%M:%S"
            date_object = datetime.strptime(date_str, format_string)

            return date_object.date()
        else:
            # format_string = "%Y-%m-%d"
            # print(type(date_str), date_str)
            # date_object = datetime.strptime(date_str, format_string)

            date_object = date_str

            return date_object.date()