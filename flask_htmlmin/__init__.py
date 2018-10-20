from functools import wraps
from htmlmin import Minifier
from flask import request, current_app


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

        self._exempt_routes = set()
        self._html_minify = Minifier(
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
            endpoint = request.endpoint or ''
            view_func = current_app.view_functions.get(endpoint, None)
            name = (
                '%s.%s' % (view_func.__module__, view_func.__name__)
                if view_func else ''
            )
            if name in self._exempt_routes:
                return response

            response.direct_passthrough = False
            response.set_data(
                self._html_minify.minify(response.get_data(as_text=True))
            )

            return response
        return response

    def exempt(self, obj):
        """
        decorator to mark a view as exempt from htmlmin.
        """
        name = '%s.%s' % (obj.__module__, obj.__name__)

        @wraps(obj)
        def __inner(*a, **k):
            return obj(*a, **k)

        self._exempt_routes.add(name)
        return __inner
