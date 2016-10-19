from flask import Flask, render_template, request
from url_data import get_search_engine_content, get_ask_search_results

# Search query paths
bing_search_url = "http://www.bing.com/search?q="
ask_search_url = "http://www.ask.com/web?q=query"


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("base.html", form_url='/query')


@app.route('/query', methods=['POST'])
def query():
    if request.method == 'POST':
        search_query = request.form['query']
        # bing_data = get_search_engine_content(bing_search_url + search_query)
        ask_data = get_search_engine_content(ask_search_url + search_query)
        get_ask_search_results(ask_data)


if __name__ == '__main__':
    app.run(debug=True)
