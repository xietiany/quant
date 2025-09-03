from lib.util.utility import UtilityMixin
from lib.util.globalvariable import ratioMapping

class ratio(UtilityMixin):
    global ratioMapping
    def __init__(self, ticker, period, datatype):
        self._url = self.combine_url(ticker, period, datatype)
        self._raw = self.from_url(self._url)

        self._date = self.loadkey(self._raw, ratioMapping['date'])
        self._year = self.loadkey(self._raw, ratioMapping['year'])
        self._symbol = self.loadsingle(self._raw, ratioMapping['symbol'])
        self._period = self.loadsingle(self._raw, ratioMapping['period'])
        self._revShare = self.loadts(self._raw, ratioMapping['revShare'], self._date)
        self._NIShare = self.loadts(self._raw, ratioMapping['NIShare'], self._date)
        self._OperaCFShare = self.loadts(self._raw, ratioMapping['OperaCFShare'], self._date)
        self._FCFShare = self.loadts(self._raw, ratioMapping['FCFShare'], self._date)
        self._cashShare = self.loadts(self._raw, ratioMapping['cashShare'], self._date)
        self._BVShare = self.loadts(self._raw, ratioMapping['BVShare'], self._date)
        self._tangibleBVShare = self.loadts(self._raw, ratioMapping['tangibleBVShare'], self._date)
        self._SHEquityShare = self.loadts(self._raw, ratioMapping['SHEquityShare'], self._date)
        self._interestDebtShare = self.loadts(self._raw, ratioMapping['interestDebtShare'], self._date)
        self._MV = self.loadts(self._raw, ratioMapping['MV'], self._date)
        self._EV = self.loadts(self._raw, ratioMapping['EV'], self._date)
        self._PE = self.loadts(self._raw, ratioMapping['PE'], self._date)
        self._PS = self.loadts(self._raw, ratioMapping['PS'], self._date)
        self._PCF = self.loadts(self._raw, ratioMapping['PCF'], self._date)
        self._PFCF = self.loadts(self._raw, ratioMapping['PFCF'], self._date)
        self._PB = self.loadts(self._raw, ratioMapping['PB'], self._date)
        self._PTB = self.loadts(self._raw, ratioMapping['PTB'], self._date)
        self._EVtoSales = self.loadts(self._raw, ratioMapping['EVtoSales'], self._date)
        self._EVtoEBITDA = self.loadts(self._raw, ratioMapping['EVtoEBITDA'], self._date)
        self._EVtoOperaCF = self.loadts(self._raw, ratioMapping['EVtoOperaCF'], self._date)
        self._EVtoFCF = self.loadts(self._raw, ratioMapping['EVtoFCF'], self._date)
        self._EarningYield = self.loadts(self._raw, ratioMapping['EarningYield'], self._date)
        self._FCFYield = self.loadts(self._raw, ratioMapping['FCFYield'], self._date)
        self._debtEquity = self.loadts(self._raw, ratioMapping['debtEquity'], self._date)
        self._debtAsset = self.loadts(self._raw, ratioMapping['debtAsset'], self._date)
        self._netDebtEBITDA = self.loadts(self._raw, ratioMapping['netDebtEBITDA'], self._date)
        self._CA = self.loadts(self._raw, ratioMapping['CA'], self._date)
        self._IntCoverage = self.loadts(self._raw, ratioMapping['IntCoverage'], self._date)
        self._IncQuality = self.loadts(self._raw, ratioMapping['IncQuality'], self._date)
        self._dividendYield = self.loadts(self._raw, ratioMapping['dividendYield'], self._date)
        self._payoutRatio = self.loadts(self._raw, ratioMapping['payoutRatio'], self._date)
        self._AdmintoRevenue = self.loadts(self._raw, ratioMapping['AdmintoRevenue'], self._date)
        self._RDtoRevenue = self.loadts(self._raw, ratioMapping['research&developtoRevenue'], self._date)
        self._intangibletoAsset = self.loadts(self._raw, ratioMapping['intangibletoAsset'], self._date)
        self._CapExtoOperaCF = self.loadts(self._raw, ratioMapping['CapExtoOperaCF'], self._date)
        self._CapExtoRevenue = self.loadts(self._raw, ratioMapping['CapExtoRevenue'], self._date)
        self._CapExtoDepre = self.loadts(self._raw, ratioMapping['CapExtoDepre'], self._date)
        self._stockComptoRevenue = self.loadts(self._raw, ratioMapping['stockComptoRevenue'], self._date)
        self._grahamNumber = self.loadts(self._raw, ratioMapping['grahamNumber'], self._date)
        self._ROIC = self.loadts(self._raw, ratioMapping['ROIC'], self._date)
        self._ROTangibleAsset = self.loadts(self._raw, ratioMapping['ROTangibleAsset'], self._date)
        self._grahamNetNet = self.loadts(self._raw, ratioMapping['grahamNetNet'], self._date)
        self._WC = self.loadts(self._raw, ratioMapping['WC'], self._date)
        self._tangibleAsset = self.loadts(self._raw, ratioMapping['tangibleAsset'], self._date)
        self._netCurrentAsset = self.loadts(self._raw, ratioMapping['netCurrentAsset'], self._date)
        self._investedCapital = self.loadts(self._raw, ratioMapping['investedCapital'], self._date)
        self._avgReceivables = self.loadts(self._raw, ratioMapping['avgReceivables'], self._date)
        self._avgPayables = self.loadts(self._raw, ratioMapping['avgPayables'], self._date)
        self._avgInv = self.loadts(self._raw, ratioMapping['avgInv'], self._date)
        self._daysSalesOutstanding = self.loadts(self._raw, ratioMapping['daysSalesOutstanding'], self._date)
        self._daysPayablesOutstanding = self.loadts(self._raw, ratioMapping['daysPayablesOutstanding'], self._date)
        self._daysInv = self.loadts(self._raw, ratioMapping['daysInv'], self._date)
        self._receivablesTurnover = self.loadts(self._raw, ratioMapping['receivablesTurnover'], self._date)
        self._payablesTurnover = self.loadts(self._raw, ratioMapping['payablesTurnover'], self._date)
        self._InvTurnover = self.loadts(self._raw, ratioMapping['InvTurnover'], self._date)
        self._ROE = self.loadts(self._raw, ratioMapping['ROE'], self._date)
        self._CapExShare = self.loadts(self._raw, ratioMapping['CapExShare'], self._date)

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
    def date(self):
        return self._date

    @property
    def symbol(self):
        return self._symbol

    @property
    def period(self):
        return self._period

    @property
    def revShare(self):
        return self._revShare

    @property
    def NIShare(self):
        return self._NIShare

    @property
    def OperaCFShare(self):
        return self._OperaCFShare

    @property
    def FCFShare(self):
        return self._FCFShare

    @property
    def cashShare(self):
        return self._cashShare

    @property
    def BVShare(self):
        return self._BVShare

    @property
    def tangibleBVShare(self):
        return self._tangibleBVShare

    @property
    def SHEquityShare(self):
        return self._SHEquityShare

    @property
    def interestDebtShare(self):
        return self._interestDebtShare

    @property
    def MV(self):
        return self._MV

    @property
    def EV(self):
        return self._EV

    @property
    def PE(self):
        return self._PE

    @property
    def PS(self):
        return self._PS

    @property
    def PCF(self):
        return self._PCF

    @property
    def PFCF(self):
        return self._PFCF

    @property
    def PB(self):
        return self._PB

    @property
    def PTB(self):
        return self._PTB

    @property
    def EVtoSales(self):
        return self._EVtoSales

    @property
    def EVtoEBITDA(self):
        return self._EVtoEBITDA

    @property
    def EVtoOperaCF(self):
        return self._EVtoOperaCF

    @property
    def EVtoFCF(self):
        return self._EVtoFCF

    @property
    def EarningYield(self):
        return self._EarningYield

    @property
    def FCFYield(self):
        return self._FCFYield

    @property
    def debtEquity(self):
        return self._debtEquity

    @property
    def debtAsset(self):
        return self._debtAsset

    @property
    def netDebtEBITDA(self):
        return self._netDebtEBITDA

    @property
    def CA(self):
        return self._CA

    @property
    def IntCoverage(self):
        return self._IntCoverage

    @property
    def IncQuality(self):
        return self._IncQuality

    @property
    def dividendYield(self):
        return self._dividendYield

    @property
    def payoutRatio(self):
        return self._payoutRatio

    @property
    def AdmintoRevenue(self):
        return self._AdmintoRevenue

    @property
    def RDtoRevenue(self):
        return self._RDtoRevenue

    @property
    def intangibletoAsset(self):
        return self._intangibletoAsset

    @property
    def CapExtoOperaCF(self):
        return self._CapExtoOperaCF

    @property
    def CapExtoRevenue(self):
        return self._CapExtoRevenue

    @property
    def CapExtoDepre(self):
        return self._CapExtoDepre

    @property
    def stockComptoRevenue(self):
        return self._stockComptoRevenue

    @property
    def grahamNumber(self):
        return self._grahamNumber

    @property
    def ROIC(self):
        return self._ROIC

    @property
    def ROTangibleAsset(self):
        return self._ROTangibleAsset

    @property
    def grahamNetNet(self):
        return self._grahamNetNet

    @property
    def WC(self):
        return self._WC

    @property
    def tangibleAsset(self):
        return self._tangibleAsset

    @property
    def netCurrentAsset(self):
        return self._netCurrentAsset

    @property
    def investedCapital(self):
        return self._investedCapital

    @property
    def avgReceivables(self):
        return self._avgReceivables

    @property
    def avgPayables(self):
        return self._avgPayables

    @property
    def avgInv(self):
        return self._avgInv

    @property
    def daysSalesOutstanding(self):
        return self._daysSalesOutstanding

    @property
    def daysPayablesOutstanding(self):
        return self._daysPayablesOutstanding

    @property
    def daysInv(self):
        return self._daysInv

    @property
    def receivablesTurnover(self):
        return self._receivablesTurnover

    @property
    def payablesTurnover(self):
        return self._payablesTurnover

    @property
    def InvTurnover(self):
        return self._InvTurnover

    @property
    def ROE(self):
        return self._ROE

    @property
    def CapExShare(self):
        return self._CapExShare