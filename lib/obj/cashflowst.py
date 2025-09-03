from lib.util.utility import UtilityMixin
from lib.util.globalvariable import mapping
import akshare as ak

class cashflowst(UtilityMixin):
    global mapping
    def __init__(self, ticker, period):
        # self._url = self.combine_url(ticker, period, datatype)
        # self._raw = self.from_url(self._url)
        if period == "report":
            self._raw = ak.stock_cash_flow_sheet_by_report_em(symbol=ticker).to_dict('index')
        elif period == "quarter": # no quarter report
            self._raw = ak.stock_cash_flow_sheet_by_quarterly_em(symbol=ticker).to_dict('index')
        elif period == "annual":
            self._raw = ak.stock_cash_flow_sheet_by_yearly_em(symbol=ticker).to_dict('index')

        self._dateStr = self.loadkey(self._raw, mapping['date'])
        self._date = [self.dateConversion(each, withAppendix=True) for each in self._dateStr]
        self._currency = self.loadsingle(self._raw, mapping['currency'])

    #     self._netInc = self.loadts(self._raw, mapping['netIncome'], self._date)
    #     self._DA = self.loadts(self._raw, mapping['D&A'], self._date)
    #     self._deferTax = self.loadts(self._raw, mapping['deferIncTax'], self._date)
    #     self._stockComp = self.loadts(self._raw, mapping['stockComp'], self._date)
    #     self._changeWC = self.loadts(self._raw, mapping['changeWC'], self._date)
    #     self._AR = self.loadts(self._raw, mapping['AR'], self._date)
    #     self._inv = self.loadts(self._raw, mapping['inv'], self._date)
    #     self._AP = self.loadts(self._raw, mapping['AP'], self._date)
    #     self._otherWC = self.loadts(self._raw, mapping['otherWC'], self._date)
    #     self._otherNonCash = self.loadts(self._raw, mapping['otherNonCash'], self._date)
    #     self._netCashOpera = self.loadts(self._raw, mapping['netCashOpera'], self._date)
    #     self._investPPE = self.loadts(self._raw, mapping['investPP&E'], self._date)
    #     self._acquisitionNet = self.loadts(self._raw, mapping['acquisitionNet'], self._date)
    #     self._purchaseInvest = self.loadts(self._raw, mapping['purchaseInvest'], self._date)
    #     self._salesMat = self.loadts(self._raw, mapping['salesMaturities'], self._date)
    #     self._otherInvest = self.loadts(self._raw, mapping['otherInvest'], self._date)
    #     self._netCashInvest = self.loadts(self._raw, mapping['netCashInvest'], self._date)      
    #     self._debtRepay = self.loadts(self._raw, mapping['debtRepay'], self._date)
    #     self._stockIss = self.loadts(self._raw, mapping['commonStockIss'], self._date)
    #     self._stockRep = self.loadts(self._raw, mapping['commonStockRep'], self._date)
    #     self._div = self.loadts(self._raw, mapping['dividend'], self._date)
    #     self._otherFinance = self.loadts(self._raw, mapping['otherFinance'], self._date)
    #     self._netCashFinance = self.loadts(self._raw, mapping['netCashFinance'], self._date)
    #     self._effectFX = self.loadts(self._raw, mapping['effectFX'], self._date)
    #     self._cashEnd = self.loadts(self._raw, mapping['cashEnd'], self._date)
    #     self._cashBegin = self.loadts(self._raw, mapping['cashBegin'], self._date)
        self._operaCF = self.loadts(self._raw, mapping['operaCF'], self._date)
        self._capitalExp = self.loadts(self._raw, mapping['capitalExp'], self._date)
        # self._freeCF = self.loadts(self._raw, mapping['freeCF'], self._date)
        self._init() # calculate some non-fetch variable

    def _init(self):
        '''
        Calculate free cash flow
        '''
        self._freeCF = self._operaCF - self._capitalExp
        
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

    # @property
    # def netInc(self):
    #     return self._netInc

    # @property
    # def DA(self):
    #     return self._DA
    
    # @property
    # def deferTax(self):
    #     return self._deferTax

    # @property
    # def stockComp(self):
    #     return self._stockComp

    # @property
    # def chagneWC(self):
    #     return self._changeWC

    # @property
    # def AR(self):
    #     return self._AR

    # @property
    # def inv(self):
    #     return self._inv

    # @property
    # def AP(self):
    #     return self._AP
    
    # @property
    # def otherWC(self):
    #     return self._otherWC

    # @property
    # def otherNonCash(self):
    #     return self._otherNonCash

    # @property
    # def netCashOpera(self):
    #     return self._netCashOpera

    # @property
    # def investPPE(self):
    #     return self._investPPE

    # @property
    # def acquisitionNet(self):
    #     return self._acquisitionNet

    # @property
    # def purchaseInvest(self):
    #     return self._purchaseInvest

    # @property
    # def salesMat(self):
    #     return self._salesMat

    # @property
    # def otherInvest(self):
    #     return self._otherInvest

    # @property
    # def netCashInvest(self):
    #     return self._netCashInvest

    # @property
    # def debtRepay(self):
    #     return self._debtRepay

    # @property
    # def stockIss(self):
    #     return self._stockIss

    # @property
    # def stockRep(self):
    #     return self._stockRep

    # @property
    # def div(self):
    #     return self._div

    # @property
    # def otherFinance(self):
    #     return self._otherFinance

    # @property
    # def netCashFinance(self):
    #     return self._netCashFinance

    # @property
    # def effectFX(self):
    #     return self._effectFX

    # @property
    # def cashEnd(self):
    #     return self._cashEnd

    # @property
    # def cashBegin(self):
    #     return self._cashBegin

    @property
    def operaCF(self):
        return self._operaCF

    @property
    def capitalExp(self):
        return self._capitalExp

    @property
    def freeCF(self):
        return self._freeCF
