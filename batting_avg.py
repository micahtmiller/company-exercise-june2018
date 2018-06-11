import pandas

import utils


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
    merged_df = df2.merge(df1, how='inner', on=['playerID'], suffixes=['_2', '_1'])
    return merged_df

def at_bats_filter(df, min_at_bats=200):
    filtered_df = df[(df['AB_2'] >= min_at_bats) & (df['AB_1'] >= min_at_bats)].copy()
    return filtered_df

def calculate_most_improved(df):
    df['improved_batting_avg'] = df['batting_avg_2'] - df['batting_avg_1']
    most_improved_df = df[df['improved_batting_avg'] == df['improved_batting_avg'].max()]
    return most_improved_df

def main():
    batting_df, player_df = utils.import_data()
    grouped_df = group_by_player_and_year(batting_df)
    batting_avg_df = calculate_batting_average(grouped_df)
    df_2009 = filter_by_year(batting_avg_df, 2009)
    df_2010 = filter_by_year(batting_avg_df, 2010)
    merged_df = merge_data(df_2009, df_2010)
    # filtered_df = at_bats_filter(merged_df, min_at_bats=350) #optional min_at_bats, default=200
    filtered_df = at_bats_filter(merged_df)
    most_improved_df = calculate_most_improved(filtered_df)
    # merge player_df to get names, not just code for better readability
    if len(most_improved_df) == 1:
        print('Most Improved Player is: ', most_improved_df['playerID'].values[0])
    elif len(most_improved_df) > 1:
        print('There are multiple "Most Improved Player"s')
        for i, row in most_improved_df.iterrows():
            print('Most Improved Player is: ', row['playerID'])

if __name__ == '__main__':
    main()
