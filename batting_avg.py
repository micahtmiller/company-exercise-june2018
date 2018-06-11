import pandas

import utils

def calculate_batting_average(df):
    df['batting_avg'] = df['H']/df['AB']
    return df

def filter_by_year(df, year):
    filtered_df = df[df['yearID'] == year].copy()
    return filtered_df

def merge_data(df1, df2):
    merged_df = df2.merge(df1, how='inner', on=['playerID'], suffixes=['_2', '_1'])
    return merged_df

def at_bats_filter(df, min_at_bats=200):
    filtered_df = df[(df['AB_2'] >= min_at_bats) & (df['AB_1'] >= min_at_bats)].copy()
    return filtered_df

def calculate_most_improved(df):
    df['improved_batting_avg'] = df['batting_avg_2'] - df['batting_avg_1']
    most_improved_df = df[df['improved_batting_avg'] == df['improved_batting_avg'].max()]
    return most_improved_df

def get_most_improved(df, start_year, end_year):
    grouped_df = utils.group_by_player_year_league(df)
    batting_avg_df = calculate_batting_average(grouped_df)
    df_older = filter_by_year(batting_avg_df, start_year)
    df_newer = filter_by_year(batting_avg_df, end_year)
    merged_df = merge_data(df_older, df_newer)
    # filtered_df = at_bats_filter(merged_df, min_at_bats=350) #optional min_at_bats, default=200
    filtered_df = at_bats_filter(merged_df)
    most_improved_df = calculate_most_improved(filtered_df)
    if len(most_improved_df) == 1:
        print('Most Improved Batting Average is: ', most_improved_df['playerID'].values[0])
    elif len(most_improved_df) > 1:
        print('There are multiple "Most Improved Batting Average"s')
        for i, row in most_improved_df.iterrows():
            print('Most Improved Batting Average is: ', row['playerID'])

def main():
    batting_df= utils.import_data('batting')
    get_most_improved(batting_df, 2009, 2010)

if __name__ == '__main__':
    main()
