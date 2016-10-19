from flask import Flask, render_template, request
from fake_useragent import UserAgent


# Search query paths
google_search_url = "https://www.google.com/#q="
bing_search_url = "http://www.bing.com/search?q="
duckduck_go_search_url = "http://www.bing.com/search?q="

user_agent = UserAgent()
user_chrome = { 'User-Agent': user_agent.chrome }
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("base.html", form_url='/query')


@app.route('/query', methods=['POST'])
def query():
    if request.method == 'POST':
        search_query = request.form['query']


if __name__ == '__main__':
    app.run(debug=True)
