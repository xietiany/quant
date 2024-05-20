from incomest import incomest
from balancest import balancest
from cashflowst import cashflowst

class stock(object):
    
    def __init__(self, ticker, period = "annual", report = False):
        self._ticker = ticker
        self._period = period
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