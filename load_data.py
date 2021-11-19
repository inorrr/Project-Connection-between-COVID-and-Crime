"""
This file loads the data to a list of object
"""

import csv
from data_class import CrimeData, CovidData


def load_crime_data(filename: str) -> list[CrimeData]:
    """
    this function loads the data in the file to a list of CrimeData object
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

def riya_s_function() ->None:
    for i in range(0, length_of_the_file, 5):
        dict[file_line_i] = file_line_i+1

def load_covid_data(filename: str) -> list[CovidData]:
    """
    this function loads the data in the file to a list of CovidData object
    """
    data_so_far = []
    with open(filename) as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)
        for row in reader:
            data_so_far.append(CovidData(year=int(row[3].split('-')[0]),
                                         month=int(row[3].split('-')[1]),
                                         day=int(row[3].split('-')[2]),
                                         province=row[1],
                                         total_case=int(row[8]),
                                         daily_case=int(row[15])))
    return data_so_far
