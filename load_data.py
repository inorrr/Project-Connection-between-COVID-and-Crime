"""
CSC110 FINAL PROJECT - The connection between COVID-19 and Crime
Load data Functions
Author:  Yinuo Zhao

This files contains the two function needed to load the datasets to the objects we created.
"""

import csv
from data_class import CrimeData, CovidData


def load_crime_data(filename: str) -> list[CrimeData]:
    """
    This function loads the data in the file to a list of CrimeData object
    """
    data_so_far = []
    with open(filename) as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)  # SKIP THE HEADER
        for row in reader:
            if row[11] == '':
                data_so_far.append(CrimeData(year=int(row[0].split('-')[0]),
                                             month=int(row[0].split('-')[1]),
                                             area=row[1],
                                             type=row[3],
                                             number=0))
            else:
                data_so_far.append(CrimeData(year=int(row[0].split('-')[0]),
                                             month=int(row[0].split('-')[1]),
                                             area=row[1],
                                             type=row[3],
                                             number=int(row[11])))
    return data_so_far


def load_covid_data(filename: str) -> list[CovidData]:
    """
    This function loads the data in the file to a list of CovidData object
    """
    data_so_far = []
    with open(filename) as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)  # SKIP THE HEADER
        for row in reader:
            data_so_far.append(CovidData(year=int(row[3].split('-')[0]),
                                         month=int(row[3].split('-')[1]),
                                         day=int(row[3].split('-')[2]),
                                         province=row[1],
                                         total_case=int(row[8]),
                                         daily_case=int(row[15])))
    return data_so_far


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'csv', 'data_class'],
        'allowed-io': ['load_crime_data', 'load_covid_data'],
        'max-line-length': 120,
        'disable': []
    })

    import python_ta.contracts
    python_ta.contracts.check_all_contracts()

    import doctest
    doctest.testmod()
