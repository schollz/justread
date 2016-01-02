from flask import Flask, render_template, request, jsonify

from parseDoc import *

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['POST','GET'])
def hello():
    url = ''
    if request.method == 'GET':
        url = request.args.get('url', '')
    if request.method == 'POST':
        url = request.form['group'].lower()
    if len(url) < 10:
        return render_template('index.html')
    else:
        print(url)
        data = getDoc2(url)
        return render_template('article3.html', data=data)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8009)
