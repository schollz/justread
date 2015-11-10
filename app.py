from flask import Flask, render_template, request, jsonify

from parseDoc import *

app = Flask(__name__)
app.debug = True

@app.route("/")
def hello():
    url = request.args.get('url', '')
    print(url)
    data = getDoc(url)
    return render_template('article.html', data=data)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8012)