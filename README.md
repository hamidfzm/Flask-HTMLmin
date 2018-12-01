
Flask-HTMLmin
=============
[![PyPi Package](https://img.shields.io/badge/pypi-v1.5.0-blue.svg)](https://pypi.org/project/Flask-HTMLmin/)
![Supported Python Versions](https://img.shields.io/badge/python-2.7%20%7C%203.6%20%7C%203.7-blue.svg)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-orange.svg)](LICENSE)
[![Build Status](https://travis-ci.org/hamidfzm/Flask-HTMLmin.svg?branch=master)](https://travis-ci.org/hamidfzm/Flask-HTMLmin)
[![Coverage Status](https://coveralls.io/repos/github/hamidfzm/Flask-HTMLmin/badge.svg?branch=master)](https://coveralls.io/github/hamidfzm/Flask-HTMLmin?branch=master)

Minify flask `text/html` mime type responses.
Just add `MINIFY_PAGE = True` to your deployment config to minify HTML and text responses of your flask application.


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
app.config['MINIFY_PAGE'] = True

htmlmin = HTMLMIN(app)
# or you can use HTMLMIN.init_app(app)
# pass additional parameters to htmlmin
# HTMLMIN(app, **kwargs)

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
- [ ] Caching
- [ ] Minify inline CSS
- [ ] Minify inline Javascript
