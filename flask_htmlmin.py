__author__ = 'Hamid FzM'

from htmlmin.main import minify


class HTMLMIN(object):

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('MINIFY_PAGE', False)

        if app.config['MINIFY_PAGE']:
            app.after_request(self.response_minify)

    def response_minify(self, response):
        """
        minify response html to decrease traffic
        """
        if response.content_type == u'text/html; charset=utf-8':
            response.set_data(
                minify(response.get_data(as_text=True),
                       remove_comments=True)
            )

            return response
        return response