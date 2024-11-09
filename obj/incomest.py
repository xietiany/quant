from util.utility import UtilityMixin
from util.globalvariable import mapping

class incomest(UtilityMixin):
    global mapping
    def __init__(self, ticker, period, datatype):
        self._url = self.combine_url(ticker, period, datatype)
        self._raw = self.from_url(self._url)
        
        self._date = self.loadkey(self._raw, mapping['date'])
        self._currency = self.loadsingle(self._raw, mapping['currency'])
        self._revenue = self.loadts(self._raw, mapping['revenue'], self._date)
        self._grossprofit = self.loadts(self._raw, mapping['grossProfit'], self._date)
        self._margin = self.loadts(self._raw, mapping['margin'], self._date)
        
        self._rdExp = self.loadts(self._raw, mapping['R&DExpense'], self._date)
        self._adminExp = self.loadts(self._raw, mapping['AdminExpense'], self._date)
        self._marketExp = self.loadts(self._raw, mapping['MarketingExpense'], self._date)
        self._generalExp = self.loadts(self._raw, mapping['Admin&MarketingExpense'], self._date)
        self._otherExp = self.loadts(self._raw, mapping['otherExpense'], self._date)
        self._operaExp = self.loadts(self._raw, mapping['operatingExpense'], self._date)
        self._exp = self.loadts(self._raw, mapping['cost&expense'], self._date)
        
        self._intInc = self.loadts(self._raw, mapping['interstIncome'], self._date)
        self._intExp = self.loadts(self._raw, mapping['interstExpense'], self._date)
        self._DA = self.loadts(self._raw, mapping['D&A'], self._date)
        self._ebitdaRatio = self.loadts(self._raw, mapping['ebitdaRatio'], self._date)
        self._ebitda = self.loadts(self._raw, mapping['ebitda'], self._date)
        self._operaInc = self.loadts(self._raw, mapping['operatingIncome'], self._date)
        self._operaIncRatio = self.loadts(self._raw, mapping['operatingIncomeRatio'], self._date)
        self._totalOtherInc = self.loadts(self._raw, mapping['totalOtherIncomeExpensesNet'], self._date)
        self._incBeforeTax = self.loadts(self._raw, mapping['incomeBeforeTax'], self._date)
        self._incBeforeTaxRatio = self.loadts(self._raw, mapping['incomeBeforeTaxRatio'], self._date)
        self._taxExp = self.loadts(self._raw, mapping['incomeTaxExpense'], self._date)
        
        self._netInc = self.loadts(self._raw, mapping['netIncome'], self._date)
        self._netIncRatio = self.loadts(self._raw, mapping['netIncomeRatio'], self._date)
        
        self._eps = self.loadts(self._raw, mapping['eps'], self._date)
        self._epsdilute = self.loadts(self._raw, mapping['epsdiluted'], self._date)
        self._shares = self.loadts(self._raw, mapping['weightedAverageShsOut'], self._date)
        self._sharesdilute = self.loadts(self._raw, mapping['weightedAverageShsOutDil'], self._date)
        
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
    def currency(self):
        return self._currency
    
    @property
    def revenue(self):
        return self._revenue
    
    @property
    def grossprofit(self):
        return self._grossprofit
    
    @property
    def margin(self):
        return self._margin
    
    @property
    def rdExp(self):
        return self._rdExp
    
    @property
    def adminExp(self):
        return self._adminExp

    @property
    def marketExp(self):
        return self._marketExp

    @property
    def generalExp(self):
        return self._generalExp
    
    @property
    def otherExp(self):
        return self._otherExp

    @property
    def operaExp(self):
        return self._operaExp

    @property
    def exp(self):
        return self._exp

    @property
    def intInc(self):
        return self._intInc

    @property
    def intExp(self):
        return self._intExp

    @property
    def DA(self):
        return self._DA

    @property
    def ebitdaRatio(self):
        return self._ebitdaRatio

    @property
    def ebitda(self):
        return self._ebitda

    @property
    def operaInc(self):
        return self._operaInc

    @property
    def operaIncRatio(self):
        return self._operaIncRatio

    @property
    def totalOtherInc(self):
        return self._totalOtherInc

    @property
    def incBeforeTax(self):
        return self._incBeforeTax

    @property
    def incBeforeTaxRatio(self):
        return self._incBeforeTaxRatio

    @property
    def taxExp(self):
        return self._taxExp

    @property
    def netInc(self):
        return self._netInc
    
    @property
    def netIncRatio(self):
        return self._netIncRatio
    
    @property
    def eps(self):
        return self._eps
    
    @property
    def epsdilute(self):
        return self._epsdilute
    
    @property
    def shares(self):
        return self._shares
    
    @property
    def sharesdilute(self):
        return self._sharesdilute
    