import logging

import pandas
import pytest

import config
import sportsball.triple_crown_winner as triple_crown_winner

logging.basicConfig(level=logging.DEBUG)

def test_filter_league_year():
    league = 'AL'
    year = 2009

    data = [
        {'league': 'AL', 'yearID': 2009, 'AB': 500}
    ]
    test_df = pandas.DataFrame(data)
    df = triple_crown_winner.filter_league_year(test_df, league, year, min_at_bats=400)
    assert df.equals(test_df)

    data = [
        {'league': 'AL', 'yearID': 2009, 'AB': 300}
    ]
    test_df = pandas.DataFrame(data)
    df = triple_crown_winner.filter_league_year(test_df, league, year, min_at_bats=400)
    assert df.equals(test_df) == False

    data = [
        {'league': 'AL', 'yearID': 2010, 'AB': 500}
    ]
    test_df = pandas.DataFrame(data)
    df = triple_crown_winner.filter_league_year(test_df, league, year, min_at_bats=400)
    assert df.equals(test_df) == False

    data = [
        {'league': 'NL', 'yearID': 2009, 'AB': 500}
    ]
    test_df = pandas.DataFrame(data)
    df = triple_crown_winner.filter_league_year(test_df, league, year, min_at_bats=400)
    assert df.equals(test_df) == False

def test_get_max_home_runs():
    data = [
        {'HR': 5},
        {'HR': 10}
    ]
    test_df = pandas.DataFrame(data)
    max_hr = triple_crown_winner.get_max_home_runs(test_df)
    assert max_hr == 10

def test_get_max_rbi():
    data = [
        {'RBI': 5},
        {'RBI': 10}
    ]
    test_df = pandas.DataFrame(data)
    max_rbi = triple_crown_winner.get_max_rbi(test_df)
    assert max_rbi == 10

def test_get_max_batting_avg():
    '''
    Max batting avg should be 0.5
    '''
    data = [
        {'AB': 10, 'H': 5},
        {'AB': 10, 'H': 2}
    ]
    test_df = pandas.DataFrame(data)
    max_batting_average = triple_crown_winner.get_max_batting_avg(test_df)
    assert max_batting_average == 0.5

if __name__ == '__main__':
    test_filter_league_year()
