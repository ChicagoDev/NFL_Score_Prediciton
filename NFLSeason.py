import pandas as pd
import requests
import copy
import pickle
import time



class NFLSeason(object):
    """Scrapes from PFR, Saves Database for later EDA"""

    database = pd.DataFrame()
    score_by_quarter_pandas_html_indices = {1: 16, 2: 16, 3: 16, 4: 15, 5: 15, 6: 15, 7: 14, 8: 14, 9: 13, 10: 14,
                                            11: 13, 12: 15, 13: 16, 14: 16, 15: 16, 16: 16, 17: 16, 18: 4}
    game_summary_df_pfr_indicies = {}
    urls = None
    found_count = 0

    def __init__(self):


        with open('urls', 'rb') as fl:
            self.urls = pickle.load(fl)

        self.game_summary_df_pfr_indicies = copy.deepcopy(self.score_by_quarter_pandas_html_indices)

        for week , df_index_on_webpg in self.game_summary_df_pfr_indicies.items():
            df_index_on_webpg += 5

        self.scrape_all(self.urls)
        self.save_database('nfl.database.pkl')

        return

    def save_database(self, path):

        with open(f'{path}', 'wb') as fl:
            pickle.dump(self.database, fl)

        return



    def strip_html_nwlns_cmnts(self, html_txt):
        rslt = html_txt.replace('\n', '').replace('<!--', '').replace('-->', '')
        return rslt

    def scrape_all(self, url_dict_by_wk):

        for week , url_list in url_dict_by_wk.items():

            for url in url_list:

                #TODO Add the tables, concatenate to database
                #Get the quarter summary, and Dfs

                game_shrt_summary = None
                scraped_frames = []
                game_lng_report = None
                data_set_entry = None

                try:

                    print(f'Getting 4 qtr summary')
                    game_shrt_summary, scraped_frames = self.scrape_quarter_summary(url, week + 1)

                    print(f'Getting long game summary from dfs')
                    game_lng_report = self.get_game_summary_df_from_scrape(scraped_frames)

                    print(f'Merging dfs')
                    data_set_entry = self.merge_game_summaries(game_shrt_summary, game_lng_report)

                    print(f'appending df to master')
                    self.database.append(data_set_entry, ignore_index=True)

                    print(f'Appended table #{self.found_count}')
                    self.found_count += 1



                except:
                    print(f'Unable to locate DFs for {url}')


    def scrape_quarter_summary(self, url, week_no):

        """A Summary of The Game By Quarters"""
        time.sleep(4)
        resp = requests.get(url).text
        resp_trimmed = self.strip_html_nwlns_cmnts(resp)

        dfs = pd.read_html(resp_trimmed)

        quarter_table = dfs[self.score_by_quarter_pandas_html_indices[week_no]].copy(deep=True)

        if quarter_table.shape == (2, 7):

            quarter_table.rename(columns={'Unnamed: 0': 'HOME/AWAY', 'Unnamed: 1': 'TEAM'}, inplace=True)

            quarter_table.iloc[1, 0] = 'HOME'
            quarter_table.iloc[0, 0] = 'AWAY'

            week = pd.DataFrame([week_no, week_no], columns=['WEEK'])

            summary = quarter_table.merge(week, left_index=True, right_index=True)

            print(f'Retrieved {summary} @ {url}')
            return (summary, dfs)

        else:

            print(f'Bad Quarter Table')
            #raise Exception("Index chosen does not match dimensions of 4-Quarter Table")



    def merge_game_summaries(self, quarters_df, gm_summary_df):

        long_game_data = copy.deepcopy(gm_summary_df)
        long_game_data.reset_index()
        long_game_data.columns = long_game_data.iloc[0]
        long_tbl = long_game_data.iloc[1:3, :].reset_index()

        http_ftchd_tbl = copy.deepcopy(quarters_df)

        intermediate_mrg = long_tbl.merge(http_ftchd_tbl, left_index=True, right_index=True)

        swaped_index_merge = intermediate_mrg.reindex(pd.Index([1, 0]), axis=0)

        complete_game_summary = swaped_index_merge.merge(long_tbl, left_index=True, right_index=True,
                                              suffixes=('_challenger', '_defender'))

        return complete_game_summary

    def get_game_summary_df_from_scrape(self, dfs):

        for tbl in dfs:
            if tbl.shape == (12, 3):
                long_game_summary = tbl.transpose()  # This table is five
        # y = x.reset_index()
        # x.reindex([1,0], axis=0)
        return long_game_summary


if __name__ == '__main__':
    scraper = NFLSeason()





