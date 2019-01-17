




nfl_reference_base_url = 'https://www.pro-football-reference.com/years/2018/week_{}.htm'

def nfl_week_url(week):
    return nfl_reference_base_url.replace('{}', str(week))

urls = [nfl_week_url(wk) for wk in range(1,21)]

[print(url) for url in urls]
