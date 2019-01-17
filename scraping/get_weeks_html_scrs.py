_2018_weekly_NFL_scores = []

nfl_reference_base_url = 'https://www.pro-football-reference.com/years/2018/week_{}.htm'

def nfl_week_url(week):
    return nfl_reference_base_url.replace('{}', str(week))

_2018_weekly_NFL_scores = [nfl_week_url(wk) for wk in range(1,21)]


for url in _2018_weekly_NFL_scores:
    print(url)

weekly_score_summary_html = []

import time

def strip_html_nwlns_cmnts(html_txt):
    rslt = html_txt.replace('\n', '').replace('<!--', '').replace('-->', '')
    return rslt

for url in _2018_weekly_NFL_scores:
    raw_fetch = requests.get(url).text
    fetched = strip_html_nwlns_cmnts(raw_fetch)
    weekly_score_summary_html.append(fetched)
    print(f'Fetched {url}')
    print('zzzzzzzz')
    time.sleep(3)
    print('woke_up')

#weekly_score_summary_html

import pickle

output = open('/Users/bjg/Desktop/wkly_scre_list.pkl', 'wb')

pickle.dump(weekly_score_summary_html, output)

output.close()


#pklfl = open('/Users/bjg/Desktop/wkly_scre_list.pkl', 'rb')
#lst = pickle.load(pklfl)
#pklfl.close()