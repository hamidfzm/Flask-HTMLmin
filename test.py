from json import loads

from flask import Flask, jsonify
from pytest import fixture

from flask_htmlmin import HTMLMIN

app = Flask(__name__)
app.config['TESTING'] = True
app.config['MINIFY_PAGE'] = True
htmlmin = HTMLMIN(app=app)

json_resp = dict(
    resp='some unminified json response'
)

html_resp = '''<html>
            <style>
             .h {
               width: 3em
              } 
           </style>
            <body>
                <h1 style="width: 3em;;">
                    HTML
                </h1>
            </body>
        </html>'''


@app.route('/')
def html():
    return html_resp


@app.route('/json')
def json():
    return jsonify(json_resp)


@app.route('/exempt')
@htmlmin.exempt
def exempt():
    return html_resp


@fixture
def client():
    client = app.test_client()
    yield client


def test_html_minify(client):
    """ testing HTML minified response """
    resp = client.get('/').data
    print(resp)
    assert b'<html> <style>.h{width:3em}</style><body> <h1 style="width:3em"> HTML </h1> </body> </html>' == resp


def test_json_unminifed(client):
    """ testing unminified Json response """
    resp = client.get('/json').data
    assert json_resp == loads(resp)


def test_exempt_routes(client):
    """ testing exempt routes """
    resp = client.get('/exempt').data

    assert resp == html_resp.encode()
