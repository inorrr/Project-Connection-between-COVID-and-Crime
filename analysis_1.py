"""
CSC110 FINAL PROJECT - The connection between COVID-19 and Crime
Analysis 1 : The number of crime cases by type and area of any specific month.

Author:  Yinuo Zhao

This file contains the functions necessary for data wrangling and creating the plot.
"""

import matplotlib.pyplot as plt
import load_data
from data_class import CrimeData

# Categorization of areas (royal mounted police is not included)
AREA_DICTIONARY = {'Newfoundland': ['Royal Newfoundland Constabulary [10C01]'],
                   'New Brunswick': ['Kennebecasis Region, New Brunswick, municipal [13024]'],
                   'Ontario': ['Ottawa, Ontario, municipal [35010]',
                               'Halton Region (Oakville/Burlington), Ontario, municipal [35048]',
                               'London, Ontario, municipal [35162]',
                               'Waterloo Region (Kitchener), Ontario, municipal [35291]',
                               'Toronto, Ontario, municipal [35304]',
                               'York Region, Ontario, municipal [35335]',
                               'Ontario Provincial Police [35C01]'],
                   'Manitoba': ['Winnipeg, Manitoba, municipal [46064]'],
                   'Saskatchewan': ['Regina, Saskatchewan, municipal [47063]',
                                    'Saskatoon, Saskatchewan, municipal [47066]'],
                   'Alberta': ['Calgary, Alberta, municipal [48014]',
                               'Edmonton, Alberta, municipal [48033]'],
                   'British Columbia': ['Vancouver, British Columbia, municipal [59023]',
                                        'Victoria, British Columbia, municipal [59025]'],
                   'Quebec': ['Montréal, Quebec, municipal [24175]',
                              'Quebec Provincial Police [24C01]'],
                   'Total(National)': ['Total, Selected police services']}

# Categorization of types
TYPE_DICTIONARY = {'Assaults': ['Total assaults (levels 1, 2, 3) [141]'],
                   'Sexual Assaults': ['Total sexual assaults (levels 1, 2, 3) [131]'],
                   'Uttering threats': ['Uttering threats [1627]'],
                   'Robbery': ['Total robbery [160]'],
                   'Breaking and Entering': ['Total breaking and entering [210]'],
                   'Impaired Driving': ['Impaired driving, causing death or bodily harm [921]',
                                        'Impaired driving, operating while impaired [923]'],
                   'Calls for Service': ['Calls for service, domestic disturbances / disputes',
                                         'Calls for service, Mental Health Act (MHA) apprehension',
                                         'Calls for service, mental health - other',
                                         'Calls for service, suicide/attempted suicide',
                                         'Calls for service, overdose',
                                         'Calls for service, child welfare check',
                                         'Calls for service, check welfare - general',
                                         'Calls for service, child custody matter - domestic'],
                   'Shoplifting': ['Shoplifting [213]'],
                   'Fraud': ['Fraud/identity theft/identity fraud [216]'],
                   'COVID-19': ['Provincial/Territorial acts related to COVID-19'],
                   'Others': ['Dangerous operation, causing death or bodily harm [911]',
                              'Motor vehicle theft [2135]',
                              'Fail to comply with order [3410]']}


def get_monthly_data(year: int, month: int) -> list[CrimeData]:
    """
    Returns a list of crime data filtered from the original data
    that includes only data of the given year and month

    Preconditions:
        - 2019 <= year <= 2021
        - 1 <= month <= 12
    """

    data = load_data.load_crime_data('crime.csv')
    return [obs for obs in data if obs.year == year and obs.month == month]


def total_num_by_area_and_type(data: list[CrimeData], area: str, crime_type: str) -> int:
    """
    Returns the total number of crimes of the given area of the given type (generalized)

    Preconditions:
        - area in ['Newfoundland', 'New Brunswick', 'Ontario', 'Manitoba',
                 'Saskatchewan', 'Alberta', 'British Columbia', 'Quebec', 'Total(National)']
        - crime_type in ['Assaults', 'Sexual Assaults', 'Uttering threats', 'Robbery', 'Breaking and Entering',
                 'Impaired Driving', 'Calls for Service', 'Shoplifting', 'Fraud', 'COVID-19', 'Others']
    """

    return sum(obs.number for obs in data
               if obs.area in AREA_DICTIONARY[area] and obs.type in TYPE_DICTIONARY[crime_type])


def categorized_data(year: int, month: int) -> list[CrimeData]:
    """
    Returns a new list of CrimeData(of a specific month) that:

    Divides all crime types to the following categories:
    assaults, sexual assaults, uttering threats, robbery, breaking and entering,
    Impaired driving, Calls for service, Shoplifting, Fraud, COVID-19, others

    Divides all locations into the following areas:
    Newfoundland, New Brunswick, Ontario, Manitoba, Saskatchewan,
    Alberta, British Columbia, Quebec, Total(National)
    (Royal Canadian Mounted Police is excluded)

    The returned list always has length of 99 (9 areas * 11 types)

    Preconditions:
        - 2019 <= year <= 2021
        - 1 <= month <= 12
    """

    # Extract the monthly data
    data = get_monthly_data(year, month)

    # Get the lists of area and type. (keys of area_dictionary and type_dictionary)
    area_list = list(AREA_DICTIONARY.keys())
    type_list = list(TYPE_DICTIONARY.keys())

    # Accumulator
    new_data = []

    # Creates new CrimeData object and append the new abject to the accumulator
    for area in area_list:
        for crime_type in type_list:
            number = total_num_by_area_and_type(data, area, crime_type)
            obs = CrimeData(year=year, month=month, area=area, type=crime_type, number=number)
            new_data.append(obs)

    # Return the resulted list
    return new_data


def calculate_bottom(lst1: list[int], lst2: list[int]) -> list[int]:
    """
    Returns the bottom value to stack the bars on top of existing bars
    (a list of sums of the numbers in the two lists lst1 and lst2)

    Preconditions:
        - len(lst1) == len(lst2)

    >>> lst1 = [1, 2, 3]
    >>> lst2 = [2, 3, 4]
    >>> calculate_bottom(lst1, lst2)
    [3, 5, 7]

    """

    lst = []
    for i in range(len(lst1)):
        lst.append(lst1[i] + lst2[i])
    return lst


def create_one_plot(year: int, month: int, type_list: list[str], area_list: list[str]) -> plt.Figure:
    """
    Create a complete stacked bar plot for the data of a specific month

    For Reference:
    area_list = ['Newfoundland', 'New Brunswick', 'Ontario', 'Manitoba',
                 'Saskatchewan', 'Alberta', 'British Columbia', 'Quebec', 'Total(National)']
    type_list = ['Assaults', 'Sexual Assaults', 'Uttering threats', 'Robbery', 'Breaking and Entering',
                 'Impaired Driving', 'Calls for Service', 'Shoplifting', 'Fraud', 'COVID-19', 'Others']
    color_pal = ["#9e1642", "#d53e4f", "#f46d43", "#fdae61", "#fee08b", "#fffdbf",
                 "#e6f598", "#abdda4", '#66c2a5', '#3288bd', '#5e4fa2']

    Preconditions:
        - 2019 <= year <= 2021
        - 1 <= month <= 12
        - all(x in ['Newfoundland', 'New Brunswick', 'Ontario', 'Manitoba',
                 'Saskatchewan', 'Alberta', 'British Columbia', 'Quebec', 'Total(National)'] for x in area_list)
        - all(x in ['Assaults', 'Sexual Assaults', 'Uttering threats', 'Robbery', 'Breaking and Entering',
                 'Impaired Driving', 'Calls for Service', 'Shoplifting', 'Fraud', 'COVID-19', 'Others']
                 for x in area_list)
    """

    # Get the categorized data
    data = categorized_data(year, month)

    # Color dictionary that maps each type of crime to a color(HEX as strings)
    color_dict = {'Assaults': "#9e1642",
                  'Sexual Assaults': "#d53e4f",
                  'Uttering threats': "#f46d43",
                  'Robbery': "#fdae61",
                  'Breaking and Entering': "#fee08b",
                  'Impaired Driving': "#fffdbf",
                  'Calls for Service': "#e6f598",
                  'Shoplifting': "#abdda4",
                  'Fraud': '#66c2a5',
                  'COVID-19': '#3288bd',
                  'Others': '#5e4fa2'}

    # Creating a dictionary that maps the type of crime to a list of crime cases(number) by area
    type_num = {}
    for crime_type in type_list:
        type_num[crime_type] = [obs.number for obs in data if obs.type == crime_type and obs.area in area_list]

    # Width of the bars
    width = 0.5

    # The initial bottom
    bottom = [0 for _ in range(len(area_list))]

    fig, ax = plt.subplots()

    # Add bars to the plot, each time the bottom is modified to be the sum of previous bars(height)
    for crime_type in type_list:
        ax.bar(x=area_list,
               height=type_num[crime_type],
               width=width,
               bottom=bottom,
               label=crime_type,
               color=color_dict[crime_type])
        bottom = calculate_bottom(bottom, type_num[crime_type])

    # Labels and titles
    ax.set_ylabel('Number of Crime Cases', fontsize=7)
    ax.set_xlabel('Areas', fontsize=7)
    ax.set_title('Number of Crime Cases by Area and Type', fontsize=8)
    ax.legend(fontsize=5)
    plt.minorticks_on()
    plt.grid(visible=True, which='major', axis='both', linestyle='-', linewidth=0.5, alpha=1.0)
    plt.grid(visible=True, which='minor', axis='both', linestyle='--', linewidth=0.5, alpha=0.2)
    plt.xticks(fontsize=6)
    plt.yticks(fontsize=6)

    fig.canvas.set_window_title('CSC110 Final Project - Connection between COVID-19 and Crime - Analysis 1')

    return fig


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'data_class', 'matplotlib.pyplot', 'load_data'],
        'allowed-io': [],
        'max-line-length': 120,
        'disable': []
    })

    import python_ta.contracts
    python_ta.contracts.check_all_contracts()

    import doctest
    doctest.testmod()
