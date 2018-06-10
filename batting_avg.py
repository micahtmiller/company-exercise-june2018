import os

import pandas

import config

def import_data(file_location):
    batting_df = pandas.read_csv(os.path.join(file_location, 'Batting-07-12.csv'))
    player_df = pandas.read_csv(os.path.join(file_location, 'Master-small.csv'))
    return batting_df, player_df

def group_by_player_and_year(df):
    grouped_df = df.groupby(by=['playerID', 'yearID'])['AB', 'H'].sum().reset_index()
    return grouped_df

def calculate_batting_average(df):
    df['batting_avg'] = df['H']/df['AB']
    return df

def filter_by_year(df, year):
    filtered_df = df[df['yearID'] == year].copy()
    return filtered_df

def merge_data(df1, df2):
    max_year1 = df1['yearID'].max()
    max_year2 = df2['yearID'].max()
    merged_df = df2.merge(df1, how='inner', on=['playerID'], suffixes=['_{}'.format(max_year2), '_{}'.format(max_year1)])
    return merged_df

def at_bats_filter(df, min_at_bats=200):
    df['total_at_bats'] = df['AB_2010'] + df['AB_2009']
    filtered_df = df[df['total_at_bats'] >= min_at_bats].copy()
    return filtered_df

def calculate_most_improved(df):
    most_improved_df = df[df['improved_batting_avg'] == df['improved_batting_avg'].max()]
    return most_improved_df

def main():
    batting_df, player_df = import_data(config.DATA_FILE_LOCATION)
    grouped_df = group_by_player_and_year(batting_df)
    batting_avg_df = calculate_batting_average(grouped_df)
    df_2009 = filter_by_year(batting_avg_df, 2009)
    df_2010 = filter_by_year(batting_avg_df, 2010)
    merged_df = merge_data(df_2009, df_2010)
    filtered_df = at_bats_filter(merged_df) #optional min_at_bats
    most_improved_df = calculate_most_improved(filtered_df)
    # merge player_df to get names, not just code for better readability
    if len(most_improved_df) == 1:
        print('Most Improved Player is: ', most_improved_df['playerID'][0])
    elif len(most_improved_df) > 1:
        print('There are multiple "Most Improved Player"s')
        for i, row in most_improved_df.iterrows():
            print('Most Improved Player is: ', row['playerID'])

if __name__ == '__main__':
    main()
