import sportsball.utils as utils
import sportsball.batting_avg as batting_avg
import sportsball.slugging_percentage as slugging_percentage
import sportsball.triple_crown_winner as triple_crown_winner

def main():
    batting_df = utils.import_data('batting')
    batting_avg.get_most_improved(batting_df, 2009, 2010)
    slugging_percentage.get_slugging_percentage(batting_df, 'OAK', 2007)
    triple_crown_years = range(2011, 2012 + 1)
    leagues = ['NL', 'AL']
    for year in triple_crown_years:
        for league in leagues:
            triple_crown_winner.get_triple_crown_winner(batting_df, league, year)

if __name__ == '__main__':
    main()