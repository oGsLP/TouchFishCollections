import requests
from requests_html import HTMLSession

player_url = "http://pokemonshowdown.com/users/{username}"
session = HTMLSession()


def crawl_player(username="oGsLP"):
    res = session.get(player_url.format(username=username))
    table = res.html.find("table").find("tr")
    print(table)


if __name__ == '__main__':
    crawl_player()
