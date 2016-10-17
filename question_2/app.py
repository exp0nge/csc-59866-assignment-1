from flask import Flask

# Search query paths
google_search_url = "https://www.google.com/#q="
bing_search_url = "http://www.bing.com/search?q="
duckduck_go_search_url = "http://www.bing.com/search?q="

app = Flask(__name__)

@app.route('/')
def index():
    # TODO: Make a search form
    # TODO: Make a get request and scrape the web
    pass

if __name__ == '__main__':
    app.run()
