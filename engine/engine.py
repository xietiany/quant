import numpy as np
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta

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
        return equityWeight * return_on_equity + debtWeight * return_on_debt

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

    @classmethod
    def dateconverter(cls, date, period="annual"):
        if isinstance(date, str):
            format_string = "%Y-%m-%d"
            date = datetime.strptime(date, format_string)
        if period == "annual":
            return cls._get_year_end_date(date)
        elif period == "quarter":
            return cls._get_quarter_end_date(date)
        else:
            raise ValueError("Invalid period specified. Use 'annual' or 'quarter'.")

    @classmethod
    def _get_quarter_end_date(cls, input_date):
        """
        Converts a given date to the last day of its respective quarter.

        Args:
            input_date (datetime.date): The date to convert.

        Returns:
            datetime.date: The last day of the quarter for the given date.
        """
        # Determine the quarter start month based on the input date's month
        quarter_start_month = ((input_date.month - 1) // 3) * 3 + 1

        # Calculate the first day of the quarter
        first_day_of_quarter = date(input_date.year, quarter_start_month, 1)

        # Add 3 months and subtract 1 day to get the last day of the quarter
        last_day_of_quarter = first_day_of_quarter + relativedelta(months=3) - relativedelta(days=1)

        return last_day_of_quarter
    
    @classmethod
    def _get_year_end_date(cls, input_date):
        """
        Converts a given date to the last day of its respective year.

        Args:
            input_date (datetime.date): The date to convert.

        Returns:
            datetime.date: The last day of the year for the given date.
        """
        return date(input_date.year, 12, 31)

    @classmethod
    def compDateConverter(cls, date, n, period="annual"):
        """
        Converts a given date to the last day of the previous Nth year or quarter.

        Args:
            date (datetime.date): The date to convert.
            period (str): The period type, either "annual" or "quarter".

        Returns:
            datetime.date: The last day of the previous Nth year or quarter.
        """
        if isinstance(date, str):
            format_string = "%Y-%m-%d"
            date = datetime.strptime(date, format_string)
        if period == "annual":
            return cls.get_last_day_of_previous_nth_year(date, n)
        elif period == "quarter":
            return cls.get_last_day_of_previous_nth_quarter(date, n*4)
        else:
            raise ValueError("Invalid period specified. Use 'annual' or 'quarter'.")

    @classmethod
    def get_last_day_of_previous_nth_year(cls, input_date, n):
        """
        Calculates the last day of the previous Nth year from the current date.

        Args:
            n (int): The number of years to go back.

        Returns:
            date: The last day of the previous Nth year.
        """
        # Calculate the year of the previous Nth year
        target_year = input_date.year - n
        # Create a date object for the last day of that target year
        
        last_day = date(target_year, 12, 31)
        return last_day

    @classmethod
    def get_last_day_of_previous_nth_quarter(cls, input_date: date, n: int) -> date:
        """
        Calculates the last day of the previous Nth quarter relative to a reference date.

        Args:
            input_date: The reference date.
            n: The number of quarters to go back (e.g., 1 for the immediate previous quarter).

        Returns:
            The last day of the previous Nth quarter.
        """
        # Determine the first month of the current quarter
        current_quarter_first_month = ((input_date.month - 1) // 3) * 3 + 1

        # Calculate the target quarter's year and month
        target_month = current_quarter_first_month - (n * 3)
        target_year = input_date.year

        while target_month <= 0:
            target_month += 12
            target_year -= 1

        # Get the first day of the target quarter
        first_day_of_target_quarter = date(target_year, target_month, 1)

        # Get the first day of the quarter after the target quarter
        # This is the same as adding 3 months to the target quarter's first day
        next_quarter_first_month = target_month + 3
        next_quarter_year = target_year
        if next_quarter_first_month > 12:
            next_quarter_first_month -= 12
            next_quarter_year += 1
        
        first_day_of_next_quarter = date(next_quarter_year, next_quarter_first_month, 1)

        # The last day of the target quarter is one day before the first day of the next quarter
        last_day_of_target_quarter = first_day_of_next_quarter - timedelta(days=1)

        return last_day_of_target_quarter

    @classmethod
    def defaultDate(cls, period="annual"):
        """
        Returns the default date for the specified period type.

        Args:
            period (str): The period type, either "annual" or "quarter".

        Returns:
            datetime.date: The default date for the specified period.
        """
        current_date = date.today()
        if period == "annual":
            last_year = current_date.year - 1
            return date(last_year, 12, 31)
        elif period == "quarter":
            current_quarter_start_month = (current_date.month - 1) // 3 * 3 + 1
            first_day_current_quarter = date(current_date.year, current_quarter_start_month, 1)

            # Subtract one day from the first day of the current quarter to get the last day of the previous quarter
            last_day_last_quarter = first_day_current_quarter - relativedelta(days=1)

            return last_day_last_quarter
        else:
            raise ValueError("Invalid period specified. Use 'annual' or 'quarter'.")

    @classmethod
    def get_last_day_of_quarters(cls, input_date, num_quarters=3):
        """
        Returns a list of dates representing the last day of the current day's equivalent
        in the last 'num_quarters' completed quarters.
        """
        last_days = []

        for i in range(1, num_quarters + 1):
            # Calculate the start of the quarter 'i' quarters ago
            # First, go back to the first day of the current quarter
            current_quarter_start = date(input_date.year, (input_date.month - 1) // 3 * 3 + 1, 1)
            
            # Then, subtract 'i' quarters from that start date
            target_quarter_start = current_quarter_start - relativedelta(months=3 * i)
            
            # Find the last day of that target quarter
            # This is the day before the start of the next quarter
            next_quarter_start = target_quarter_start + relativedelta(months=3)
            last_day_of_quarter = next_quarter_start - relativedelta(days=1)
            
            last_days.append(last_day_of_quarter)
            
        return last_days
