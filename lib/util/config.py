import configparser

class config(object):
    def __init__(self, path="config.ini"):
        self._config = configparser.RawConfigParser()
        self._config.read(path)

        # --- API ---
        self._api = self._config.get("APIKEY", "API", fallback=None)

        # --- Econ ---
        self._tax_rate              = self._config.getfloat("ECON", "tax_rate",              fallback=25.0)
        self._risk_free_rate        = self._config.getfloat("ECON", "risk_free_rate",        fallback=1.64)
        self._lowest_market_return  = self._config.getfloat("ECON", "lowest_market_return",  fallback=6.0)
        self._market_return_method  = self._config.get(     "ECON", "market_return_method",  fallback="historical")
        self._n_years               = self._config.getint(  "ECON", "n_years",               fallback=10)
        self._fixed_erp             = self._config.getfloat("ECON", "fixed_erp",             fallback=7.5)

        # --- Valuation ---
        self._wacc_approach             = self._config.getboolean("VALUATION", "wacc_approach",             fallback=True)
        self._valuation_method          = self._config.get(       "VALUATION", "valuation_method",          fallback="fcfe")
        self._growth_calc_method        = self._config.get(       "VALUATION", "growth_calc_method",        fallback="earning")
        self._growth_calc_horizon       = self._config.getint(    "VALUATION", "growth_calc_horizon",       fallback=5)
        self._valuation_horizon         = self._config.getint(    "VALUATION", "valuation_horizon",         fallback=5)
        self._valuation_stage           = self._config.get(       "VALUATION", "valuation_stage",           fallback="single")
        self._long_term_growth_default  = self._config.getboolean("VALUATION", "long_term_growth_default",  fallback=True)

    # --- API ---
    @property
    def api(self):
        return self._api

    # --- Econ ---
    @property
    def taxRate(self):
        return self._tax_rate

    @property
    def riskFreeRate(self):
        return self._risk_free_rate

    @property
    def lowestMarketReturn(self):
        return self._lowest_market_return

    @property
    def marketReturnMethod(self):
        return self._market_return_method

    @property
    def nYears(self):
        return self._n_years

    @property
    def fixedErp(self):
        return self._fixed_erp

    # --- Valuation ---
    @property
    def waccApproach(self):
        return self._wacc_approach

    @property
    def valuationMethod(self):
        return self._valuation_method

    @property
    def growthCalcMethod(self):
        return self._growth_calc_method

    @property
    def growthCalcHorizon(self):
        return self._growth_calc_horizon

    @property
    def valuationHorizon(self):
        return self._valuation_horizon

    @property
    def valuationStage(self):
        return self._valuation_stage

    @property
    def longTermGrowthDefault(self):
        return self._long_term_growth_default
