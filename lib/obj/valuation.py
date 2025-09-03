from lib.util.utility import UtilityMixin
from lib.util.globalvariable import valuationMapping

class valuation(UtilityMixin):
    global valuationMapping
    def __init__(self, ticker):
        self._url = self.valuation_url(ticker)
        self._raw = self.from_url(self._url)

        self._year = self.loadkey(self._raw, valuationMapping['year'])
        self._price = self.loadts(self._raw, valuationMapping['price'], self._year)
        self._beta = self.loadsingle(self._raw, valuationMapping['beta'])
        # self._finalTaxRate = self.loadts(self._raw, valuationMapping['finalTaxRate'], self._year)
        self._totalDebt = self.loadts(self._raw, valuationMapping['totalDebt'], self._year)
        self._totalEquity = self.loadts(self._raw, valuationMapping['totalEquity'], self._year)
        self._totalCapital = self.loadts(self._raw, valuationMapping['totalCapital'], self._year)
        self._dilutedShare = self.loadts(self._raw, valuationMapping['dilutedShare'], self._year)
        self._debtWeight = self.loadsingle(self._raw, valuationMapping['debtWeight'])
        self._equityWeight = self.loadsingle(self._raw, valuationMapping['equityWeight'])
        # self._period = self.loadts(self._raw, valuationMapping['period'], self._year)
        self._revenue = self.loadts(self._raw, valuationMapping['revenue'], self._year)
        self._ebitda = self.loadts(self._raw, valuationMapping['ebitda'], self._year)
        # self._operatingCF = self.loadts(self._raw, valuationMapping['operatingCF'], self._year)
        self._ebit = self.loadts(self._raw, valuationMapping['ebit'], self._year)
        # self._avgWeightShare = self.loadts(self._raw, valuationMapping['avgWeightShare'], self._year)
        self._netDebt = self.loadts(self._raw, valuationMapping['netDebt'], self._year)
        self._inventory = self.loadts(self._raw, valuationMapping['inventory'], self._year)
        self._receivables = self.loadts(self._raw, valuationMapping['receivables'], self._year)
        self._payable = self.loadts(self._raw, valuationMapping['payable'], self._year)
        # self._inventoryDiff = self.loadts(self._raw, valuationMapping['inventoryDiff'], self._year)
        # self._receivableDiff = self.loadts(self._raw, valuationMapping['receivableDiff'], self._year)
        # self._payableDiff = self.loadts(self._raw, valuationMapping['payableDiff'], self._year)
        self._capExp = self.loadts(self._raw, valuationMapping['capExp'], self._year)
        # self._priorRevenue = self.loadts(self._raw, valuationMapping['priorRevenue'], self._year)
        self._revenuePercent = self.loadts(self._raw, valuationMapping['revenuePercent'], self._year)
        self._taxRate = self.loadts(self._raw, valuationMapping['taxRate'], self._year)
        self._ebitdaPercent = self.loadts(self._raw, valuationMapping['ebitdaPercent'], self._year)
        
        self._receivablePercent = self.loadts(self._raw, valuationMapping['receivablePercent'], self._year)
        self._inventoryPercent = self.loadts(self._raw, valuationMapping['inventoryPercent'], self._year)
        self._payablePercent = self.loadts(self._raw, valuationMapping['payablePercent'], self._year)
        self._ebitPercent = self.loadts(self._raw, valuationMapping['ebitPercent'], self._year)
        
        self._capExpPercent = self.loadts(self._raw, valuationMapping['capExpPercent'], self._year)
        # self._operatingCFPercent = self.loadts(self._raw, valuationMapping['operatingCFPercent'], self._year)
        self._postTaxCostDebt = self.loadts(self._raw, valuationMapping['postTaxCostDebt'], self._year)
        self._marketRiskPremium = self.loadsingle(self._raw, valuationMapping['marketRiskPremium'])
        self._growthRateLT = self.loadsingle(self._raw, valuationMapping['growthRateLT'])
        self._costOfEquity = self.loadsingle(self._raw, valuationMapping['costOfEquity'])
        self._WACC = self.loadts(self._raw, valuationMapping['WACC'], self._year)
        
        self._cashTaxRate = self.loadts(self._raw, valuationMapping['cashTaxRate'], self._year)
        self._ebiat = self.loadts(self._raw, valuationMapping['ebiat'], self._year)
        self._ufcf = self.loadts(self._raw, valuationMapping['ufcf'], self._year)
        self._riskFreeRate = self.loadsingle(self._raw, valuationMapping['riskFreeRate'])
        self._sumPvUfcf = self.loadts(self._raw, valuationMapping['sumPvUfcf'], self._year)
        self._terminalValue = self.loadts(self._raw, valuationMapping['terminalValue'], self._year)
        self._presentTerminalValue = self.loadts(self._raw, valuationMapping['presentTerminalValue'], self._year)
        self._EV = self.loadts(self._raw, valuationMapping['EV'], self._year)
        self._equityValue = self.loadts(self._raw, valuationMapping['equityValue'], self._year)
        self._equityValuePerShare = self.loadts(self._raw, valuationMapping['equityValuePerShare'], self._year)
        self._freeCashFlowT1 = self.loadts(self._raw, valuationMapping['freeCashFlowT1'], self._year)
        self._costOfDebt = self.loadsingle(self._raw, valuationMapping['costOfDebt'])
        self._dep = self.loadts(self._raw, valuationMapping['dep'], self._year)
        self._totalCash = self.loadts(self._raw, valuationMapping['totalCash'], self._year)
        self._depPercent = self.loadts(self._raw, valuationMapping['depPercent'], self._year)
        self._totalCashPercent = self.loadts(self._raw, valuationMapping['totalCashPercent'], self._year)

    @property
    def raw(self):
        return self._raw

    @property
    def url(self):
        return self._url

    @property
    def year(self):
        return self._year

    @property
    def price(self):
        return self._price

    @property
    def beta(self):
        return self._beta

    # @property
    # def taxRateTotal(self):
    #     return self._finalTaxRate

    @property
    def totalDebt(self):
        return self._totalDebt

    @property
    def totalEquity(self):
        return self._totalEquity

    @property
    def totalCapital(self):
        return self._totalCapital

    @property
    def dilutedShare(self):
        return self._dilutedShare

    @property
    def debtWeight(self):
        return self._debtWeight

    @property
    def equityWeight(self):
        return self._equityWeight

    @property
    def period(self):
        return self._period

    @property
    def revenue(self):
        return self._revenue

    @property
    def ebitda(self):
        return self._ebitda

    @property
    def operatingCF(self):
        return self._operatingCF

    @property
    def ebit(self):
        return self._ebit

    @property
    def avgWeightShare(self):
        return self._avgWeightShare

    @property
    def netDebt(self):
        return self._netDebt

    @property
    def inventory(self):
        return self._inventory

    @property
    def receivable(self):
        return self._receivables

    @property
    def payable(self):
        return self._payable

    @property
    def inventoryDiff(self):
        return self._inventoryDiff

    @property
    def receivableDiff(self):
        return self._receivableDiff

    @property
    def payableDiff(self):
        return self._payableDiff

    @property
    def capExp(self):
        return self._capExp

    @property
    def priorRevenue(self):
        return self._priorRevenue

    @property
    def revenuePercent(self):
        return self._revenuePercent

    @property
    def taxRate(self):
        return self._taxRate

    @property
    def ebitdaPercent(self):
        return self._ebitdaPercent

    @property
    def receivablePercent(self):
        return self._receivablePercent

    @property
    def inventoryPercent(self):
        return self._inventoryPercent

    @property
    def payablePercent(self):
        return self._payablePercent

    @property
    def ebitPercent(self):
        return self._ebitPercent

    @property
    def capExpPercent(self):
        return self._capExpPercent

    @property
    def operatingCFPercent(self):
        return self._operatingCFPercent

    @property
    def postTaxCostDebt(self):
        return self._postTaxCostDebt

    @property
    def RP(self):
        return self._marketRiskPremium

    @property
    def growthRateLT(self):
        return self._growthRateLT

    @property
    def costOfEquity(self):
        return self._costOfEquity

    @property
    def WACC(self):
        return self._WACC

    @property
    def cashTaxRate(self):
        return self._cashTaxRate

    @property
    def ebiat(self):
        return self._ebiat
    
    @property
    def ufcf(self):
        return self._ufcf

    @property
    def RF(self):
        return self._riskFreeRate

    @property
    def sumPvUfcf(self):
        return self._sumPvUfcf

    @property
    def terminalValue(self):
        return self._terminalValue

    @property
    def presentTerminalValue(self):
        return self._presentTerminalValue

    @property
    def EV(self):
        return self._EV

    @property
    def equityValue(self):
        return self._equityValue

    @property
    def equityValuePerShare(self):
        return self._equityValuePerShare

    @property
    def freeCashFlowT1(self):
        return self._freeCashFlowT1

    @property
    def costOfDebt(self):
        return self._costOfDebt

    @property
    def dep(self):
        return self._dep

    @property
    def totalCash(self):
        return self._totalCash

    @property
    def depPercent(self):
        return self._depPercent

    @property
    def totalCashPercent(self):
        return self._totalCashPercent

