# -*- coding: utf-8 -*-

"""
Adding CSS & JS and Overriding the Page-Load Template

Dash applications are rendered in the web browser with CSS and JavaScript. On
page load, Dash serves a small HTML template that includes references to the
CSS and JavaScript that are required to render the application. This chapter
covers everything that you need to know about configuring this HTML file and
about including external CSS and JavaScript in Dash applications.

Serving Dash's Component Libraries Locally or from a CDN

Changed in Dash 1.0.0 - now serve_locally defaults to True, previously it
defaulted to False

Dash's component libraries, like dash_core_components and dash_html_components,
are bundled with JavaScript and CSS files. Dash automatically checks with
component libraries are being used in your application and will automatically
serve these files in order to render the application.

By default, dash serves the JavaScript and CSS resources from the local files on
the server where Dash is running. This is the more flexible and robust option:
in some cases, such as firewalled or airgapped environments, it is the only
option. It also avoids some hard-to-debug problems like packages that have not
been published to NPM or CDN downtime, and the unlikely but possible scenario of
the CDN being hacked. And of course, component developers will want the local
version while changing the code, so when dev bundles are requested (such as with
debug=True) we always serve locally.

However, for performance-critical apps served beyond an intranet, online CDNs
can often deliver these files much faster than loading the resources from the
file system, and will reduce the load on the Dash server.

Here's how to enable CDN serving. app.scripts is the most important one, that
controls the JavaScript files, but app.css can sometimes help too.
"""

import dash
import dash_core_components as dcc
import dash_html_components as html


#####################
# Version 3.
# External Resources.
# external JavaScript files
external_scripts = [
    'https://www.google-analytics.com/analytics.js',
    {'src': 'https://cdn.polyfill.io/v2/polyfill.min.js'},
    {
        'src': 'https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.10/lodash.core.js',
        'integrity': 'sha256-Qqd/EfdABZUcAxjOkMi8eGEivtdTkh3b65xCZL4qAQA=',
        'crossorigin': 'anonymous'
    }
]

# external CSS stylesheets
external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }
]

app = dash.Dash(__name__,
                external_scripts=external_scripts,
                external_stylesheets=external_stylesheets)

#  Disable serving local files.
app.css.config.serve_locally = False
app.scripts.config.serve_locally = False
# NOTE: These settings will be overridden by dev bundle requests if
# app.run_server(debug=True).

#####################
#  Layout

app.layout = html.Div([
    html.Div(
        className="app-header",
        children=[
            html.Div('Plotly Dash', className="app-header--title")
        ]
    ),
    html.Div(
        children=html.Div([
            html.H5('Overview'),
            html.Div('''
                This is an example of a simple Dash app with
                local, customized CSS.
            '''),
            html.Br(),
            html.Img(src='/assets/manhattan.jpg')
        ])
    )
])

if __name__ == '__main__':
    app.run_server(debug=False)    # will override the serve_locally setting.
