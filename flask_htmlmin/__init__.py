from functools import wraps
from htmlmin import Minifier
from flask import request, current_app
import warnings
import cssmin
import re


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

        self.disable_css_min = kwargs.get('disable_css_min', False)
        default_options.update(kwargs)
        self.opts = default_options

        self._exempt_routes = set()
        self._html_minify = Minifier(
            **default_options)

    def init_app(self, app):
        app.config.setdefault('MINIFY_HTML', False)

        if 'MINIFY_PAGE' in app.config:
            app.config['MINIFY_HTML'] = app.config['MINIFY_PAGE']
            warnings.warn(
                'MINIFY_PAGE is deprecated, use MINIFY_HTML instead',
                DeprecationWarning,
                stacklevel=2
            )

        if app.config['MINIFY_HTML']:
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
            if self.disable_css_min:
                response.set_data(
                    self._html_minify.minify(response.get_data(as_text=True))
                )
            else:
                response.set_data(
                    self._css_minify(
                      self._html_minify.minify(
                           response.get_data(as_text=True)
                       )
                     )
                )

            return response
        return response

    def _css_minify(self, response):
        """
            Minify inline css
        """

        # Minify internal css
        out = ''
        text = response
        opening_tags = re.findall(r"<style\s*[^>]*>", text, re.M | re.I)
        for tag in opening_tags:
            i = text.find(tag)+len(tag)-1
            e = text.find("</style>")+9
            css = text[i:e]
            out += text[0:i] + self._min_css(css)
            text = text[e:]
        out = out+text

        # Minify inline css
        out2 = ''
        inlines = re.findall(r"<[A-Za-z0-9-]+[^>]+?style=\"[\s\S]+?\"",
                             out,  re.M | re.I)
        for inline in inlines:
            i = out.find(inline)
            j = out[i:].find("style=")+7
            k = out[i+j:].find('"')
            css = out[i+j:i+j+k+1]
            out2 += out[0:i+j] + re.sub(r";+\s*(?=(\"|\'))", "",
                                        self._min_css(css), re.I | re.M)
            out = out[i+j+k+1:]
        out2 += out
        return out2

    def _min_css(self, css):
        if self.opts.get("remove_comments"):
            css = cssmin.remove_comments(css)
        css = cssmin.condense_whitespace(css)
        css = css.replace('"\\"}\\""', "___PSEUDOCLASSBMH___")
        css = cssmin.remove_unnecessary_whitespace(css)
        css = cssmin.remove_unnecessary_semicolons(css)
        css = cssmin.condense_zero_units(css)
        css = cssmin.condense_multidimensional_zeros(css)
        css = cssmin.condense_floating_points(css)
        css = cssmin.normalize_rgb_colors_to_hex(css)
        css = cssmin.condense_hex_colors(css)
        return css

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
