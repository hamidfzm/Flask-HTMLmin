"""Flask-HTMLmin."""

from htmlmin.main import minify

__author__ = 'Hamid FzM'


class HTMLMIN(object):
    """Minify flask text/html mime types responses."""

    def __init__(self, app=None, options=None):
        self.app = app
        self.options = {
            'remove_comments': True,
            'reduce_empty_attributes': True,
            'remove_optional_attribute_quotes': False
            }
        if options:
            self.options.update(options)
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """Initialize onto app."""
        app.config.setdefault('MINIFY_PAGE', False)

        if app.config['MINIFY_PAGE']:
            app.after_request(self.response_minify)

    def response_minify(self, response):
        """
        minify response html to decrease traffic
        """
        if response.content_type == u'text/html; charset=utf-8':
            response.direct_passthrough = False
            response.set_data(
                minify(response.get_data(as_text=True),
                       **self.options)
            )

            return response
        return response
