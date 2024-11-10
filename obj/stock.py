from obj.incomest import incomest
from obj.balancest import balancest
from obj.cashflowst import cashflowst
from obj.valuation import valuation
from obj.ratio import ratio
from engine.engine import engine

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

        
        # stock characteristics setup
        self._WACCApproach = True
        self._longtermGrowthDefault = True

        self._firstStageGrowth = None 
        self._secondStageGrowth = None
        self._LTGrowth = None

        self._valuationStage = "single" # two, three
        self._valuationMethod = "fcfe" # either fcfe or earning
        self._starting = float(self.cashflowst.freeCF.iloc[0] / self.incomest.shares.iloc[0]) # earning, NI
        self._growthCalcuMethod = "earning" # fcfe, NI
        self._growthCalcuHorizon = 5

    
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
    def firstStageGrowthValue(self):
        return self._firstStageGrowth

    def firstStageGrowthValueOverride(self, overrideValue):
        self._firstStageGrowth = overrideValue

    @property
    def secondStageGrowthValue(self):
        return self._secondStageGrowth

    def secondStageGrowthValue(self, overrideValue):
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
    def growthCalcuMethod(self):
        return self._growthCalcuMethod

    @growthCalcuMethod.setter
    def growthCalcuMethod(self, growthCalcuMethod = "earning"):
        self._growthCalcuMethod = growthCalcuMethod

    @property
    def growthCalcuHorizon(self):
        return self._growthCalcuHorizon

    @growthCalcuHorizon.setter
    def growthCalcuHorizon(self, growthCalcuHorizon = 5):
        self._growthcalculationHorizon = growthCalcuHorizon

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

    def _smooth(self):
        pass

    def firststateGrowthEngine(self):
        profit = self.incomest.eps
        if self._growthCalcuMethod == "earning":
            profit = self.incomest.eps
        elif self._growthCalcuMethod == "fcfe":
            profit = self.cashflowst.freeCF / self.incomest.shares
        elif self._growthCalcuMethod == "NI":
            profit = self.incomest.netInc
        starting = profit.iloc[0]
        if starting < 0:
            raise ValueError("the most recent year profit is negative, try other approach")
        last = profit.iloc[0 + self._growthCalcuHorizon]
        if last < 0:
            raise ValueError("the last value is negative, try different year")
        if last > starting:
            raise ValueError("profit is downtrend, try other approach")
        periodInv = 1 / self._growthCalcuHorizon
        self._firstStageGrowth = ((starting / last) ** periodInv - 1) * 100

        # to-do:first value must be positive as well as the last value
        # to-do:first value must be greater than last value

    def secondstateGrowthEngine(self):
        ### use if else condition to get the secondstategrowth
        if not self._firstStageGrowth:
            raise ValueError("Not initialzie the first stage growth rate")
        if self._firstStageGrowth <= 10:
            self._secondStageGrowth = 5
        elif self._firstStageGrowth <= 20:
            self._secondStageGrowth = 10
        elif self._firstStageGrowth <= 30:
            self._secondStageGrowth = 15
        elif self._firstStageGrowth <= 50:
            self._secondStageGrowth = 20
        else:
            self._secondStageGrowth = 30

        return self._secondStageGrowth
        

    def LTGrowthEngine(self):
        # to-do: We should have a table config for this parameter
        if not self._secondStageGrowth:
            raise ValueError("Not initialize the second stage growth rate")
        if self._secondStageGrowth <= 10:
            self._LTGrowth = 5
        elif self._secondStageGrowth <= 20:
            self._LTGrowth = 8
        else:
            self._LTGrowth = 10
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
    def LTGrowth(self, usingAnalysis):
        self._longtermGrowthDefault = usingAnalysis
        if self._longtermGrowthDefault:
            self._LTGrowth = self.valuation.growthRateLT
        else:
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
        return self._starting
    
    @valuationMethod.setter
    def valuationMehod(self, option="fcfe"):
        '''
        Option could be "fcfe, earning, ri"
        '''
        self._valuationMethod = option
        if self._valuationMethod == "fcfe":
            self._starting = float(self.cashflowst.freeCF.iloc[0] / self.incomest.shares.iloc[0])
        elif self._valuationMethod == "earning":
            self._starting = float(self.incomest.eps.iloc[0])
        if self._starting <= 0:
            raise ValueError("starting value should be greater than 0, consider other approach")

    @property
    def FCFE(self):
        """
        Calculate its own FCFE
        """
        pass

    @property
    def FV(self):
        """
        Notice the parameter in the earning function is the callback attribute
        Therefore it will prin the input information
        """
        print("valuation method is ", self._valuationMethod)
        print("valuation stage is ", self._valuationStage)
        print("first stage growth is ", self._firstStageGrowth)
        print("second stage growth is ", self._secondStageGrowth)
        print("long term growth is ", self._LTGrowth)
        print("growth period is ", self._growthCalcuHorizon)
        print("starting value is ", self._starting)
        print("required rate of returen is ", self._RR)
        if self._valuationMethod == "fcfe":
            if self._valuationStage == "single":
                return self.FCFE(self._starting, self._LTGrowth, self._RR)
            elif self._valuationStage == "two":
                return self.FCFETwoStage(self._starting, self._firstStageGrowth, self._growthCalcuHorizon, self._LTGrowth, self._RR)
            elif self._valuationStage == "three":
                return self.FCFEThreeStage(self._starting, self._firstStageGrowth, self._growthCalcuHorizon, self._secondStageGrowth, \
                                        self._growthCalcuHorizon, self._LTGrowth, self._RR)

        elif self._valuationMethod == "earning":
            if self._valuationStage == "single":
                return self.earning(self._starting, self._LTGrowth, self._RR)
            elif self._valuationStage == "two":
                return self.earningTwoStage(self._starting, self._firstStageGrowth, self._growthCalcuHorizon, self._LTGrowth, self._RR)
            elif self._valuationStage == "three":
                return self.earningThreeStage(self._starting, self._firstStageGrowth, self._growthCalcuHorizon, self._secondStageGrowth, \
                                        self._growthCalcuHorizon, self._LTGrowth, self._RR)

        return self.FCFE(self._starting, self._LTGrowth, self._RR)

    def initialize(self, defaultRateApproach = True, valuationMethod = "fcfe", defaultLTGrowth = True, \
                        valuationStage = "single", growthCalcuMethod = "earning", growthCalcuHorizon = 5):
        self.RR = defaultRateApproach
        self.valuationMehod = valuationMethod
        self._longtermGrowthDefault = defaultLTGrowth
        self._valuationStage = valuationStage
        self._growthCalcuMethod = growthCalcuMethod
        self._growthCalcuHorizon = growthCalcuHorizon

        self.firststateGrowthEngine()
        self.secondstateGrowthEngine()
        self.LTGrowthEngine() # Notice that this function including the engine, becuase there is another option for choosing LT growth
    
    @property
    def reporting(self):
        pass