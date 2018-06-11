import pytest
import pandas

import sportsball.slugging_percentage as slugging_percentage

import config

import logging

logging.basicConfig(level=logging.DEBUG)

def test_filter_oakland_2007():
    team = 'OAK'
    year = 2007
    data = [
        {'teamID': 'OAK', 'yearID': 2007},
        # {'teamID': 'OAK', 'yearID': 2008},
        # {'teamID': 'OTH', 'yearID': 2007},
    ]
    test_df = pandas.DataFrame(data)
    filtered_df = slugging_percentage.filter_team_year(test_df, team, year)
    assert len(filtered_df) == 1
    data = [
        # {'teamID': 'OAK', 'yearID': 2007},
        {'teamID': 'OAK', 'yearID': 2008},
        # {'teamID': 'OTH', 'yearID': 2007},
    ]
    test_df = pandas.DataFrame(data)
    filtered_df = slugging_percentage.filter_team_year(test_df, team, year)
    assert len(filtered_df) == 0
    data = [
        # {'teamID': 'OAK', 'yearID': 2007},
        # {'teamID': 'OAK', 'yearID': 2008},
        {'teamID': 'OTH', 'yearID': 2007},
    ]
    test_df = pandas.DataFrame(data)
    filtered_df = slugging_percentage.filter_team_year(test_df, team, year)
    assert len(filtered_df) == 0
    
def test_calculate_sluggers():
    data = [
        {'playerID': 'test', 'H': 4, '2B': 1, '3B': 1, 'HR': 1, 'AB': 5}
    ]
    # (4 -1(double) -1(triple) -1(hr)) = 1
    # (1 + 2 * 1 + 3 * 1 + 4 * 1)  = 10
    # 10 / 5 = 2.0
    test_df = pandas.DataFrame(data)
    sluggers_df = slugging_percentage.calculate_sluggers(test_df)
    logging.debug(sluggers_df)
    assert sluggers_df['slugging_perc'].values[0] == 2.0 
    data = [
        {'playerID': 'test', 'H': 8, '2B': 2, '3B': 2, 'HR': 2, 'AB': 40}
    ]
    # (8 -2(double) -2(triple) -2(hr)) = 2
    # (2 + 2 * 2 + 3 * 2 + 4 * 2)  = 20
    # 20 / 40 = .5
    test_df = pandas.DataFrame(data)
    sluggers_df = slugging_percentage.calculate_sluggers(test_df)
    logging.debug(sluggers_df)
    assert sluggers_df['slugging_perc'].values[0] == 0.5

if __name__ == '__main__':
    test_calculate_sluggers()