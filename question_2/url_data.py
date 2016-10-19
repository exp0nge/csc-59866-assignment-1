from requests import get
from fake_useragent import UserAgent
from bs4 import BeautifulSoup, element

user_agent = UserAgent(cache=True)
chrome_user = {'User-Agent': user_agent.chrome}


def get_search_engine_content(url, do_write=False, path=None):
    """
    Gets the entire content of the search engine results, unparsed data
    :param url:
    :param do_write:
    :param path:
    :return:
    """
    data = get(url, headers=chrome_user)
    if do_write:
        with open(path, 'w') as output:
            output.write("%s" % data.text.encode('utf-8'))
    soup = BeautifulSoup(data.text, 'html.parser')
    return soup


def get_bing_search_results(soup, samples):
    """
    Returns the first x results
    :param soup: BeautifulSoup
    :param samples: int
    :return: string
    """
    ul = soup.find_all(id='b_results')
    for item in ul:
        for h in item.find_all('h2'):
            a = h.find('a')
            if a is not None:
                url_text = (a['href'], a.get_text())
                print url_text
        for caption in item.find_all('div', { 'class': 'b_caption'}):
            summary = caption.find('p')
            print summary


def get_ask_search_results(soup):
    ul = soup.find_all('div', {'class':'l-mid-content hcsa'})
    results = ul[0].find('div', {'class': 'l-web-results web-results content-mid'})
    for item in results:
        if type(item) == element.Tag:
            h = item.find('h2')
            if h is not None:
                a = h.find('a')
                if a is not None:
                    url = (a['href'], a.get_text())
                    print url
            summary = item.find('p', {'class': 'web-result-description'})
            if summary is not None:
                print summary


def get_yahoo_search_results(soup):
    pass
