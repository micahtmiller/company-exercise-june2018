import logging

import pandas

import config
import utils

logging.basicConfig(level=logging.DEBUG)

def filter_team_year(df, team, year):
    filtered_df = df[(df['teamID'] == team) & (df['yearID'] == year)].copy()
    return filtered_df

def calculate_sluggers(df):
    df['slugging_perc'] = (
        (
            (df['H'] - df['2B'] - df['3B'] - df['HR']) + (2 * df['2B']) + (3 * df['3B']) + (4 * df['HR'])
        ) / df['AB']
    )
    return df[['playerID', 'slugging_perc']].sort_values(by=['slugging_perc'], ascending=False).reset_index(drop=True)

def get_slugging_percentage(df, team, year):
    filtered_df = filter_team_year(df, team, year)
    slugging_perc_df = calculate_sluggers(filtered_df)
    print('All Players Slugging Percentage (Team: {t} , Year: {y})'.format(t=team, y=year))
    print(slugging_perc_df)

def main(team, year):
    batting_df = utils.import_data('batting')
    get_slugging_percentage(batting_df, team, year)

if __name__ == '__main__':
    main('OAK', 2007)
