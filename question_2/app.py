from flask import Flask, render_template, request

# Search query paths
google_search_url = "https://www.google.com/#q="
bing_search_url = "http://www.bing.com/search?q="
duckduck_go_search_url = "http://www.bing.com/search?q="

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    print request.method
    print request.form
    return render_template("base.html")


if __name__ == '__main__':
    app.run()
