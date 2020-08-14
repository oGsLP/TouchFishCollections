import requests

ladder_url = "https://pokemonshowdown.com/ladder/"


def crawl_ladder(kind):
    _url = ladder_url + kind
    res = requests.get(_url)
    print(res.content)


if __name__ == '__main__':
    crawl_ladder("Random")
