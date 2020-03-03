# -*- coding: utf-8 -*-

"""
Adding CSS & JS and Overriding the Page-Load Template

Dash applications are rendered in the web browser with CSS and JavaScript. On
page load, Dash serves a small HTML template that includes references to the
CSS and JavaScript that are required to render the application. This chapter
covers everything that you need to know about configuring this HTML file and
about including external CSS and JavaScript in Dash applications.


Customizing Dash's HTML Index Template

New in dash 0.22.0

Dash's UI is generated dynamically with Dash's React.js front-end. So, on page l
oad, Dash serves a very small HTML template string that includes the CSS and
JavaScript that is necessary to render the page and some simple HTML meta tags.

This simple HTML string is customizable. You might want to customize this string
if you wanted to:

- Include a different <title> for your app (the <title> tag is the name that
    appears in your brower's tab. By default, it is "Dash")

- Customize the way that your CSS or JavaScript is included in the page. For
    example, if you wanted to include remote scripts or if you wanted to include
    the CSS before the Dash component CSS

- Include custom meta tags in your app. Note that meta tags can also be added
    with the meta_tags argument (example below).

- Include a custom version of dash-renderer, by instantiating the DashRenderer
    class yourself. You can add request hooks this way, by providing a hooks
    config object as in the example below.

OPTION 2

Option 2 - interpolate_index

If your HTML content isn't static or if you would like to introspect or modify
the templated variables, then you can override the Dash.interpolate_index method.

Unlike the index_string method, where we worked with template string variables,
the keyword variables that are passed into interpolate_index are already
evaluated.

In the example above, when we print the input arguments of interpolate_index we
should see an output like this:

{
    'title': 'Dash',
    'app_entry': '\n<div id="react-entry-point">\n    <div class="_dash-loading">\n        Loading...\n    </div>\n</div>\n',
    'favicon': '',
    'metas': '<meta charset="UTF-8"/>',
    'scripts': '<script src="https://unpkg.com/react@15.4.2/dist/react.min.js"></script>\n<script src="https://unpkg.com/react-dom@15.4.2/dist/react-dom.min.js"></script>\n<script src="https://unpkg.com/dash-html-components@0.14.0/dash_html_components/bundle.js"></script>\n<script src="https://unpkg.com/dash-renderer@0.20.0/dash_renderer/bundle.js"></script>',
    'renderer': '<script id="_dash-renderer" type="application/javascript">var renderer = new DashRenderer();</script>',
    'config': '<script id="_dash-config" type="application/json">{"requests_pathname_prefix": "/", "url_base_pathname": "/"}</script>',
    'css': ''
}

The values of the scripts and css keys may be different depending on which
component libraries you have included or which files might be in your assets
folder.

"""

import dash
import dash_html_components as html


class CustomDash(dash.Dash):
    def interpolate_index(self, **kwargs):

        # Inspect the arguments by printing them
        # print(kwargs)

        for key, value in kwargs.items():
            print("--- {} = {} \n".format(key, value))

        return '''
        <!DOCTYPE html>
        <html>
            <head>
                <title>My App</title>
            </head>
            <body>

                <div id="custom-header">My custom header</div>
                {app_entry}
                {config}
                {scripts}
                {renderer}
                <div id="custom-footer">My custom footer</div>
            </body>
        </html>
        '''.format(
            app_entry=kwargs['app_entry'],
            config=kwargs['config'],
            scripts=kwargs['scripts'],
            renderer=kwargs['renderer'])

app = CustomDash()

app.layout = html.Div('Simple Dash App - Custom Template 2')

if __name__ == '__main__':
    app.run_server(debug=True)
