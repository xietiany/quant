from obj.incomest import incomest
from obj.balancest import balancest
from obj.cashflowst import cashflowst
from obj.valuation import valuation
from obj.ratio import ratio
from obj.dividend import dividend
from obj.econ import econ
from obj.price import price
from engine.engine import engine
import numpy as np
import pandas as pd

class stock(engine):
    
    def __init__(self, ticker, period = "annual"):
        self._ticker = ticker
        self._period = period
        self._ratiotype = "key-metrics"
        self._balancest = balancest(self._ticker, self._period) # period could be annual|quarter|report
        self._incomest = incomest(self._ticker, self._period) # period could be annual|quarter|report
        self._cashflowst = cashflowst(self._ticker, self._period) # period could be annual|quarter|report
        self._price = price(self._ticker)
        # self._valuation = valuation(self._ticker)
        # self._ratio = ratio(self._ticker, self._period, self._ratiotype)
        self._div = dividend(self._ticker)

        
        # stock characteristics setup
        self._WACCApproach = True
        self._longtermGrowthDefault = True

        self._firstStageGrowth = None 
        self._secondStageGrowth = None
        self._LTGrowth = None

        self._valuationStage = "single" # two, three
        self._valuationMethod = "fcfe" # either fcfe or earning
        self._starting = float(self.incomest.eps.iloc[0]) # earning, NI
        self._growthCalcMethod = "earning" # fcfe, NI
        self._growthCalcHorizon = 5
        self._valuationHorizon = 5
        
        # Econ Variables
        self._macro = econ(taxRate = 25, rf = 1.64)
        self._taxRate = self._macro.taxRate()
        self._rf = self._macro.riskFreeRate()
        self._marketReturn = self._macro.marketReturn()
        self._marketIndex = self._macro.index()

        self._betaCalc()
        self.MVEquity()
        self.MVDebt()
        self.EV()
        self.equityWeight()
        self.debtWeight()
        self.costEquity()
        self.costDebt()


    
    @property
    def ticker(self):
        return self._ticker
    
    @property
    def period(self):
        return self._period
    
    @property
    def balancest(self):
        return self._balancest
    
    @property
    def incomest(self):
        return self._incomest
    
    @property
    def cashflowst(self):
        return self._cashflowst

    @property
    def valuation(self):
        return self._valuation

    @property
    def ratio(self):
        return self._ratio

    @property
    def div(self):
        return self._div

    @property
    def price(self):
        return self._price

    @property
    def taxRate(self):
        return self._taxRate
    
    @property
    def rf(self):
        return self._rf

    @property
    def marketReturn(self):
        return self._marketReturn

    @property
    def beta(self):
        return self._beta

    @property
    def firstStageGrowthValue(self):
        return self._firstStageGrowth

    def firstStageGrowthValueOverride(self, overrideValue):
        self._firstStageGrowth = overrideValue

    @property
    def secondStageGrowthValue(self):
        return self._secondStageGrowth

    def secondStageGrowthValueOverride(self, overrideValue):
        self._secondStageGrowth = overrideValue

    @property
    def longtermGrowthDefault(self):
        return self._longtermGrowthDefault

    @longtermGrowthDefault.setter
    def longtermGrowthDefault(self, defaultGrowthValue = True):
        self._longtermGrowthDefault = defaultGrowthValue

    @property
    def valuationStage(self):
        return self._valuationStage

    @valuationStage.setter
    def valuationStage(self, valuationStage = "single"):
        self._valuationStage = valuationStage

    @property
    def growthCalcMethod(self):
        return self._growthCalcMethod

    @growthCalcMethod.setter
    def growthCalcMethod(self, growthCalcMethod = "earning"):
        self._growthCalcMethod = growthCalcMethod

    @property
    def growthCalcHorizon(self):
        return self._growthCalcHorizon

    @growthCalcHorizon.setter
    def growthCalcHorizon(self, value = 5):
        self._growthCalcHorizon = value

    @property
    def valuationHorizon(self):
        return self._valuationHorizon

    @valuationHorizon.setter
    def valuationHorizon(self, value = 5):
       self._valuationHorizon = value

    def MVEquity(self):
        self._MVEquity = (self._incomest.shares * self._price.latestQuarterMarketPrice).to_list()[0]
        return self._MVEquity
    
    def MVDebt(self):
        self._MVDebt = (self._balancest.stDebt.fillna(0) + self._balancest.notePayable.fillna(0) + \
        self._balancest.ltDebt.fillna(0) + self._balancest.bondPayable.fillna(0) + \
        self._balancest.capitalLease.fillna(0)).to_list()[0]
        return self._MVDebt

    def EV(self):
        self._EV = self._MVEquity + self._MVDebt
        return self._EV

    def equityWeight(self):
        self._equityWeight = self._MVEquity / self._EV
        return self._equityWeight

    def debtWeight(self):
        self._debtWeight = self._MVDebt / self._EV
        return self._debtWeight

    def costEquity(self):
        '''
        CAPM Model
        '''
        self._costEquity = self._rf + self._beta * (self._marketReturn - self._rf)
    
    def costDebt(self):
        self._costDebt = (self._incomest.intExp.fillna(0) / self._MVDebt * 100).to_list()[0]

    def PS(self):
        pass
    
    def PE(self):
        pass

    def PB(self):
        pass
    
    def EVtoEBITDA(self):
        pass

    def PEG(self):
        pass


    @property
    def RR(self):
        if not hasattr(self, "_RR"):
            print("please initialize RR first")
        if self._WACCApproach:
            print("using WACC required rate of return", self._RR)
        else:
            print("using CAPM required rate of return", self._RR)
        return self._RR

    # @RR.setter
    # def RR(self, rate):
    #     if rate <= 0 :
    #         raise ValueError("rate should be greater than 0")
    #     self._RR = rate

    @RR.setter
    def RR(self, WACCApproach=True):
        """
        The default value is true, if WACC is false, then use CAPM
                    self.valuation.equityWeight
                    self.valuation.debtWeight
                    self.valuation.costOfDebt
                    self.valuation.costOfEquity
                    self.valuation.beta
                    self.valuation.RP
                    self.valuation.RF
        """
        self._WACCApproach = WACCApproach
        if self._WACCApproach:
            rate = self.WACC(self._costEquity, self._costDebt, self._equityWeight, self._debtWeight)
        else:
            rate = self.CAPM(self._rf, self._marketReturn, self._beta)
        if rate <= 0:
            raise ValueError("rate should be greater than 0")
        self._RR = rate
    
    def _betaCalc(self, start = "2024-01-01", end = "2024-12-31"):
        stockHist = self._price.raw
        stock_data = stockHist[(stockHist["date"].astype(str) >= start) & (stockHist["date"].astype(str) <= end)]["close"]
        market_data = self._marketIndex[(self._marketIndex["date"].astype(str) >= start) & (self._marketIndex["date"].astype(str) <= end)]["close"]
        if len(stock_data) != len(market_data):
            raise ValueError("Stock data and market data must have the same length for beta calculation.")
        stock_returns = stock_data.pct_change().dropna().to_list()
        market_returns = market_data.pct_change().dropna().to_list()
        
        covariance = np.cov(stock_returns, market_returns)[0,1]
        market_variance = np.var(market_returns)

        self._beta = covariance / market_variance

    def _smooth(self):
        pass

    def firststateGrowthEngine(self, date_now=None, date_pre=None):
        profit = self.incomest.eps
        if self._growthCalcMethod == "earning":
            profit = self.incomest.eps
        elif self._growthCalcMethod == "fcfe":
            profit = (self.cashflowst.freeCF / self.incomest.shares)
        # elif self._growthCalcMethod == "NI":
        #     profit = self.incomest.netInc
        elif self._growthCalcMethod == "div":
            profit = self.div.div
        starting = profit[date_now]
        if starting < 0:
            raise ValueError("the most recent year profit is negative, try other approach")
        if date_pre not in profit:  
            raise ValueError("the profit data is not enough for growth calculation, try other approach")
        last = profit[date_pre]
        if last < 0:
            raise ValueError("the last value is negative, try different year")
        if last > starting:
            print("profit is downtrend,  be aware")
        periodInv = 1 / self._growthCalcHorizon
        self._firstStageGrowth = ((starting / last) ** periodInv - 1) * 100

        # to-do:first value must be positive as well as the last value
        # to-do:first value must be greater than last value

    def secondstateGrowthEngine(self):
        ### use if else condition to get the secondstategrowth
        if not self._firstStageGrowth:
            raise ValueError("Not initialzie the first stage growth rate")
        if self._firstStageGrowth <= 5:
            self._secondStageGrowth = self._firstStageGrowth
        elif self._firstStageGrowth <= 10:
            self._secondStageGrowth = 5
        elif self._firstStageGrowth <= 20:
            self._secondStageGrowth = 10
        elif self._firstStageGrowth <= 30:
            self._secondStageGrowth = 15
        elif self._firstStageGrowth <= 50:
            self._secondStageGrowth = 20
        else:
            self._secondStageGrowth = 30

        if self._firstStageGrowth < 0:
            self._secondStageGrowth = self._firstStageGrowth

        return self._secondStageGrowth
        

    def LTGrowthEngine(self):
        # to-do: We should have a table config for this parameter
        if not self._secondStageGrowth:
            raise ValueError("Not initialize the second stage growth rate")
        if self._secondStageGrowth <= 5:
            self._LTGrowth = self._secondStageGrowth
        elif self._secondStageGrowth <= 10:
            self._LTGrowth = 5
        elif self._secondStageGrowth <= 20:
            self._LTGrowth = 8
        else:
            self._LTGrowth = 10

        # if self._secondStageGrowth < 0:
        #     self._LTGrowth = self._secondStageGrowth
        return self._LTGrowth

    @property
    def LTGrowth(self):
        if not hasattr(self, "_LTGrowth"):
            print("please initialize long term growth first")
        if self._longtermGrowthDefault:
            print("using default long term growth", self._LTGrowth)
        else:
            print("using forecast long term growth", self._LTGrowth)
        return self._LTGrowth

    @LTGrowth.setter
    def LTGrowth(self, usingAnalysis=False):
        # self._longtermGrowthDefault = usingAnalysis
        # if self._longtermGrowthDefault:
        #     self._LTGrowth = self.valuation.growthRateLT
        self._LTGrowth = self.LTGrowthEngine()
        if self._LTGrowth <= 0:
            raise ValueError("long term growth should be greater than 0")

    def LTGrowthOverrdie(self, overrideValue):
        self._LTGrowth = overrideValue

    # def LTGrowthOverride(self, overridevalue):
    #     #to-do: LTGrowth override function or table
    #     pass

    @property
    def valuationMethod(self):
        if not hasattr(self, "_starting"):
            print("please initialize starting first")
        if self._valuationMethod == "fcfe":
            print("using free cash flow per share as forecasting cashflow ", self._starting)
        elif self._valuationMethod == "earning":
            print("using earning per share as forecasting cashflow ", self._starting)
        elif self._valuationMethod == "div":
            print("using dividend as forecasting cashflow", self._starting)
        return self._valuationMethod
    
    @valuationMethod.setter
    def valuationMehod(self, option="fcfe"):
        '''
        Option could be "fcfe, earning, ri"
        '''
        self._valuationMethod = option
        # if self._valuationMethod == "fcfe":
        #     self._starting = (self.cashflowst.freeCF / self.incomest.shares).sort_index(ascending=False).iloc[0]
        # elif self._valuationMethod == "earning":
        #     self._starting = self.incomest.eps.sort_index(ascending=False).iloc[0]
        # elif self._valuationMethod == "div":
        #     self._starting = self.div.div.sort_index(ascending=False).iloc[0]
        # if self._starting <= 0:
        #     raise ValueError("starting value should be greater than 0, consider other approach")
        # self._valuationMethod = option
        # self._starting = float(self.incomest.eps.iloc[0])

    # @property
    # def freecashtoEquity(self):
    #     """
    #     Calculate its own FCFE
    #     """
    #     pass
    def startingValueInit(self, date=None):
        """
        Initialize the starting value
        """
        if self._valuationMethod == "fcfe":
            self._startingList = (self.cashflowst.freeCF / self.incomest.shares)
        elif self._valuationMethod == "earning":
            self._startingList = self.incomest.eps
        elif self._valuationMethod == "div":
            self._startingList = self.div.div
        if not date:
            if self._period == "quarter":
                self._starting = sum(self._startingList.iloc[0:4])
            else:
                self._starting = self._startingList.iloc[0]
        else:
            if self._period == "quarter":
                restDays = self.get_last_day_of_quarters(date)
                res = [self._startingList[date]]
                for each in restDays:
                    res.append(self._startingList[each])
                self._starting = sum(res)
            else:
                self._starting = self._startingList[date]
        # to-do: check the quarter starting value annulization
        if self._starting <= 0:
            raise ValueError("starting value should be greater than 0, consider other approach")


    @property
    def FV(self, date=None):
        """
        Notice the parameter in the earning function is the callback attribute
        Therefore it will prin the input information
        """
        print("valuation method is ", self._valuationMethod)
        print("valuation stage is ", self._valuationStage)
        print("first stage growth is ", self._firstStageGrowth)
        print("second stage growth is ", self._secondStageGrowth)
        print("long term growth is ", self._LTGrowth)
        print("growth period is ", self._growthCalcHorizon)
        print("valuation horizon is ", self._valuationHorizon)
        print("starting value is ", self._starting)
        print("required rate of returen is ", self._RR)
        if self._valuationMethod == "fcfe":
            if self._valuationStage == "single":
                return self.FCFE(self._starting, self._LTGrowth, self._RR)
            elif self._valuationStage == "two":
                return self.FCFETwoStage(self._starting, self._firstStageGrowth, self._valuationHorizon, self._LTGrowth, self._RR)
            elif self._valuationStage == "three":
                return self.FCFEThreeStage(self._starting, self._firstStageGrowth, self._valuationHorizon, self._secondStageGrowth, \
                                        self._valuationHorizon, self._LTGrowth, self._RR)

        elif self._valuationMethod == "earning":
            if self._valuationStage == "single":
                return self.earning(self._starting, self._LTGrowth, self._RR)
            elif self._valuationStage == "two":
                return self.earningTwoStage(self._starting, self._firstStageGrowth, self._valuationHorizon, self._LTGrowth, self._RR)
            elif self._valuationStage == "three":
                return self.earningThreeStage(self._starting, self._firstStageGrowth, self._valuationHorizon, self._secondStageGrowth, \
                                        self._valuationHorizon, self._LTGrowth, self._RR)
        elif self._valuationMethod == "div":
            if self._valuationStage == "single":
                return self.dividendGGM(self._starting, self._LTGrowth, self._RR)
            elif self._valuationStage == "two":
                return self.dividendTwoStage(self._starting, self._firstStageGrowth, self._valuationHorizon, self._LTGrowth, self._RR)
            elif self._valuationStage == "three":
                return self.dividendThreeStage(self._starting, self._firstStageGrowth, self._valuationHorizon, \
                                        self._secondStageGrowth, self._valuationHorizon, self._LTGrowth, self._RR)
        else:
            raise ValueError(f"Unsupported valuation method: {self._valuationMethod}")

    def initialize(self, defaultRateApproach = True, valuationMethod = "fcfe", defaultLTGrowth = False, \
                        valuationStage = "single", growthCalcMethod = "earning", growthCalcHorizon = 5, valuationHorizon = 5, date=None):
        self.RR = defaultRateApproach
        self.valuationMehod = valuationMethod
        self._longtermGrowthDefault = defaultLTGrowth
        self._valuationStage = valuationStage
        self._growthCalcMethod = growthCalcMethod
        self._growthCalcHorizon = growthCalcHorizon
        self._valuationHorizon = valuationHorizon

        self._period ### check period to determine starting value and growth value

        ### If not input, the date will be the latest date in the incomest
        if not date:
            date = self.defaultDate(period=self._period)

        self._formalDate =self.dateconverter(date, period=self._period)
        self._compDate = self.compDateConverter(date, growthCalcHorizon, period=self._period)
        self.startingValueInit(date=self._formalDate)

        self.firststateGrowthEngine(date_now=self._formalDate, date_pre=self._compDate)
        self.secondstateGrowthEngine()
        self.LTGrowthEngine() # Notice that this function including the engine, becuase there is another option for choosing LT growth

        if self._RR < self._LTGrowth + 5:
            print("the current required rate of return is", self._RR)
            print("manually set the RR to be 5 percent greater than long term growth")
            self._RR = self._LTGrowth + 5 # hard code problem
    
    @property
    def reporting(self):
        pass

    @property
    def starting(self):
        return self._starting

    @property
    def getFormalDate(self):
        """
        Get the formal date for the stock
        """
        return self._formalDate

    @property
    def getCompDate(self):
        """
        Get the comparison date for the stock
        """
        return self._compDate