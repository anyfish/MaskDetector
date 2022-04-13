from flask import Flask
from flask import render_template, request, url_for

app = Flask(__name__)
PORT = 5000
DEBUG = True

@app.errorhandler(404)
def not_found(error):
    return "Not Found"

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=PORT,debug=DEBUG)
