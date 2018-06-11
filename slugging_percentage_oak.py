import logging

import pandas

import config
import utils

logging.basicConfig(level=logging.DEBUG)

def filter_oakland_2007(df):
    filtered_df = df[(df['teamID'] == 'OAK') & (df['yearID'] == 2007)].copy()
    return filtered_df

def calculate_sluggers(df):
    df['slugging_perc'] = (
        (
            (df['H'] - df['2B'] - df['3B'] - df['HR']) + (2 * df['2B']) + (3 * df['3B']) + (4 * df['HR'])
        ) / df['AB']
    )
    return df[['playerID', 'slugging_perc']].sort_values(by=['slugging_perc'], ascending=False).reset_index()

def main():
    batting_df = utils.import_data('batting')
    filtered_df = filter_oakland_2007(batting_df)
    slugging_perc_df = calculate_sluggers(filtered_df)
    print('All Players Slugging Percentage')
    print(slugging_perc_df)

if __name__ == '__main__':
    main()
