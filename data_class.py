"""
This file creates a new data class
"""

from dataclasses import dataclass


@dataclass
class CrimeData:
    """ data of crime.

    Instance Attributes:
        - year: the year of this line of data
        - month: the month of this line of data
        - area:
        - type: type of the crime
        - number: number of cases

    Representation Invariants:

    """
    year: int
    month: int
    area: str
    type: str
    number: int


@dataclass
class CovidData:
    """
    data of covid cases by area and time

    Instance Attributes:
        - year:
        - month:
        - day:
        - province: name of the province
        - total_case: Number of total cases (confirmed + probable),Number of confirmed cases in
                    each P/T (Canada= sum of all P/Ts)
        - daily_case: Number of new cases since last update,Number of total counts from last update
                    subtracted from total counts of current update

    Representation Invariants:

    """
    year: int
    month: int
    day: int
    province: str
    total_case: int
    daily_case: int




