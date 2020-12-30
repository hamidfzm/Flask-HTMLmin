
Flask-HTMLmin
=============
[![PyPI version](https://badge.fury.io/py/Flask-HTMLmin.svg)](https://badge.fury.io/py/Flask-HTMLmin)
![Supported Python Versions](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8-blue.svg)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-orange.svg)](LICENSE)
![tests](https://github.com/hamidfzm/Flask-HTMLmin/workflows/tests/badge.svg)
[![codecov](https://codecov.io/gh/hamidfzm/Flask-HTMLmin/branch/master/graph/badge.svg)](https://codecov.io/gh/hamidfzm/Flask-HTMLmin)

Minify flask `text/html` mime type responses.
Just add `MINIFY_HTML = True` to your deployment config to minify HTML and text responses of your flask application.


Installation
------------
To install Flask-HTMLmin, simply:

    pip install Flask-HTMLmin

Or use pipenv (recommended):

    pipenv install Flask-HTMLmin

Or alternatively, you can download the repository and install manually by doing:

    git clone git@github.com:hamidfzm/Flask-HTMLmin.git
    cd Flask-HTMLmin
    python setup.py install


Example
-------
```python
from flask import Flask, render_template
from flask_htmlmin import HTMLMIN
    
app = Flask(__name__)
app.config['MINIFY_HTML'] = True

htmlmin = HTMLMIN(app)
# or you can use HTMLMIN.init_app(app)
# pass additional parameters to htmlmin
# HTMLMIN(app, **kwargs)
# example:
# htmlmin = HTMLMIN(app, remove_comments=False, remove_empty_space=True)


@app.route('/')
def main():
    # index.html will be minimized !!!
    return render_template('index.html')


@app.route('/exempt')
@htmlmin.exempt
def exempted_route():
    # index.html will be exempted and not blessed by holy htmlmin !!!
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
```

TODO
----
- [x] Test cases
- [x] Route (or URL rule) exemption
- [x] Caching (in progress)
- [ ] Minify inline CSS
- [ ] Minify inline Javascript
