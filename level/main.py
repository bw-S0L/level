import flask
from flask_cors import CORS
from flask import Flask

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/level1')
def level1():
    return flask.send_from_directory('static', 'level1.html')

@app.route('/level2')
def level2():
    return flask.send_from_directory('static', 'level2.html')

@app.route('/level3')
def level3():
    return flask.send_from_directory('static', 'level3.html')

""""@app.route('/favicon.ico')
def favicon(): 
    return flask.send_from_directory('static', 'loveheart.ico', mimetype='image/vnd.microsoft.icon')"""

app.run(host='0.0.0.0', port=11667, debug=True)
