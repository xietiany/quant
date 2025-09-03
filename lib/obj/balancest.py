from lib.util.utility import UtilityMixin
from lib.util.globalvariable import mapping
import akshare as ak

class balancest(UtilityMixin):
    global mapping
    def __init__(self, ticker, period):
        # self._url = self.combine_url(ticker, period, datatype)
        # self._raw = self.from_url(self._url)
        if period == "report":
            self._raw = ak.stock_balance_sheet_by_report_em(symbol=ticker).to_dict('index')
        elif period == "quarter": # no quarter report
            self._raw = ak.stock_balance_sheet_by_report_em(symbol=ticker).to_dict('index')
        elif period == "annual":
            self._raw = ak.stock_balance_sheet_by_yearly_em(symbol=ticker).to_dict('index')

        self._dateStr = self.loadkey(self._raw, mapping['date'])
        self._date = [self.dateConversion(each, withAppendix=True) for each in self._dateStr]
        self._currency = self.loadsingle(self._raw, mapping['currency'])
        self._cashEqui = self.loadts(self._raw, mapping['cash&equival'], self._date)
        self._AR = self.loadts(self._raw, mapping['accountsReceivable'], self._date)
        self._noteReceivable = self.loadts(self._raw, mapping['noteReceivable'], self._date)
        self._AP = self.loadts(self._raw, mapping['accountsPayable'], self._date)
        self._unearnedRevenue = self.loadts(self._raw, mapping['unearnedRevenue'], self._date)
        self._prepaidExpense = self.loadts(self._raw, mapping['prepaidExpense'], self._date)
        self._fixedAsset = self.loadts(self._raw, mapping['fixedAsset'], self._date)
        self._fixedAssetUnderConstruct = self.loadts(self._raw, mapping['fixedAssetUnderConstruct'], self._date)
        self._useRightAsset = self.loadts(self._raw, mapping['useRightAsset'], self._date)
        self._investedAsset = self.loadts(self._raw, mapping['investedAsset'], self._date)
        self._intangibleAsset = self.loadts(self._raw, mapping['intangibleAsset'], self._date)
        self._goodwill = self.loadts(self._raw, mapping['goodwill'], self._date)

        # self._cashEqui = self.loadts(self._raw, mapping['cash&equival'], self._date)
        # self._stInvest = self.loadts(self._raw, mapping['shortTermInvest'], self._date)
        # self._cashSTInvest = self.loadts(self._raw, mapping['cash&short'], self._date)
        # self._netReceivables = self.loadts(self._raw, mapping['netReceivables'], self._date)
        # self._otherCurAsset = self.loadts(self._raw, mapping['otherCurAsset'], self._date)
        # self._totalCurAsset = self.loadts(self._raw, mapping['totalCurAsset'], self._date)
        # self._PPE = self.loadts(self._raw, mapping['PP&E'], self._date)
        # self._goodwill = self.loadts(self._raw, mapping['goodwill'], self._date)
        # self._intangibleAsset = self.loadts(self._raw, mapping['intangibleAsset'], self._date)
        # self._goodwillIntangibleAsset = self.loadts(self._raw, mapping['goodwill&intangible'], self._date)
        # self._ltInvest = self.loadts(self._raw, mapping['longTermInvest'], self._date)
        # self._taxAsset = self.loadts(self._raw, mapping['taxAsset'], self._date)
        # self._otherNonCurAsset = self.loadts(self._raw, mapping['otherNonCurAsset'], self._date)
        # self._totalNonCurAsset = self.loadts(self._raw, mapping['totalNonCurAsset'], self._date)
        # self._otherAsset = self.loadts(self._raw, mapping['otherAsset'], self._date)
        # self._totalAsset = self.loadts(self._raw, mapping['totalAsset'], self._date)
        self._inv = self.loadts(self._raw, mapping['inv'], self._date)
        # self._AP = self.loadts(self._raw, mapping['APs'], self._date)
        self._stDebt = self.loadts(self._raw, mapping['shortTermDebt'], self._date)
        self._notePayable = self.loadts(self._raw, mapping['notePayable'], self._date)
        # self._taxPayable = self.loadts(self._raw, mapping['taxPayable'], self._date)
        # self._DR = self.loadts(self._raw, mapping['DR'], self._date)
        # self._otherCurLiability = self.loadts(self._raw, mapping['otherCurLiability'], self._date)
        # self._totalCurLiability = self.loadts(self._raw, mapping['totalCurLiability'], self._date)
        self._ltDebt = self.loadts(self._raw, mapping['longTermDebt'], self._date)
        self._bondPayable = self.loadts(self._raw, mapping['bondPayable'], self._date)
        # self._DRNonCur = self.loadts(self._raw, mapping['DRNonCur'], self._date)
        # self._deferTaxLiabilityNonCur = self.loadts(self._raw, mapping['deferTaxLiabilityNonCur'], self._date)
        # self._otherNonCurLiability = self.loadts(self._raw, mapping['otherNonCurLiability'], self._date)
        # self._totalNonCurLiability = self.loadts(self._raw, mapping['totalNonCurLiability'], self._date)
        # self._otherLiability = self.loadts(self._raw, mapping['otherLiability'], self._date)
        self._capitalLease = self.loadts(self._raw, mapping['capitalLease'], self._date)
        # self._totalLiability = self.loadts(self._raw, mapping['totalLiability'], self._date) 
        # self._preStock = self.loadts(self._raw, mapping['preStock'], self._date)
        # self._comStock = self.loadts(self._raw, mapping['comStock'], self._date)
        # self._RE = self.loadts(self._raw, mapping['RE'], self._date)
        # self._otherComprehensivePL = self.loadts(self._raw, mapping['otherComprehensivePL'], self._date)
        # self._otherTotalEquity = self.loadts(self._raw, mapping['otherTotalEquity'], self._date)
        # self._totalStockEquity = self.loadts(self._raw, mapping['totalStockEquity'], self._date)
        # self._totalEquity = self.loadts(self._raw, mapping['totalEquity'], self._date)
        # self._totalLStockE = self.loadts(self._raw, mapping['totalL&StockE'], self._date)
        # self._minorInt = self.loadts(self._raw, mapping['minorInt'], self._date)
        # self._totalLE = self.loadts(self._raw, mapping['totalL&E'], self._date)
        # self._totalInvest = self.loadts(self._raw, mapping['totalInvest'], self._date)
        # self._totalDebt = self.loadts(self._raw, mapping['totalDebt'], self._date)
        # self._netDebt = self.loadts(self._raw, mapping['netDebt'], self._date)
    
    @property
    def raw(self):
        return self._raw
    
    # @property
    # def url(self):
    #     return self._url

    @property
    def date(self):
        return self._date

    @property
    def currency(self):
        return self._currency

    @property
    def cashEqui(self):
        return self._cashEqui

    @property
    def AR(self):
        return self._AR

    @property
    def noteReceivable(self):
        return self._noteReceivable

    @property
    def AP(self):
        return self._AP

    @property
    def unearnedRevenue(self):
        return self._unearnedRevenue
    
    @property
    def prepaidExpense(self):
        return self._prepaidExpense

    @property
    def fixedAsset(self):
        return self._fixedAsset

    @property
    def fixedAssetUnderConstruct(self):
        return self._fixedAssetUnderConstruct

    @property
    def useRightAsset(self):
        return self._useRightAsset  

    @property
    def investedAsset(self):
        return self._investedAsset  

    @property
    def goodwill(self):
        return self._goodwill
    
    @property
    def intangibleAsset(self):
        return self._intangibleAsset

    # @property
    # def stInvest(self):
    #     return self._stInvest

    # @property
    # def cashSTInvest(self):
    #     return self._cashSTInvest

    # @property
    # def netReceivables(self):
    #     return self._netReceivables

    # @property
    # def otherCurAsset(self):
    #     return self._otherCurAsset

    # @property
    # def totalCurAsset(self):
    #     return self._totalCurAsset

    # @property
    # def PPE(self):
    #     return self._PPE

    # @property
    # def goodwill(self):
    #     return self._goodwill

    # @property
    # def intangibleAsset(self):
    #     return self._intangibleAsset

    # @property
    # def goodwillIntangibleAsset(self):
    #     return self._goodwillIntangibleAsset

    @property
    def ltInvest(self):
        return self._ltInvest

    # @property
    # def taxAsset(self):
    #     return self._taxAsset

    # @property
    # def otherNonCurAsset(self):
    #     return self._otherNonCurAsset

    # @property
    # def totalNonCurAsset(self):
    #     return self._totalNonCurAsset

    # @property
    # def otherAsset(self):
    #     return self._otherAsset

    # @property
    # def totalAsset(self):
    #     return self._totalAsset

    @property
    def inv(self):
        return self._inv

    # @property
    # def AP(self):
    #     return self._AP

    @property
    def stDebt(self):
        return self._stDebt

    @property
    def notePayable(self):
        return self._notePayable

    # @property
    # def taxPayable(self):
    #     return self._taxPayable

    # @property
    # def DR(self):
    #     return self._DR

    # @property
    # def otherCurLiability(self):
    #     return self._otherCurLiability

    # @property
    # def totalCurLiability(self):
    #     return self._totalCurLiability

    @property
    def ltDebt(self):
        return self._ltDebt

    @property
    def bondPayable(self):
        return self._bondPayable

    # @property
    # def DRNonCur(self):
    #     return self._DRNonCur

    # @property
    # def deferTaxLiabilityNonCur(self):
    #     return self._deferTaxLiabilityNonCur

    # @property
    # def otherNonCurLiability(self):
    #     return self._otherNonCurAsset

    # @property
    # def totalNonCurLiability(self):
    #     return self._totalNonCurLiability

    # @property
    # def otherLiability(self):
    #     return self._otherLiability

    @property
    def capitalLease(self):
        return self._capitalLease

    # @property
    # def totalLiability(self):
    #     return self._totalLiability

    # @property
    # def preStock(self):
    #     return self._preStock

    # @property
    # def comStock(self):
    #     return self._comStock

    # @property
    # def RE(self):
    #     return self._RE

    # @property
    # def otherComprehensivePL(self):
    #     return self._otherComprehensivePL

    # @property
    # def otherTotalEquity(self):
    #     return self._otherTotalEquity

    # @property
    # def totalStockEquity(self):
    #     return self._totalStockEquity

    # @property
    # def totalEquity(self):
    #     return self._totalEquity

    # @property
    # def totalLStockE(self):
    #     return self._totalLStockE

    # @property
    # def minorInt(self):
    #     return self._minorInt

    # @property
    # def totalLE(self):
    #     return self._totalLE

    # @property
    # def totalInvest(self):
    #     return self._totalInvest

    # @property
    # def totalDebt(self):
    #     return self._totalDebt

    # @property
    # def netDebt(self):
    #     return self._netDebt