from bs4 import BeautifulSoup


def get_score_links(weekly_score_page):
    soup = BeautifulSoup(weekly_score_page, 'lxml')

    # PFR Specific
    links = soup.find_all("a", string='Final')

    links = ['https://www.pro-football-reference.com' + lk.attrs['href'] for lk in links]

    return links