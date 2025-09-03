from lib.obj.incomest import incomest
from lib.obj.balancest import balancest
from lib.obj.cashflowst import cashflowst
from lib.obj.valuation import valuation
from lib.obj.ratio import ratio
from lib.obj.dividend import dividend
from lib.obj.econ import econ
from lib.obj.price import price
from lib.engine.engine import engine
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
        self._lowestMarketReturn = self._macro.getLowestMarketReturn()
        self._rf = self._macro.riskFreeRate()
        self._marketIndex = self._macro.index()
        self._marketReturn = self._marketReturnCalc()

        self._updateCurrentMarketPrice()
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

    def MVEquity(self, input_date=None):
        if not input_date:
            input_date = self.get_default_last_day_of_previous_year()
        self._MVEquity = (self._incomest.shares * self._price.latestQuarterMarketPrice)[input_date]
        return self._MVEquity
    
    def MVDebt(self, input_date=None):
        if not input_date:
            input_date = self.get_default_last_day_of_previous_year()
        self._MVDebt = (self._balancest.stDebt.fillna(0) + self._balancest.notePayable.fillna(0) + \
        self._balancest.ltDebt.fillna(0) + self._balancest.bondPayable.fillna(0) + \
        self._balancest.capitalLease.fillna(0))[input_date]
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

    def costEquity(self, input_date=None):
        '''
        CAPM Model
        '''
        if not input_date:
            input_date = self.get_default_last_day_of_previous_year()
        self._costEquity = self._rf + self._beta * (self._marketReturn - self._rf)
        if self._costEquity < 0:
            self._costEquity = self._lowestMarketReturn
    
    def costDebt(self, input_date=None):
        if not input_date:
            input_date = self.get_default_last_day_of_previous_year()
        self._costDebt = (self._incomest.intExp.fillna(0) / self._MVDebt * 100)[input_date]

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

    def PPE(self):
        self._PPE = self._balancest.fixedAsset.fillna(0) + self._balancest.fixedAssetUnderConstruct.fillna(0) + self._balancest.useRightAsset.fillna(0)
        return self._PPE

    def fixedAssetInvestment(self):
        # self._fixedAssetInvestment = self._PPE.diff(-1) + self._incomest.DA.fillna(0)
        self._fixedAssetInvestment = self._PPE.fillna(0).diff(-1)
        return self._fixedAssetInvestment

    def deltaAP(self):
        self._deltaAP = self._balancest.AP.fillna(0).diff(-1)
        return self._deltaAP
    
    def deltaAR(self):
        self._deltaAR = self._balancest.AR.fillna(0).diff(-1)
        return self._deltaAR    

    def deltaInv(self):
        self._deltaInv = self._balancest.inv.fillna(0).diff(-1)
        return self._deltaInv
    
    def deltaWorkingCapital(self):
        self._deltaWC = self._deltaAR + self._deltaInv - self._deltaAP
        return self._deltaWC

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
        if isinstance(start, str):
            format_string = "%Y-%m-%d"
            start = pd.to_datetime(start, format=format_string).date()
        if isinstance(end, str):
            format_string = "%Y-%m-%d"
            end = pd.to_datetime(end, format=format_string).date()
        
        stockHist = self._price.raw
        self._marketIndex["date"] = pd.to_datetime(self._marketIndex.date)
        stockHist["date"] = pd.to_datetime(stockHist.date)
        stock_data = stockHist[(stockHist["date"].dt.date >= start) & (stockHist["date"].dt.date <= end)].reset_index().set_index("date")["close"]
        market_data = self._marketIndex[(self._marketIndex["date"].dt.date >= start) & (self._marketIndex["date"].dt.date <= end)].reset_index().set_index("date")["close"]
        if len(stock_data) != len(market_data):
            # print("Stock data length:", len(stock_data))
            # print("Market data length:", len(market_data))
            # print(stock_data)
            # print(market_data)
            print("Stock data and market data must have the same length for beta calculation.")
            intercept = set(stock_data.index) & set(market_data.index)
            stock_data = stock_data.loc[list(intercept)] 
            market_data = market_data.loc[list(intercept)]
            print("After alignment, new length:", len(stock_data))
        stock_returns = stock_data.pct_change().dropna().to_list()
        market_returns = market_data.pct_change().dropna().to_list()
        
        covariance = np.cov(stock_returns, market_returns)[0,1]
        market_variance = np.var(market_returns)

        self._beta = covariance / market_variance

    def _marketReturnCalc(self, start = "2024-01-01", end = "2024-12-31"):
        if isinstance(start, str):
            format_string = "%Y-%m-%d"
            start = pd.to_datetime(start, format=format_string).date()
        if isinstance(end, str):
            format_string = "%Y-%m-%d"
            end = pd.to_datetime(end, format=format_string).date()
        self._marketIndex["date"] = pd.to_datetime(self._marketIndex.date)
        selected = self._marketIndex[(self._marketIndex["date"].dt.date >= start) & (self._marketIndex["date"].dt.date <= end)]
        self._marketReturn = (selected.iloc[-1]['close'] / selected.iloc[0]['close'] - 1) * 100
        return self._marketReturn

    def _updateCurrentMarketPrice(self, start = "2024-01-01", end = "2024-12-31"):
        if isinstance(start, str):
            format_string = "%Y-%m-%d"
            start = pd.to_datetime(start, format=format_string).date()
        if isinstance(end, str):
            format_string = "%Y-%m-%d"
            end = pd.to_datetime(end, format=format_string).date()
        self._price._latestQuarterMarketPriceCalc(start, end)
        return self._price.latestQuarterMarketPrice
    
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
        print("required rate of return is ", self._RR)
        print("the beta is ", self._beta)
        print("the market return is ", self._marketReturn)
        print("the cost of equity is ", self._costEquity)
        print("the cost of debt is ", self._costDebt)
        print("the equity weight is ", self._equityWeight)
        print("the debt weight is ", self._debtWeight)
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
                return self.singleStage(self._starting, self._LTGrowth, self._RR)
            elif self._valuationStage == "two":
                return self.TwoStage(self._starting, self._firstStageGrowth, self._valuationHorizon, self._LTGrowth, self._RR)
            elif self._valuationStage == "three":
                return self.ThreeStage(self._starting, self._firstStageGrowth, self._valuationHorizon, \
                                        self._secondStageGrowth, self._valuationHorizon, self._LTGrowth, self._RR)
        else:
            raise ValueError(f"Unsupported valuation method: {self._valuationMethod}")

    def backtesting(self, defaultRateApproach = True, valuationMethod = "fcfe", defaultLTGrowth = False, \
                        valuationStage = "single", growthCalcMethod = "earning", growthCalcHorizon = 5, valuationHorizon = 5, \
                        start_date = '2022-06-30', end_date = '2025-06-30'):
        self._res = []
        self._xaxis = []
        dates = self.get_dates_ends(start_date, end_date, self._period)
        for each in dates:
            temp = []
            current = each
            if self._period == 'quarter':
                next = self.get_last_day_of_next_quarter(each)
            elif self._period == 'annual':
                next = self.get_last_day_of_next_year(each)
            year = next.year
            quarter = (next.month - 1) // 3 + 1
            temp = []
            # print("here", get_last_day_of_next_quarter(each))
            try:
                self.initialize(defaultRateApproach, valuationMethod, defaultLTGrowth, \
                                valuationStage, growthCalcMethod, growthCalcHorizon, valuationHorizon, current)
                fairvalue = self.FV
                temp.append(fairvalue)
                if self._period == 'quarter':
                    temp.append(self.price.topTenMean(self._period).to_dict()[(year, quarter)])
                    temp.append(self.price.Mean(self._period).to_dict()[(year, quarter)])
                elif self._period == 'annual':
                    temp.append(self.price.topTenMean(self._period).to_dict()[year])
                    temp.append(self.price.Mean(self._period).to_dict()[year])
                self._xaxis.append(current)
                self._res.append(temp)
            except ValueError:
                print(ValueError)

        self._backtestingDF = pd.DataFrame(data=self._res, index=self._xaxis, columns=["fair value", "top 10 mean", "mean"])
        plt.plot(self._xaxis, self._res, label = ["fair value", "top 10 mean", "mean"],marker='o', linestyle='-') # For a line plot with markers
        # Or for a scatter plot:
        # plt.scatter(x_values, y_values)
        
        plt.xticks(rotation=90)
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.title("Plot of Backtesting")
        plt.legend()
        plt.grid(True)
        plt.show()

    def initialize(self, defaultRateApproach = True, valuationMethod = "fcfe", defaultLTGrowth = False, \
                        valuationStage = "single", growthCalcMethod = "earning", growthCalcHorizon = 5, valuationHorizon = 5, date=None):
        
        if not date:
            date = self.defaultDate(period=self._period)

        self._formalDate =self.dateconverter(date, period=self._period)
        self._compDate = self.compDateConverter(date, growthCalcHorizon, period=self._period)
        self._startdate, self._enddate = self.get_date_range_from_date(self._formalDate)
        # self._startdate, self._enddate = self.get_last_year_range(date)
        # self._lastdaylastyear = self.get_last_day_of_previous_year(date)

        self._updateCurrentMarketPrice(self._startdate, self._enddate) # resset the latest market price
        self._marketReturnCalc(self._startdate, self._enddate) # reset the market return
        self._betaCalc(self._startdate, self._enddate)
        self.MVEquity(self._formalDate)
        self.MVDebt(self._formalDate)
        self.EV()
        self.equityWeight()
        self.debtWeight()
        self.costEquity(self._formalDate)
        self.costDebt(self._formalDate)
        
        self.RR = defaultRateApproach
        self.valuationMehod = valuationMethod
        self._longtermGrowthDefault = defaultLTGrowth
        self._valuationStage = valuationStage
        self._growthCalcMethod = growthCalcMethod
        self._growthCalcHorizon = growthCalcHorizon
        self._valuationHorizon = valuationHorizon

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

    @property
    def getBacktestingDF(self):
        return self._backtestingDF