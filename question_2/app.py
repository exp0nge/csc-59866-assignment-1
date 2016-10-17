from flask import Flask, render_template, request
from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup


# Search query paths
google_search_url = "https://www.google.com/#q="
bing_search_url = "http://www.bing.com/search?q="
duckduck_go_search_url = "http://www.bing.com/search?q="

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("base.html", form_url='/query')


@app.route('/query', methods=['POST'])
def query():
    if request.method == 'POST':
        search_query = request.form['query']


def get_google_data(url):
    pass


def get_bing_data(url):
    pass


def get_duck_data(url):
    pass

if __name__ == '__main__':
    app.run(debug=True)
