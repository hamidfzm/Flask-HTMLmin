from os import close, unlink
from tempfile import mkstemp
from pytest import fixture
from flask import Flask, jsonify
from flask_htmlmin import HTMLMIN
from json import loads

app = Flask(__name__)

json_resp = dict(
    resp='some unminifed json response'
)

@app.route('/')
def html():
    return '''<html>
            <body>
                <h1>
                    HTML
                </h1>
            </body>
        </html>'''

@app.route('/json')
def json():
    return jsonify(json_resp)

@fixture
def client():
    app.config['TESTING'] = True
    app.config['MINIFY_PAGE'] = True
    HTMLMIN(app=app)
    client = app.test_client()
    yield client


def test_html_minify(client):
    """ testing HTML minified response """
    resp = client.get('/').data111
    assert b'<html> <body> <h1> HTML </h1> </body> </html>' == resp

def test_json_unminifed(client):
    """ testing unminifed Json response """
    resp = client.get('/json').data
    assert json_resp == loads(resp)
