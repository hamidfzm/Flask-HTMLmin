import logging
from htmlmin import Minifier
from htmlmin.parser import OpenTagNotFoundError

__author__ = 'Hamid FzM'


class HTMLMIN(object):
    def __init__(self, app=None, **kwargs):
        self.app = app
        if app is not None:
            self.init_app(app)

        default_options = {
            'remove_comments': True,
            'reduce_empty_attributes': True,
            'remove_optional_attribute_quotes': False
        }
        default_options.update(kwargs)

        self.html_minify = Minifier(
            **default_options)

    def init_app(self, app):
        app.config.setdefault('MINIFY_PAGE', False)

        if app.config['MINIFY_PAGE']:
            app.after_request(self.response_minify)

    def response_minify(self, response):
        """
        minify response html to decrease traffic
        """
        if response.content_type == u'text/html; charset=utf-8':
            response.direct_passthrough = False
            data = response.get_data(as_text=True)
            try:
                minified = self.html_minify.minify(data)
            except OpenTagNotFoundError:
                minified = data
                logging.error('Could not minify data: OpenTagNotFoundError')
            response.set_data(minified)

            return response
        return response
