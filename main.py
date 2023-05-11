import requests, time
from bs4 import BeautifulSoup
from flask import Flask, request

app = Flask(__name__)

my_headers = headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 '
                                      '(KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

@app.route("/")
def home():
    return "Welcome, this is the home page."


@app.route("/price", methods=['GET'])
def price():
    name = request.args.get('name')

    def get_price(name):
        url = get_search_url(name)
        r = requests.get(url, headers=my_headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        price = soup.find('span', 'format')
        if price is None:
            price = "Pricing not available."
        else:
            price = price.next_element.next_element.next_element.get_text()
            price = price[price.find("$"):len(price) + 1]
        return price

    def get_search_url(name):
        name = name.replace(' ', '+')
        print(name)
        url_search = "https://www.barnesandnoble.com/s/" + name
        return url_search

    return get_price(name)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
