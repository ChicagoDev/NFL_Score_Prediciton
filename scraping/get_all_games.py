import pandas as pd
import requests


def strip_html_nwlns_cmnts(html_txt):
    '''
    Removes misc. characters from HTML file to prep for parsing with Pandas.
    PFR sites comment out tables, so this is required.
    :param html_txt:
    :return:
    '''
    rslt = html_txt.replace('\n', '').replace('<!--', '').replace('-->', '')
    return rslt



def get_games_table(url):
    '''
    Returns a specialized set of pandas tables from a ProFootballReference URL
    :param url: A String URL to a PFR single NFL Game
    :return: List of Tables
    '''

    table_indicies = [16, 17, 18, 21, 22, 23, 24, 34, 35]

    game_html = requests.get(url).text
    game_html = strip_html_nwlns_cmnts(game_html)

    table_dfs = pd.read_html(game_html)

    tables = []
    for val in table_indicies:
        tables.append(table_dfs[val])

    return tables


