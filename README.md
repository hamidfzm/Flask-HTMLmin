Flask-HTMLmin
=============

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

    from flask import Flask, render_template
    from flask.ext_htmlmin import HTMLMIN
    
    app = Flask(__name__)
    app.config['MINIFY_PAGE'] = True
    
    HTMLMIN(app)
    # or you can use HTMLMIN.init_app(app)
    
    @app.route('/')
    def main():
        # index.html will be minimized !!!
        return render_template('index.html')
    
    if __name__ == '__main__':
        app.run()
