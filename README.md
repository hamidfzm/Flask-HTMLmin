
Flask-HTMLmin
=============
[![Build Status](https://travis-ci.org/hamidfzm/Flask-HTMLmin.svg?branch=master)](https://travis-ci.org/hamidfzm/Flask-HTMLmin)
[![Coverage Status](https://coveralls.io/repos/github/hamidfzm/Flask-HTMLmin/badge.svg?branch=master)](https://coveralls.io/github/hamidfzm/Flask-HTMLmin?branch=master)

Minify flask `text/html` mime types responses.
Just add `MINIFY_PAGE = True` to your deployment config to minify html and text responses of your flask application.


Installation
------------
To install Flask-HTMLmin, simply:

    pip install Flask-HTMLmin

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
    
    HTMLMIN(app)
    # or you can use HTMLMIN.init_app(app)
    # pass additional parameters to htmlmin
    # HTMLMIN(app, **kwargs)
    
    @app.route('/')
    def main():
        # index.html will be minimized !!!
        return render_template('index.html')
    
    if __name__ == '__main__':
        app.run()
```

TODO
----
- [x] Test cases
- [ ] Route (or URL rule) exemption
- [ ] Caching
- [ ] Minify inline CSS
- [ ] Minify inline Javascript
