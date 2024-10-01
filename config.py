import configparser

class config(object):
    def __init__(self, config):
        self._config = configparser.RawConfigParser()
        self._config.read(config)

        self._api = self._config["APIKEY"]["API"]

        # self._advancedvaluationURL = self._config["VALUATIONURL"]["Advance"]
        # self._leveredvaluationURL = self._config["VALUATIONURL"]["Lever"]

    @property
    def api(self):
        return self._api