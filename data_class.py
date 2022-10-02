"""
CSC110 FINAL PROJECT - The connection between COVID-19 and Crime
Data Classes
Author: Yinuo Zhao

This files contains the two data classes needed for this program.
"""

from dataclasses import dataclass


@dataclass
class CrimeData:
    """
    A custom data type that represents data for crime cases of a specific area, type, and time(year and  month)

    Instance Attributes:
        - year: the year of this line of data
        - month: the month of this line of data
        - area: the area of which this line of data is recorded in
        - type: type of the crime
        - number: number of cases

    Representation Invariants:
        - self.year > 0
        - self.month >0
        - len(self.area) >= 0
        - len(self.type) >= 0
        - self.number >= 0

    >>> crimedata = CrimeData(year=2019, month=3, area='', type='', number=0)
    >>> crimedata
    CrimeData(year=2019, month=3, area='', type='', number=0)
    """
    year: int
    month: int
    area: str
    type: str
    number: int


@dataclass
class CovidData:
    """
    A custom data type that represents data for COVID cases of a specific province, and time(year month day)

    Instance Attributes:
        - year: The year of this data
        - month: The month of this data
        - day: The day of this data
        - province: Name of the province
        - total_case: Number of total cases (confirmed + probable),Number of confirmed cases in
                    each P/T (Canada= sum of all P/Ts)
        - daily_case: Number of new cases since last update,Number of total counts from last update
                    subtracted from total counts of current update

    Representation Invariants:
        - 2019 <= self.year <= 2021
        - 1 <= self.month <= 12
        - 1 <= self.day <= 31
        - len(self.province) > 0
        - self.total_case > 0
        - self.daily_case > 0
        - self.daily_case <= self.total_case

    >>> covid_data = CovidData(year=2019, month=3, day=25, province='Ontario', total_case=25, daily_case=10)
    >>> covid_data
    CovidData(year=2019, month=3, day=25, province='Ontario', total_case=25, daily_case=10)

    """
    year: int
    month: int
    day: int
    province: str
    total_case: int
    daily_case: int


if __name__ == '__main__':

    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts'],
        'allowed-io': [],
        'max-line-length': 120,
        'disable': []
    })

    import python_ta.contracts
    python_ta.contracts.check_all_contracts()

    import doctest
    doctest.testmod()
