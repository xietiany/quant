mapping = {
    ### ------------------------------- ###
    ### income statement variable ###
    ### ------------------------------- ###
    'date': 'REPORT_DATE',
    'currency': 'CURRENCY',
    'revenue': 'OPERATE_INCOME',
    'operaCost': 'OPERATE_COST',
    # 'grossProfit': 'grossProfit',
    # 'margin': 'grossProfit',
    # 'Admin&MarketingExpense': 'sellingGeneralAndAdministrativeExpenses',
    'MarketingExpense': 'SALE_EXPENSE',
    'AdminExpense': 'MANAGE_EXPENSE',
    'R&DExpense': 'RESEARCH_EXPENSE',
    'financeExp': 'FINANCE_EXPENSE',
    'operaTax': 'OPERATE_TAX_ADD',
    # 'otherExpense': 'otherExpenses',
    # 'operatingExpense': 'operatingExpenses',
    # 'cost&expense': 'costAndExpenses',
    'interstIncome': 'FE_INTEREST_INCOME',
    'interstExpense': 'FE_INTEREST_EXPENSE',
    'assetImpairment': 'ASSET_IMPAIRMENT_INCOME',
    'asseetDispose': 'ASSET_DISPOSAl_INCOME',
    'creditImpairment': 'CREDIT_IMPAIRMENT_INCOME', #  Is this goodwill?
    'otherInc': 'OTHER_INCOME',
    # 'D&A': 'depreciationAndAmortization',
    # 'ebitda': 'ebitda',
    # 'ebitdaRatio': 'ebitdaratio',
    # 'operatingIncome': 'operatingIncome',
    # 'operatingIncomeRatio': 'operatingIncomeRatio',
    # 'totalOtherIncomeExpensesNet': 'totalOtherIncomeExpensesNet',
    # 'incomeBeforeTax': 'incomeBeforeTax',
    # 'incomeBeforeTaxRatio': 'incomeBeforeTaxRatio',
    # 'incomeTaxExpense': 'incomeTaxExpense',
    'netIncome': 'NETPROFIT',
    'parentNetIncome': 'PARENT_NETPROFIT', #  Is this net income?
    # 'netIncomeRatio': 'netIncomeRatio',
    'eps': 'BASIC_EPS',
    # 'epsdiluted': 'epsdiluted',
    # 'weightedAverageShsOut': 'weightedAverageShsOut',
    # 'weightedAverageShsOutDil': 'weightedAverageShsOutDil',
    'operate_cost': "OPERATE_COST", # 
    'total_operate_cost': "TOTAL_OPERATE_COST",
    ### ------------------------------- ###
    ### income statement variable ###
    ### ------------------------------- ###
    ### cashflow statement variable ###
    ### ------------------------------- ###
    # 'deferIncTax': 'deferredIncomeTax',
    # 'stockComp': 'stockBasedCompensation',
    # 'changeWC': 'changeInWorkingCapital',
    # 'AR': 'accountsReceivables',
    # 'AP': 'accountsPayables',
    # 'otherWC': 'otherWorkingCapital',
    # 'otherNonCash': 'otherNonCashItems',
    # 'netCashOpera': 'netCashProvidedByOperatingActivities',
    # 'investPP&E': 'investmentsInPropertyPlantAndEquipment',
    # 'acquisitionNet': 'acquisitionsNet',
    # 'purchaseInvest': 'purchasesOfInvestments',
    # 'salesMaturities': 'salesMaturitiesOfInvestments',
    # 'otherInvest': 'otherInvestingActivites',
    # 'netCashInvest': 'netCashUsedForInvestingActivites',
    # 'debtRepay': 'debtRepayment',
    # 'commonStockIss': 'commonStockIssued',
    # 'commonStockRep': 'commonStockRepurchased',
    # 'dividend': 'dividendsPaid',
    # 'otherFinance': 'otherFinancingActivites',
    # 'netCashFinance': 'netCashUsedProvidedByFinancingActivities',
    # 'effectFX': 'effectOfForexChangesOnCash',
    # 'netChangeCash': 'netChangeInCash',
    # 'cashEnd': 'cashAtEndOfPeriod',
    # 'cashBegin': 'cashAtBeginningOfPeriod',
    'operaCF': 'NETCASH_OPERATENOTE',
    'capitalExp': 'CONSTRUCT_LONG_ASSET',
    # 'freeCF': 'freeCashFlow',
    ### ------------------------------- ###
    ### cashflow statement variable ###
    ### ------------------------------- ###
    ### balancesheet statement variable ###
    ### ------------------------------- ###
    'cash&equival': 'MONETARYFUNDS',
    # 'shortTermInvest': 'shortTermInvestments',
    # 'cash&short': 'cashAndShortTermInvestments',
    # 'netReceivables': 'netReceivables',
    'accountsReceivable': 'ACCOUNTS_RECE',
    'noteReceivable': 'NOTE_RECE',
    'accountsPayable': 'ACCOUNTS_PAYABLE',
    # 'notePayable': 'NOTE_PAYABLE', # this in is below
    'unearnedRevenue': 'ADVANCE_RECEIVABLES', # this is unearned revenue, liability
    'prepaidExpense': 'PREPAYMENT', # this is prepaid expense, asset
    'fixedAsset': 'FIXED_ASSET', # part of PPE
    'fixedAssetUnderConstruct': 'CIP', # part of PPE
    'useRightAsset': 'USERIGHT_ASSET', # part of PPE
    'investedAsset': 'INVEST_REALESTATE',
    'intangibleAsset': 'INTANGIBLE_ASSET',
    'goodwill': 'GOODWILL',
    # ## 'inventory', ## In cashflow statement, there is inv map
    # 'otherCurAsset': 'otherCurrentAssets',
    # 'totalCurAsset': 'totalCurrentAssets',
    # 'PP&E': 'propertyPlantEquipmentNet',
    # 'goodwill': 'goodwill',
    # 'intangibleAsset': 'intangibleAssets',
    # 'goodwill&intangible': 'goodwillAndIntangibleAssets',
    # 'longTermInvest': 'longTermInvestments',
    # 'taxAsset': 'taxAssets',
    # 'otherNonCurAsset': 'otherNonCurrentAssets',
    # 'totalNonCurAsset': 'totalNonCurrentAssets',
    # 'otherAsset': 'otherAssets',
    # 'totalAsset': 'totalAssets',
    # 'APs': 'accountPayables',
    'shortTermDebt': 'SHORT_LOAN',
    'notePayable': 'NOTE_PAYABLE',
    'inv': 'INVENTORY',
    # 'taxPayable': 'taxPayables',
    # 'DR': 'deferredRevenue',
    # 'otherCurLiability': 'otherCurrentLiabilities',
    # 'totalCurLiability': 'totalCurrentLiabilities',
    'longTermDebt': 'LONG_LOAN',
    # 'DRNonCur': 'deferredRevenueNonCurrent',
    # 'deferTaxLiabilityNonCur': 'deferredTaxLiabilitiesNonCurrent',
    # 'otherNonCurLiability': 'otherNonCurrentLiabilities',
    # 'totalNonCurLiability': 'totalNonCurrentLiabilities',
    # 'otherLiability': 'otherLiabilities',
    'capitalLease': 'LEASE_LIAB',
    'bondPayable': 'BOND_PAYABLE',
    # 'totalLiability': 'totalLiabilities',
    # 'preStock': 'preferredStock', 
    # 'comStock': 'commonStock', 
    # 'RE': 'retainedEarnings',
    # 'otherComprehensivePL': 'accumulatedOtherComprehensiveIncomeLoss',
    # 'otherTotalEquity': 'othertotalStockholdersEquity',
    # 'totalStockEquity': 'totalStockholdersEquity',
    # 'totalEquity': 'totalEquity',
    # 'totalL&StockE': 'totalLiabilitiesAndStockholdersEquity',
    # 'minorInt': 'minorityInterest',
    # 'totalL&E': 'totalLiabilitiesAndTotalEquity',
    # 'totalInvest': 'totalInvestments',
    # 'totalDebt': 'totalDebt',
    'netDebt': 'netDebt'
    ### balancesheet statement variable ###
    ### ------------------------------- ###
}

valuationMapping = {
    ### Advanced DCF ###
    'year': 'year',
    'price': "price",
    'beta': 'beta',
    'finalTaxRate': 'finalTaxRate',
    'totalDebt': "totalDebt",
    'totalEquity': "totalEquity",
	'totalCapital': "totalCapital",
	'dilutedShare': "dilutedSharesOutstanding",
	'debtWeight': "debtWeighting",
	'equityWeight': "equityWeighting",
	'period': "period",
	'revenue': "revenue",
	'ebitda': "ebitda",
	'operatingCF': "operatingCashFlow",
	'ebit': "ebit",
	'avgWeightShare': "weightedAverageShsOutDil",
	'netDebt': "netDebt",
	'inventory': "inventories",
	'receivables': "receivables",
	'payable': "payable",
	'inventoryDiff': "inventoriesChange",
	'receivableDiff': "receivablesChange",
	'payableDiff': "payableChange",
	'capExp': "capitalExpenditure",
	'priorRevenue': "previousRevenue",
	'revenuePercent': "revenuePercentage",
	'taxRate': "taxRate",
	'ebitdaPercent': "ebitdaPercentage",
	'receivablePercent': "receivablesPercentage",
	'inventoryPercent': "inventoriesPercentage",
	'payablePercent': "payablePercentage",
	'ebitPercent': "ebitPercentage",
	'capExpPercent': "capitalExpenditurePercentage",
	'operatingCFPercent': "operatingCashFlowPercentage",
	'postTaxCostDebt': "afterTaxCostOfDebt",
	'marketRiskPremium': "marketRiskPremium",
	'growthRateLT': "longTermGrowthRate",
	'costOfEquity': "costOfEquity",
	'WACC': "wacc",
	'cashTaxRate': "taxRateCash",
	'ebiat': "ebiat",
	'ufcf': "ufcf",
	'riskFreeRate': "riskFreeRate",
	'sumPvUfcf': "sumPvUfcf",
	'terminalValue': "terminalValue",
	'presentTerminalValue': "presentTerminalValue",
	'EV': "enterpriseValue",
	'equityValue': "equityValue",
	'equityValuePerShare': "equityValuePerShare",
	'freeCashFlowT1': "freeCashFlowT1",
	'costOfDebt': "costofDebt",
	'dep': "depreciation",
	'totalCash': "totalCash",
	'depPercent': "depreciationPercentage",
	'totalCashPercent': "totalCashPercentage"
    ### Advanced DCF ###
    ### Levered DCF ###
    ### Levered DCF ###
}

ratioMapping = {
    ### Key Metric Quarterly ###
    "symbol": "symbol",
    "date": "date",
    'year': "calendarYear",
    'period': "period",
    'revShare': "revenuePerShare",
    'NIShare': "netIncomePerShare",
    'OperaCFShare': "operatingCashFlowPerShare",
    'FCFShare': "freeCashFlowPerShare",
    'cashShare': "cashPerShare",
    'BVShare': "bookValuePerShare",
    'tangibleBVShare': "tangibleBookValuePerShare",
    'SHEquityShare': "shareholdersEquityPerShare",
    'interestDebtShare': "interestDebtPerShare",
    'MV': "marketCap",
    'EV': "enterpriseValue",
    'PE': "peRatio",
    'PS': "priceToSalesRatio",
    'PCF': "pocfratio",
    'PFCF': "pfcfRatio",
    'PB': "pbRatio",
    'PTB': "ptbRatio",
    'EVtoSales': "evToSales",
    'EVtoEBITDA': "enterpriseValueOverEBITDA",
    'EVtoOperaCF': "evToOperatingCashFlow",
    'EVtoFCF': "evToFreeCashFlow",
    'EarningYield': "earningsYield",
    'FCFYield': "freeCashFlowYield",
    'debtEquity': "debtToEquity",
    'debtAsset': "debtToAssets",
    'netDebtEBITDA': "netDebtToEBITDA",
    'CA': "currentRatio",
    'IntCoverage': "interestCoverage",
    'IncQuality': "incomeQuality",
    'dividendYield': "dividendYield",
    'payoutRatio': "payoutRatio",
    'AdmintoRevenue': "salesGeneralAndAdministrativeToRevenue",
    'research&developtoRevenue': "researchAndDdevelopementToRevenue",
    'intangibletoAsset': "intangiblesToTotalAssets",
    'CapExtoOperaCF': "capexToOperatingCashFlow",
    'CapExtoRevenue': "capexToRevenue",
    'CapExtoDepre': "capexToDepreciation",
    'stockComptoRevenue': "stockBasedCompensationToRevenue",
    'grahamNumber': "grahamNumber",
    'ROIC': "roic",
    'ROTangibleAsset': "returnOnTangibleAssets",
    'grahamNetNet': "grahamNetNet",
    'WC': "workingCapital",
    'tangibleAsset': "tangibleAssetValue",
    'netCurrentAsset': "netCurrentAssetValue",
    'investedCapital': "investedCapital",
    'avgReceivables': "averageReceivables",
    'avgPayables': "averagePayables",
    'avgInv': "averageInventory",
    'daysSalesOutstanding': "daysSalesOutstanding",
    'daysPayablesOutstanding': "daysPayablesOutstanding",
    'daysInv': "daysOfInventoryOnHand",
    'receivablesTurnover': "receivablesTurnover",
    'payablesTurnover': "payablesTurnover",
    'InvTurnover': "inventoryTurnover",
    'ROE': "roe",
    'CapExShare': "capexPerShare"
    ### Key Metric Quarterly ###
}

dividendMapping = {
    "date": "date",
    # "label": "label",
    # "divAdj": "adjDividend",
    # "div": "dividend",
    # "recordDate": "recordDate",
    # "paymentDate": "paymentDate",
    "reportDate": "报告时间",
    "divType": "分红类型",
    "shareAdd": "送股比例",
    "shareConvert": "转增比例",
    "div": "派息比例",
    # "payoutRatio": "股利支付率",
    "declarationDate": "declarationDate"
}

ratioTTMMapping = {
    ### Key Metric TTM ###
    
    ### Key Metric TTM ###
}

CFGrowthMapping = {

}

IncGrowthMapping = {

}

BSGrowthMapping = {

}

FinancialGrowthMapping = {

}