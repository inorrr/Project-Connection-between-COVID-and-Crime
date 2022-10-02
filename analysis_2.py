"""
CSC110 FINAL PROJECT - The connection between COVID-19 and Crime
Analysis 2: compare the level of influence of covid-19 on different types of crimes

Author: Xiangxuan Kong

This file contains the functions necessary for data wrangling and creating the plot.
"""
import datetime
import plotly.graph_objects as plt
import load_data
from data_class import CrimeData, CovidData
CRIME_DATA = load_data.load_crime_data('crime.csv')
COVID_DATA = load_data.load_covid_data('covid.csv')


# part 1: check
def fix(covid: list[CovidData]) -> None:
    """
    make every national cases equal to the sum of provincial cases at each time

    Preconditions:
        - covid != []

    >>> ccovid = [CovidData(year = 1, month = 2, day = 3, province = 'Canada', total_case= 10,\
                           daily_case = 3),\
                 CovidData(year = 1, month = 2, day = 3,\
                           province = 'Ontario', total_case= 5, daily_case = 2),\
                 CovidData(year = 1, month = 2, day = 3,\
                           province = 'Quebec', total_case= 4, daily_case = 1)]
    >>> fix(ccovid)
    >>> ccovid == [CovidData(year = 1, month = 2, day = 3, province = 'Canada', total_case= 9,\
                            daily_case = 3),\
                  CovidData(year = 1, month = 2, day = 3, province = 'Ontario', total_case= 5,\
                            daily_case = 2),\
                  CovidData(year = 1, month = 2, day = 3, province = 'Quebec', total_case= 4,\
                            daily_case = 1)]
    True
    """
    # find all the data at the time
    # check if the total case equals the sum of provincial cases
    for i in range(len(covid)):
        if covid[i].province == 'Canada':
            fix_helper(i, covid)


def fix_helper(i: int, covid: list[CovidData]) -> None:
    """
    make the total_cases attribute of covid[i] equal the sum of provincial total cases
    and the daily_cases attribute of covid[i] equal the sum of provincial daily cases
    on the same day

    Precondition:
        - covid[i].province = 'Canada'
    """
    sum_total = 0
    sum_daily = 0
    for y in covid:
        if all([y.year == covid[i].year, y.month == covid[i].month, y.day == covid[i].day,
                y.province != 'Canada']):
            sum_total = sum_total + y.total_case
            sum_daily = sum_daily + y.daily_case
    covid[i] = CovidData(year=covid[i].year,
                         month=covid[i].month,
                         day=covid[i].day,
                         province=covid[i].province,
                         total_case=sum_total,
                         daily_case=sum_daily)


def check_helper(i: int, covid: list[CovidData]) -> tuple:
    """
    Return the tuple containing the sum of provincial total cases and the national sum of daily cases
    on the same day as covid[i]

    Precondition:
        - covid[i].province == 'Canada'

    >>> cvid = [CovidData(year = 1, month = 2, day = 3, province = 'Canada', total_case= 9, \
                           daily_case = 3), \
                 CovidData(year = 1, month = 2, day = 3, province = 'Ontario', total_case= 5, \
                           daily_case = 2), \
                 CovidData(year = 1, month = 2, day = 3, province = 'Quebec', \
                           total_case= 4, daily_case = 1)]
    >>> check_helper(0, cvid)
    (9, 3)
    """
    sum_total = 0
    sum_daily = 0
    for y in covid:
        if all([y.year == covid[i].year, y.month == covid[i].month, y.day == covid[i].day,
                y.province != 'Canada']):
            sum_total = sum_total + y.total_case
            sum_daily = sum_daily + y.daily_case
    return (sum_total, sum_daily)


def check(covid: list[CovidData]) -> str:
    """
    check if every national cases equal to the sum of provincial cases at each time

    Preconditions:
        - covid != []

    >>> cvid = [CovidData(year = 1, month = 2, day = 3, province = 'Canada', total_case= 9, \
                           daily_case = 3), \
                 CovidData(year = 1, month = 2, day = 3, province = 'Ontario', total_case= 5, \
                           daily_case = 2), \
                 CovidData(year = 1, month = 2, day = 3, province = 'Quebec', \
                           total_case= 4, daily_case = 1)]
    >>> check(cvid)
    'nothing wrong'
    """
    # find all the data at the time
    # check if the total case equals the sum of provincial cases
    for i in range(len(covid)):
        if covid[i].province == 'Canada' and (covid[i].total_case != check_helper(i, covid)[0]
                                              or covid[i].daily_case != check_helper(i, covid)[1]):
            return 'please fix the data at ' + str(covid[i].day) + 'th in'
    return 'nothing wrong'


fix(COVID_DATA)


# part 2: categorize
# categorize the areas and crimes

def possible_crime(crime: list[CrimeData]) -> set[str]:
    """
    return a set of possible crimes in the list by excluding the services

    Preconditions:
        - crime != []

    >>> c = [CrimeData(year = 2020, month = 2, area = 'Toronto', type = 'Robbery', number = 10),\
             CrimeData(year = 2020, month = 2, area = 'Montreal', type = 'Assault', number = 7),\
             CrimeData(year = 2020, month = 2, area = 'Markham', type = 'threat', number = 3)]
    >>> possible_crime(c) == {'Robbery', 'Assault','threat'}
    True
    """
    all_crimes = set()
    for x in crime:
        if 'service' not in x.type:
            all_crimes.add(x.type)
    return all_crimes


# Excluding the services in types and there are 26 types of crimes in crime data
# and the categories that
# {'Fail to comply with order [3410]'
# 'Motor vehicle theft [2135]', 'Shoplifting [213]', 'Fraud/identity theft/identity fraud [216]',
# 'Total robbery [160]',
# 'Uttering threats [1627]', 'Total breaking and entering [210]',
# 'Total sexual assaults (levels 1, 2, 3) [131]',
# 'Dangerous operation, causing death or bodily harm [911]',
# 'Provincial/Territorial acts related to COVID-19',
# 'Impaired driving, operating while impaired [923]',
# 'Impaired driving, causing death or bodily harm [921]',
# 'Total assaults (levels 1, 2, 3) [141]'}

# we categorize the data into sets
VIOLENCE = {'Total sexual assaults (levels 1, 2, 3) [131]', 'Total assaults (levels 1, 2, 3) [141]',
            'Total breaking and entering [210]', 'Total robbery [160]',
            'Dangerous operation, causing death or bodily harm [911]',
            'Impaired driving, causing death or bodily harm [921]'}
TRAFFIC = {'Impaired driving, operating while impaired [923]',
           'Impaired driving, causing death or bodily harm [921]'}
THREAT_FRAUD = {'Uttering threats [1627]', 'Fraud/identity theft/identity fraud [216]'}
PROPERTY_RELATED = {'Total robbery [160]', 'Motor vehicle theft [2135]', 'Shoplifting [213]',
                    'Total breaking and entering [210]'}
TYPES_LIST = [VIOLENCE, TRAFFIC, THREAT_FRAUD, PROPERTY_RELATED]

# put them in a map
CRIME_MAP = {'violence': VIOLENCE,
             'traffic': TRAFFIC, 'threat or fraud': THREAT_FRAUD,
             'property related': PROPERTY_RELATED}


def possible_area_crime(crime: list[CrimeData]) -> set[str]:
    """
    return a set of all areas in the crime

    Preconditions:
        - crime != []

    >>> cr = [CrimeData(year = 2020, month = 2, area = 'Toronto', type = 'Robbery', number = 10),\
              CrimeData(year = 2020, month = 2, area = 'Montreal', type = 'Assault', number = 7),\
              CrimeData(year = 2020, month = 2, area = 'Markham', type = 'threat', number = 3)]
    >>> possible_area_crime(cr) == {'Toronto', 'Montreal', 'Markham'}
    True
    """
    area_crime = set()
    for x in crime:
        area_crime.add(x.area)
    return area_crime


# there are 20 areas in the crime data
# {'Royal Newfoundland Constabulary [10C01]', 'Toronto, Ontario, municipal [35304]',
# 'Vancouver, British Columbia, municipal [59023]', 'Saskatoon, Saskatchewan, municipal [47066]',
# 'Winnipeg, Manitoba, municipal [46064]', 'Victoria, British Columbia, municipal [59025]',
# 'Calgary, Alberta, municipal [48014]', 'Edmonton, Alberta, municipal [48033]',
# 'London, Ontario, municipal [35162]', 'Montréal, Quebec, municipal [24175]',
# 'Kennebecasis Region, New Brunswick, municipal [13024]', 'Regina, Saskatchewan, municipal [47063]',
# 'York Region, Ontario, municipal [35335]', 'Quebec Provincial Police [24C01]',
# 'Ontario Provincial Police [35C01]', 'Waterloo Region (Kitchener), Ontario, municipal [35291]',
# 'Total, Selected police services', 'Ottawa, Ontario, municipal [35010]',
# 'Halton Region (Oakville/Burlington), Ontario, municipal [35048]',
# 'Royal Canadian Mounted Police [99C01]'}

# they are categorized by the province
ON = {'Toronto, Ontario, municipal [35304]', 'London, Ontario, municipal [35162]',
      'York Region, Ontario, municipal [35335]',
      'Waterloo Region (Kitchener), Ontario, municipal [35291]'
      'Ottawa, Ontario, municipal [35010]'
      'Halton Region (Oakville/Burlington), Ontario, municipal [35048]'}
BC = {'Vancouver, British Columbia, municipal [59023]',
      'Victoria, British Columbia, municipal [59025]'}
MB = {'Winnipeg, Manitoba, municipal [46064]'}
QC = {'Montréal, Quebec, municipal [24175]', }
NB = {'Kennebecasis Region, New Brunswick, municipal [13024]', }
SK = {'Saskatoon, Saskatchewan, municipal [47066]', 'Regina, Saskatchewan, municipal [47063]',
      'Regina, Saskatchewan, municipal [47063]'}
AB = {'Calgary, Alberta, municipal[48014]', 'Edmonton, Alberta, municipal [48033]', }
NL = {'Royal Newfoundland Constabulary [10C01]'}
CA = {'Total, Selected police services'}


def possible_area_covid(covid: list[CovidData]) -> set[str]:
    """
    return a set of all possible areas in the covid

    Precondition:
        - covid != []

    >>> cov = [CovidData(year = 2020, month = 2, day = 3, province = 'Ontario',\
                         daily_case = 10, total_case= 10),\
               CovidData(year = 2020, month = 2, day = 3, province = 'British Columbia',\
                         daily_case = 7, total_case = 10),\
               CovidData(year = 2020, month = 2, day = 3, province = 'Quebec',\
                         daily_case = 3, total_case = 10)]
    >>> possible_area_covid(cov) == {'Ontario', 'British Columbia', 'Quebec'}
    True
    """
    area = set()
    for x in covid:
        area.add(x.province)
    return area


# Existing object.provinces for object in covid data:
# {'New Brunswick', 'Canada', 'Newfoundland and Labrador', 'Nova Scotia', 'Ontario', 'British Columbia',
# 'Prince Edward Island', 'Nunavut', 'Yukon', 'Repatriated travellers', 'Alberta', 'Manitoba',
# 'Northwest Territories',
# 'Saskatchewan', 'Quebec'}

# we put the provinces that are involved in crime.csv and covid.csv
AREA_MAP = {'Ontario': ON, 'British Columbia': BC, 'Alberta': AB, 'Manitoba': MB,
            'Saskatchewan': SK, 'Newfoundland and Labrador': NL, 'New Brunswick': NB,
            'Quebec': QC, 'Canada': CA}

# part3 preparation
# put the independent variable time in a list.
# a function that return a list of number of specified type of crimes
# in each month of a specified province
# a function that return the number of total cases of each month for each province
# check the length of the x-data and y-data so that plotting is possible


# The crime data has data from 2019-03 to 2021-08
# The covid data has data from  2020-01-31 to 2021-11-01
# so the data from 2020-02-01 to 2021-08-01 can be compared

TIME = []
for M in range(2, 13):
    TIME.append(datetime.datetime(year=2020, month=M, day=1))
for M in range(1, 9):
    TIME.append(datetime.datetime(year=2021, month=M, day=1))


def get_nums(category: set, province: str) -> list[int]:
    """
    return a list of monthly numbers of the given type of crimes of the given province

    Preconditions:
        - category != set()
        - province in area_map
    """
    nums = []
    for month in TIME:
        total = 0
        for unit in CRIME_DATA:
            if unit.year == month.year and unit.month == month.month and \
                    unit.area in AREA_MAP[province] and unit.type in category:
                total += unit.number
        nums.append(total)
    return nums


def get_cases(province: str) -> list[int]:
    """
    return the number of total cases of each month for each province

    Precondition:
        - province in area_map
    """
    cases = []
    for month in TIME:
        month_cases = 0
        for unit in COVID_DATA:
            if unit.year == month.year and unit.month == month.month and unit.province == province:
                month_cases += unit.daily_case
        cases.append(month_cases)
    return cases


def check_length_crime() -> bool:
    """
    check if the length of the list of numbers of each type of crime equals the length of date

    Preconditions:

    """
    return all(len(get_nums(category, province)) == 19 for province in AREA_MAP
               for category in TYPES_LIST)


def check_length_cases() -> bool:
    """
    check if the length of the list of cases equals the length of date

    Preconditions:

    """
    return all(len(get_cases(province)) == 19 for province in AREA_MAP)


# part 4 plots
# a function that plot all the graphs
# for each area (a province or the whole country)
#  date(month) vs 4 types
#  date(month) vs total cases (sum of daily cases of the month)

def plot_together(province: str) -> None:
    """
    plot
    the line chart of a The Number of Each Type of Crimes in the specified province versus time
    and the line chart of the Monthly COVID-19 Cases in the specified province versus time
    together

    Preconditions:
        - province in area_map
        - len(get_cases(province)) == len(time)
        - all(len(get_nums(cate, province)) == len(time) for cate in type_list)

    """
    fig = plt.Figure()

    for typ in CRIME_MAP:
        fig.add_trace(plt.Scatter(
            x=TIME,
            y=get_nums(CRIME_MAP[typ], province),
            name=typ,
        )
        )

    fig.add_trace(plt.Scatter(
        x=TIME,
        y=get_cases(province),
        name='COVID-19 cases',
        yaxis='y2'
    )
    )

    fig.update_layout(
        xaxis=dict(
            title='Time'
        ),
        yaxis=dict(
            title="Number of Crimes"
        ),
        yaxis2=dict(
            title="Cases",
            titlefont=dict(
                color="#ff7f0e"
            ),
            tickfont=dict(
                color="#ff7f0e"
            ),
            anchor="x",
            overlaying="y",
            side="right"),
        title={'text': 'The Number of Each Type of Crimes and Monthly COVID-19 Cases in '
                       + province + ' versus Time', 'x': 0.5}
    )
    fig.show()


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'plotly.graph_objects', 'datetime',
                          'load_data', 'data_class'],
        'allowed-io': [],
        'max-line-length': 120,
        'disable': []
    })

    import python_ta.contracts

    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod()
