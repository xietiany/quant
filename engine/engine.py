import numpy as np

class engine(object):

    @classmethod
    def RateConversion(cls, rate):
        return 1 + rate / 100

    @classmethod
    def CAPM(cls, rf, market, beta):
        marketpremium = market - rf
        return rf + beta * marketpremium

    @classmethod
    def WACC(cls, return_on_equity, return_on_debt, equityWeight, debtWeight):
        return (equityWeight * return_on_equity + debtWeight * return_on_debt) / 100

    @classmethod
    def LTGrowthEngine(cls):
        pass

    @classmethod
    def cashflow(cls, starting, growth, RR, period):
        cashflowlist = []
        ending = starting
        growthcent = cls.RateConversion(growth)
        RRcent = cls.RateConversion(RR)
        for i in range(period):
            ending = ending * growthcent / RRcent
            cashflowlist.append(ending)

        return cashflowlist, ending

    @classmethod
    def FCFE(cls, starting, LTGrowth, RR):
        divider = ((RR - LTGrowth) / 100)
        if RR - LTGrowth <= 0:
            print("RR needs to be greater than LTGrowth")
        return starting * (1 + LTGrowth / 100) / divider

    @classmethod
    def FCFETwoStage(cls, starting, firststageGrowth, firststagePeriod, LTGrowth, RR):
        cashflowlist, firststageending = cls.cashflow(starting, firststageGrowth, RR, firststagePeriod)
        terminalValue = cls.FCFE(firststageending, LTGrowth, RR)
        return terminalValue + sum(cashflowlist)

    @classmethod
    def FCFEThreeStage(cls, starting, firststageGrowth, firststagePeriod, secondstageGrowth, secondstagePeriod, LTGrowth, RR):
        cashflowlistfirst, firststageending = cls.cashflow(starting, firststageGrowth, RR, firststagePeriod)
        cashflowlistsecond, secondstageending = cls.cashflow(firststageending, secondstageGrowth, RR, secondstagePeriod)
        terminalValue = cls.FCFE(secondstageending, LTGrowth, RR)
        return terminalValue + sum(cashflowlistfirst) + sum(cashflowlistsecond)

    @classmethod
    def earning(cls, starting, LTGrowth, RR):
        divider = ((RR - LTGrowth) / 100)
        if RR - LTGrowth <= 0:
            print("RR needs to be greater than LTGrowth")
        return starting * (1 + LTGrowth / 100) / divider

    @classmethod
    def earningTwoStage(cls, starting, firststageGrowth, firststagePeriod, LTGrowth, RR):
        cashflowlist, firststageending = cls.cashflow(starting, firststageGrowth, RR, firststagePeriod)
        terminalValue = cls.earning(firststageending, LTGrowth, RR)
        return terminalValue + sum(cashflowlist)

    @classmethod
    def earningThreeStage(cls, starting, firststageGrowth, firststagePeriod, secondstageGrowth, secondstagePeriod, LTGrowth, RR):
        cashflowlistfirst, firststageending = cls.cashflow(starting, firststageGrowth, RR, firststagePeriod)
        cashflowlistsecond, secondstageending = cls.cashflow(firststageending, secondstageGrowth, RR, secondstagePeriod)
        terminalValue = cls.earning(secondstageending, LTGrowth, RR)
        return terminalValue + sum(cashflowlistfirst) + sum(cashflowlistsecond)

    @classmethod
    def GGM(cls):
        pass