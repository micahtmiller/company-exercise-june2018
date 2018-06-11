import logging
import os

import pandas

import config

logging.basicConfig(level=logging.DEBUG)

def import_data(kind):
    if kind == 'batting':
        df = pandas.read_csv(os.path.join(config.DATA_FILES_LOCATION, 'Batting-07-12.csv'))
    elif kind == 'player':
        df = pandas.read_csv(os.path.join(config.DATA_FILES_LOCATION, 'Master-small.csv'))
    elif kind == 'pitching':
        df = pandas.read_csv(os.path.join(config.DATA_FILES_LOCATION, 'xxxx.csv'))
    else:
        logging.info('No file kind found')
    return df

def add_player_details(df):
    player_df = import_data('player')
    batting_player_df = df.merge(player_df, how='inner', on='playerID')
    return batting_player_df

def group_by_player_year_league(df):
    grouped_df = df.groupby(by=['playerID', 'yearID', 'league'])['G', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'SB', 'CS'].sum().reset_index()
    return grouped_df
