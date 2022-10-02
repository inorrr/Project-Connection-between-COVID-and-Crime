"""
CSC110 FINAL PROJECT - The connection between COVID-19 and Crime
Analysis 3: COVID-19 Policies effect on Crime

Author:  Allen Xu

This file contains the functions necessary for data wrangling and creating the plot.
"""

import matplotlib.pyplot as plt
import load_data
CRIME_DATA = load_data.load_crime_data("crime.csv")


def total_crime(year: int, month: int) -> int:
    """  returns the total monthly crime occurrences for the given month in
    the given year as an integer

    Preconditions:
        - year in [2019,2020,2021]
        - 1 <= month <= 12
    """
    sum_crime = 0
    for x in CRIME_DATA:
        if x.year == year and x.month == month:
            sum_crime += x.number
    return sum_crime


def prior(year: int, month: int) -> list:
    """ returns a list of the individual total monthly crime occurrences
    for 4 months prior to the given month and year, with the first element
    being the month directly before the given month and year

    Preconditions:
        - 2019 <= year <= 2021
        - 1 <= month <= 12

    >>> year = 2020
    >>> month = 8
    >>> prior(year, month)
    [265908, 243126, 226814, 217372]

    """
    lst = []
    for x in range(1, 5):
        if (month - x) >= 1:
            lst.append(total_crime(year, month - x))
        else:
            lst.append(total_crime(year - 1, (month - x) + 12))

    return lst


def after(year: int, month: int) -> list:
    """
    returns a list of the individual total monthly crime occurrences for
    4 months after the given month and year

    Preconditions:
        - 2019 <= month <= 2021
        - 1 <= x.month <= 12

    >>> year = 2020
    >>> month = 8
    >>> after(year, month)
    [242552, 238068, 221172, 216518]
    """
    lst = []
    for x in range(1, 5):
        if (month + x) <= 12:
            lst.append(total_crime(year, month + x))
        else:
            lst.append(total_crime(year + 1, (month + x) % 12))

    return lst


def monthly_crime(year: int, month: int) -> list:
    """
    returns a list of the individual total crime for each month
    in an 9 month interval centered at the given month and year

    Preconditions
        - 2019 <= year <= 2021
        - 1 <= month <= 12

    >>> year = 2020
    >>> month = 8
    >>> monthly_crime(year, month)
    [217372, 226814, 243126, 265908, 255700, 242552, 238068, 221172, 216518]
    """
    interval = [total_crime(year, month)]
    prior_months = prior(year, month)
    after_months = after(year, month)

    for x in prior_months:
        interval.insert(0, x)

    for x in after_months:
        interval.append(x)

    return interval


def month_interval(year: int, month: int) -> list[tuple[int, int]]:
    """
    returns a list of a 9 month interval centered at
    the given month and year

    Preconditions:
        - 2019 <= year <= 2021
        - 1 <= month <= 12

    >>> year = 2020
    >>> month = 8
    >>> month_interval(year, month)
    [(2020, 4), (2020, 5), (2020, 6), (2020, 7), (2020, 8), (2020, 9), \
    (2020, 10),(2020, 11), (2020, 12)]
    """
    lst = [(year, month)]

    for x in range(1, 5):
        if month - x >= 1:
            lst.insert(0, (year, month - x))
        else:
            lst.insert(0, (year - 1, month - x + 12))

    for x in range(1, 5):
        if month + x <= 12:
            lst.append((year, month + x))
        else:
            lst.append((year + 1, (month + x) % 12))

    return lst


def convert_months(yearmonth: tuple[int, int]) -> str:

    """ returns the given month and year as its corresponding
    abbreviation as a string

    Preconditions:
        - 2019 <= yearmonth[0] <= 2021
        - 1 <= yearmonth[1] <= 12

    >>> yearmonth = (2021,1)
    >>> convert_months(yearmonth)
    'Jan21'
    """
    month_dict = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
                  7: 'Jul', 8: 'Aug', 9: 'Spt', 10: 'Oct', 11: 'Nov', 12: 'Dec'}

    str_year = str(yearmonth[0])

    return month_dict[yearmonth[1]] + str_year[2:4]


def final_plot() -> plt.Figure:
    """ plots final graphs """

    # retrieving the individual monthly crime total for each time interval centered
    # at the policy implementation date

    # CRB implementation date and data centered at this date
    time1 = (2020, 3)
    interval1 = [convert_months(x) for x in month_interval(time1[0], time1[1])]
    crime1 = monthly_crime(time1[0], time1[1])

    # The date Canada secures 20 million Vaccine doses and the data centered at this date
    time2 = (2021, 1)
    interval2 = [convert_months(x) for x in month_interval(time2[0], time2[1])]
    crime2 = monthly_crime(time2[0], time2[1])

    # Travel Restrictions extension date announced and data centered at this date
    time3 = (2020, 11)
    interval3 = [convert_months(x) for x in month_interval(time3[0], time3[1])]
    crime3 = monthly_crime(time3[0], time3[1])

    # Recent Lockdown date and data centered at this date
    time4 = (2021, 4)
    interval4 = [convert_months(x) for x in month_interval(time4[0], time4[1])]
    crime4 = monthly_crime(time4[0], time4[1])

    figure, axis = plt.subplots(2, 2, constrained_layout=True)
    plt.suptitle('Effect Covid Policies has on Crime')

    # Plots Subsidy graph
    axis[0, 0].plot(interval1, crime1)
    axis[0, 0].set_title('Subsidy')
    axis[0, 0].set_xlabel('Month')
    axis[0, 0].set_ylabel('Total Crime')
    axis[0, 0].tick_params(axis='x', rotation=45)
    axis[0, 0].axvline(x=interval1[4], linestyle='--')
    axis[0, 0].grid()

    # Plots Vaccine graph
    axis[0, 1].plot(interval2, crime2)
    axis[0, 1].set_title('Vaccine')
    axis[0, 1].set_xlabel('Month')
    axis[0, 1].set_ylabel('Total Crime')
    axis[0, 1].tick_params(axis='x', rotation=45)
    axis[0, 1].axvline(x=interval2[4], linestyle='--')
    axis[0, 1].grid()

    # Plots Travel Restriction graph
    axis[1, 0].plot(interval3, crime3)
    axis[1, 0].set_title('Travel Restrictions')
    axis[1, 0].set_xlabel('Month')
    axis[1, 0].set_ylabel('Total Crime')
    axis[1, 0].tick_params(axis='x', rotation=45)
    axis[1, 0].axvline(x=interval3[4], linestyle='--')
    axis[1, 0].grid()

    # Plots Lockdown graph
    axis[1, 1].plot(interval4, crime4)
    axis[1, 1].set_title('Lockdown')
    axis[1, 1].set_xlabel('Month')
    axis[1, 1].set_ylabel('Total Crime')
    axis[1, 1].tick_params(axis='x', rotation=45)
    axis[1, 1].axvline(x=interval4[4], linestyle='--')
    axis[1, 1].grid()

    figure.canvas.set_window_title('CSC110 Final Project - Connection between COVID-19 and Crime - Analysis 3')

    return figure


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'matplotlib.pyplot',
                          'load_data', 'data_class'],
        'allowed-io': [],
        'max-line-length': 120,
        'disable': []
    })

    import python_ta.contracts
    python_ta.contracts.check_all_contracts()

    import doctest
    doctest.testmod()
