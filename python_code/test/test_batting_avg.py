import pytest
import pandas

import sportsball.batting_avg as batting_avg

import config

import logging

logging.basicConfig(level=logging.DEBUG)

def test_calculate_batting_average():
    test_df = pandas.DataFrame([{'H': 1, 'AB': 2}])
    batting_avg_df = batting_avg.calculate_batting_average(test_df)
    logging.debug(batting_avg_df)
    assert batting_avg_df['batting_avg'].values[0] == .5

def test_calculate_most_improved():
    data = [
        {'batting_avg_2':.5, 'batting_avg_1':.4},
        {'batting_avg_2':.5, 'batting_avg_1':.3},
    ]
    test_df = pandas.DataFrame(data)
    most_improved_df = batting_avg.calculate_most_improved(test_df)
    logging.debug(most_improved_df)
    assert len(most_improved_df) == 1
    assert most_improved_df['improved_batting_avg'].values[0] == 0.2

if __name__ == '__main__':
    test_calculate_batting_average()
    test_calculate_most_improved()
