import numpy as np
import pandas as pd
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta, TH

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
    def singleStage(cls, starting, LTGrowth, RR):
        divider = ((RR - LTGrowth) / 100)
        if RR - LTGrowth <= 0:
            print("RR needs to be greater than LTGrowth")
        return starting * (1 + LTGrowth / 100) / divider

    @classmethod
    def TwoStage(cls, starting, firststageGrowth, firststagePeriod, LTGrowth, RR):
        cashflowlist, firststageending = cls.cashflow(starting, firststageGrowth, RR, firststagePeriod)
        terminalValue = cls.earning(firststageending, LTGrowth, RR)
        return terminalValue + sum(cashflowlist)

    @classmethod
    def ThreeStage(cls, starting, firststageGrowth, firststagePeriod, secondstageGrowth, secondstagePeriod, LTGrowth, RR):
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
            date = datetime.strptime(date, format_string).date()
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
            date = datetime.strptime(date, format_string).date()
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
    def get_last_day_of_previous_year(cls, input_date):
        """
        Calculates the last day of the previous year from the current date.

        Args:
            input_date (datetime.date): The reference date.

        Returns:
            datetime.date: The last day of the previous year.
        """
        if isinstance(input_date, str):
            format_string = "%Y-%m-%d"
            input_date = datetime.strptime(input_date, format_string).date()
        last_year = input_date.year - 1
        return date(last_year, 12, 31)

    @classmethod
    def get_default_last_day_of_previous_year(cls):
        """
        Calculates the last day of the previous year from today's date.

        Returns:
            datetime.date: The last day of the previous year.
        """
        today = date.today()
        last_year = today.year - 1
        return date(last_year, 12, 31)

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

    @classmethod
    def get_last_year_range(cls, input_date):
        """
        Returns the start and end dates of the last year based on the input date.
        """
        if isinstance(input_date, str):
            format_string = "%Y-%m-%d"
            input_date = datetime.strptime(input_date, format_string).date()
        last_year = input_date.year - 1
        start_date = date(last_year, 1, 1)
        end_date = date(last_year, 12, 31)

        return start_date, end_date

    @classmethod
    def get_date_range_from_date(cls, input_date, years=1):
        """
        Returns the start and end dates of a range ending on the input date and spanning the specified number of years.
        """
        if isinstance(input_date, str):
            format_string = "%Y-%m-%d"
            input_date = datetime.strptime(input_date, format_string).date()
        end_date = input_date
        start_date = date(end_date.year - years, end_date.month, end_date.day)

        return start_date, end_date

    @classmethod
    def get_dates_ends(cls, start_date, end_date, period="quarter"):
        """
        Generates a list of the last day of each quarter within a given date range.

        Args:
            start_date (str or datetime-like): The start date of the range.
            end_date (str or datetime-like): The end date of the range.

        Returns:
            list: A list of datetime objects representing the last day of each quarter.
        """
        # Create a PeriodIndex with 'Q-DEC' frequency for quarter-end (December)
        # This automatically aligns to the end of each quarter (March, June, Sept, Dec)
        if period == "annual":
            start_date = cls.dateconverter(start_date, period="annual")
            end_date = cls.dateconverter(end_date, period="annual")
            year_periods = pd.period_range(start=start_date, end=end_date, freq='A-DEC')
            year_ends = [period.end_time.date() for period in year_periods]
            return year_ends
        elif period == "quarter":
            quarter_periods = pd.period_range(start=start_date, end=end_date, freq='Q-DEC')

            # Convert each Period object to its end date (Timestamp)
            quarter_ends = [period.end_time.date() for period in quarter_periods]

            return quarter_ends

    @classmethod
    def get_last_day_of_next_quarter(cls, input_date):
        """
        Calculates the last day of the next calendar quarter from a given date.

        Args:
            input_date (date): The starting date.

        Returns:
            date: The last day of the next quarter.
        """
        # Determine the start of the current quarter
        current_quarter_start_month = ((input_date.month - 1) // 3) * 3 + 1
        current_quarter_start = date(input_date.year, current_quarter_start_month, 1)

        # Add 3 months to get to the start of the next quarter
        next_quarter_start = current_quarter_start + relativedelta(months=3)

        # Add 3 more months to get to the start of the quarter after the next,
        # then subtract one day to get the last day of the next quarter.
        last_day_of_next_quarter = next_quarter_start + relativedelta(months=3, days=-1)

        return last_day_of_next_quarter

    @classmethod
    def get_last_day_of_next_year(cls, input_date):
        """
        Calculates the last day of the next calendar year from a given date.

        Args:
            input_date (date): The starting date.

        Returns:
            date: The last day of the next year.
        """
        next_year = input_date.year + 1
        return date(next_year, 12, 31)
