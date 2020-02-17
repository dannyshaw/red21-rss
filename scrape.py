from bs4 import BeautifulSoup
from flask import Flask, make_response
import requests
from feedgen.feed import FeedGenerator
import os


def scrape_table_data(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html)
    table = soup.select_one("table")

    # python3 just use th.text
    headers = [th.text for th in table.select("tr th")]

    table_data = [{
        headers[index]: td.text
        for index, td in enumerate(row.find_all("td"))
    } for row in table.select("tr + tr")]

    return table_data


def generate_feed(table_data, url):
    fg = FeedGenerator()
    fg.id('http://dannyshaw.github.io/dions-thing')
    fg.title('Dion\'s Cashflow')
    fg.description('Dion\'s Cashflow')
    fg.language('en')
    fg.link(href=url, rel='alternate')

    for index, entry in enumerate(table_data):
        fe = fg.add_entry()
        fe.id(entry['order_id'])
        fe.title(f'{entry["customer_name"]} bought a ticket')
        fe.description(f'{entry["customer_name"]} bought a ticket')
        fe.link(href=url)

    return fg.rss_str(pretty=True)


source_url = os.environ.get('RED21_DATA_SOURCE', None)
if not source_url:
    raise RuntimeError('You need to set RED21_DATA_SOURCE')
app = Flask(__name__)


@app.route('/')
def produce_feed():
    table_data = scrape_table_data(source_url)
    rss_xml = generate_feed(table_data, source_url)
    response = make_response(rss_xml)
    response.headers['Content-Type'] = 'application/rss+xml'
    return response


if __name__ == '__main__':
    app.run()

