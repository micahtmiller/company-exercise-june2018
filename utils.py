import os

import pandas

import config

def import_data():
    batting_df = pandas.read_csv(os.path.join(config.DATA_FILES_LOCATION, 'Batting-07-12.csv'))
    player_df = pandas.read_csv(os.path.join(config.DATA_FILES_LOCATION, 'Master-small.csv'))
    # pitching_df = pandas.read_csv(os.path.join(file_location, 'xxxx.csv'))
    return batting_df, player_df