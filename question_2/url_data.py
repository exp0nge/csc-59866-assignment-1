from requests import get
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

user_agent = UserAgent(cache=True)
chrome_user = { 'User-Agent': user_agent.chrome }


def get_search_engine_content(url, do_write=False, path=None):
    """
    Gets the entire content of the search engine results, unparsed data
    :param url:
    :param do_write:
    :param path:
    :return:
    """
    data = get(url, headers = user_agent)
    if do_write:
        with open(path) as output:
            output.write("%s" % data.text.encode('utf-8'))
    return BeautifulSoup(data).prettify(encoding='utf-8')


def get_search_results(samples):
    """
    Returns the first x results
    :param samples: int
    :return: string
    """
    pass

