import logging

import pandas

import sportsball.batting_avg as batting_avg
import sportsball.utils as utils

logging.basicConfig(level=logging.DEBUG)

def filter_league_year(df, league, year, min_at_bats=400):
    df_filtered = df[(df['league'] == league) & (df['yearID'] == year) & (df['AB'] >= min_at_bats)].copy()
    return df_filtered

def get_max_batting_avg(df):
    batting_avg_df = batting_avg.calculate_batting_average(df)
    max_batting_avg = batting_avg_df['batting_avg'].max()
    return max_batting_avg

def get_max_home_runs(df):
    max_hr = df['HR'].max()
    return max_hr

def get_max_rbi(df):
    max_rbi = df['RBI'].max()
    return max_rbi
    
def find_triple_crown(df, max_batting_avg, max_hr, max_rbi):
    triple_crown_df = df[(df['batting_avg'] == max_batting_avg) & (df['HR'] == max_hr) & (df['RBI'] == max_rbi)]
    triple_crown_name_df = utils.add_player_details(triple_crown_df)
    if len(triple_crown_name_df) == 1:
        player_name = ' '.join(triple_crown_name_df[['nameFirst', 'nameLast']].values[0])
        return player_name
    else:
        return 'No Winner'

def get_triple_crown_winner(df, league, year, min_at_bats):
    filtered_df = filter_league_year(df, league, year, min_at_bats=min_at_bats)
    grouped_df = utils.group_by_player_year_league(filtered_df)
    max_hr = get_max_home_runs(grouped_df)
    max_batting_avg = get_max_batting_avg(grouped_df)
    max_rbi = get_max_rbi(grouped_df)
    winner = find_triple_crown(grouped_df, max_batting_avg, max_hr, max_rbi)

    print('Triple Crown Winner (League: {l}, Year: {y}): '.format(l=league, y=year), winner)


def main(leagues, years, min_at_bats):
    batting_df = utils.import_data('batting')

    for year in years:
        for league in leagues:
            get_triple_crown_winner(batting_df, league, year, min_at_bats)

if __name__ == '__main__':
    leagues = ['AL', 'NL']
    years = range(2011, 2012 + 1)
    min_at_bats = 400
    main(leagues, years, min_at_bats)
