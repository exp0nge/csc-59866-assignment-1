from flask import Flask, render_template, request, redirect
from url_data import get_search_engine_content, get_ask_search_results, get_yahoo_search_results, get_bing_search_results

# Search query paths
bing_search_url = "http://www.bing.com/search?q="
ask_search_url = "http://www.ask.com/web?q=query"
yahoo_search_url = "https://search.yahoo.com/search;?p="


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("base.html", form_url='/query')


@app.route('/query', methods=['POST'])
def query():
    if request.method == 'POST':
        search_query = request.form['query']
        bing_data = get_search_engine_content(bing_search_url + search_query)
        bing_result = get_bing_search_results(bing_data)
        ask_data = get_search_engine_content(ask_search_url + search_query)
        ask_result = get_ask_search_results(ask_data)
        yahoo_data = get_search_engine_content(yahoo_search_url + search_query)
        yahoo_results = get_yahoo_search_results(yahoo_data)

        return redirect('/results')
        # return render_template("results.html", result_1=bing_result, result_2=ask_result, result_3=yahoo_results)


@app.route('/results')
def show_results():
    pass


if __name__ == '__main__':
    app.run(debug=True)
