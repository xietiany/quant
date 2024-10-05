from incomest import incomest
from balancest import balancest
from cashflowst import cashflowst
from valuation import valuation
from ratio import ratio
from engine import engine

class stock(engine):
    
    def __init__(self, ticker, period = "annual", report = False):
        self._ticker = ticker
        self._period = period
        self._ratiotype = "key-metrics"
        if report:
            self._balancedatatype = "balance-sheet-statement-as-reported"
            self._incomedatatype = "income-statement-as-reported"
            self._cashflowdatatype = "cash-flow-statement-as-reported"
        else:
            self._balancedatatype = "balance-sheet-statement"
            self._incomedatatype = "income-statement"
            self._cashflowdatatype = "cash-flow-statement"
        self._balancest = balancest(self._ticker, self._period, self._balancedatatype)
        self._incomest = incomest(self._ticker, self._period, self._incomedatatype)
        self._cashflowst = cashflowst(self._ticker, self._period, self._cashflowdatatype)
        self._valuation = valuation(self._ticker)
        self._ratio = ratio(self._ticker, self._period, self._ratiotype)

        self._WACCApproach = True
        self._startingoption = "fcfe"
        self._longtermGrowthDefault = True

    
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
            rate = self.WACC(self.valuation.costOfEquity, self.valuation.costOfDebt, self.valuation.equityWeight, self.valuation.debtWeight)
        else:
            rate = self.CAPM(self.valuation.RF, self.valuation.RP, self.valuation.beta)
        if rate <= 0:
            raise ValueError("rate should be greater than 0")
        self._RR = rate

    @property
    def firststateGrowth(self):
        pass

    @property
    def secondstateGrowth(self):
        pass

    @property
    def LTGrowth(self):
        if not hasattr(self, "_LTGrowth"):
            print("please initialize long term growth first")
        if self._longtermGrowthDefault:
            print("using default long term growth", self._LTGrowth)
        return self._LTGrowth

    @LTGrowth.setter
    def LTGrowth(self, usingAnalysis = True):
        self._longtermGrowthDefault = usingAnalysis
        if self._longtermGrowthDefault:
            self._LTGrowth = self.valuation.growthRateLT
        if self._LTGrowth <= 0:
            raise ValueError("long term growth should be greater than 0")

    @property
    def starting(self):
        if not hasattr(self, "_starting"):
            print("please initialize starting first")
        if self._startingoption == "fcfe":
            print("using free cash flow per share as forecasting cashflow ", self._starting)
        elif self._startingoption == "eps":
            print("using earning per share as forecasting cashflow ", self._starting)
        return self._starting
    
    @starting.setter
    def starting(self, option="fcfe"):
        '''
        Option could be "fcfe, eps, ri"
        '''
        self._startingoption = option
        if self._startingoption == "fcfe":
            self._starting = self.cashflowst.freeCF.iloc[0] / self.incomest.shares.iloc[0]
        elif self._startingoption == "eps":
            self._starting = self.incomest.eps.iloc[0]
        if self._starting <= 0:
            raise ValueError("starting value should be greater than 0, consider other approach")

    @property
    def FCFE(self):
        pass

    @property
    def FV(self):
        """
        Notice the parameter in the earning function is the callback attribute
        Therefore it will prin the input information
        """
        # self._starting = self.nextStarting(option)
        # self._LTGrowth = self.valuation.growthRateLT
        return self.earning(self.starting, self.LTGrowth, self.RR)

    @property
    def reporting(self):
        pass