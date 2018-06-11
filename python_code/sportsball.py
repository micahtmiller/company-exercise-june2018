import sportsball.utils as utils
import sportsball.batting_avg as batting_avg
import sportsball.slugging_percentage as slugging_percentage
import sportsball.triple_crown_winner as triple_crown_winner

import config

def main():
    batting_df = utils.import_data('batting')
    batting_avg.get_most_improved(batting_df, config.MOST_IMPROVED_START_YEAR, config.MOST_IMPROVED_END_YEAR, config.BATTING_AVG_MIN_AT_BATS)
    slugging_percentage.get_slugging_percentage(batting_df, config.SLUGGING_TEAM, config.SLUGGING_YEAR)
    triple_crown_years = range(config.TRIPLE_CROWN_START_YEAR, config.TRIPLE_CROWN_END_YEAR + 1)
    leagues = config.TRIPLE_CROWN_LEAGUES
    for year in triple_crown_years:
        for league in leagues:
            triple_crown_winner.get_triple_crown_winner(batting_df, league, year, config.TRIPLE_CROWN_MIN_AT_BATS)

if __name__ == '__main__':
    main()