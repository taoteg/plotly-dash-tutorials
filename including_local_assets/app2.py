# -*- coding: utf-8 -*-

"""
Adding CSS & JS and Overriding the Page-Load Template

Dash applications are rendered in the web browser with CSS and JavaScript. On
page load, Dash serves a small HTML template that includes references to the
CSS and JavaScript that are required to render the application. This chapter
covers everything that you need to know about configuring this HTML file and
about including external CSS and JavaScript in Dash applications.

Adding Your Own CSS and JavaScript to Dash Apps

New in dash 0.22.0

Including custom CSS or JavaScript in your Dash apps is simple. Just create a
folder named assets in the root of your app directory and include your CSS and
JavaScript files in that folder. Dash will automatically serve all of the files
that are included in this folder. By default the url to request the assets will
be /assets but you can customize this with the assets_url_path argument to
dash.Dash.

Important: For these examples, you need to include __name__ in your
Dash constructor.

That is, app = dash.Dash(__name__) instead of app = dash.Dash().

Here's why -->

    "We use flask.helpers.get_root_path which take a module name to resolves
    the path to the module. By default, we have __main__ as the module name for
    a fallback that will work when the app is called by it’s module name
    (eg: python app.py).

    When you run it thru some other command line (like the flask command or
    gunicorn/waitress) the __main__ module is no longer located where app.py
    is and now refer to some place like /venv/lib/site-packages/flask. Giving
    __name__ explicitly will always give the right path to the assets folder."

   https://community.plot.ly/t/dash-app-does-not-load-assets-and-app-index-string/12178/10?u=chriddyp&_ga=2.80337623.1773320274.1583169999-1206103131.1583169999


There are a few things to keep in mind when including assets automatically:

1 - The following file types will automatically be included:

    A - CSS files suffixed with .css
    B - JavaScript files suffixed with .js
    C - A single file named favicon.ico (the page tab's icon)

2 - Dash will include the files in alphanumerical order by filename. So, we
recommend prefixing your filenames with numbers if you need to ensure their
order (e.g. 10_typography.css, 20_header.css)

3 - You can ignore certain files in your assets folder with a regex filter
using app = dash.Dash(assets_ignore='.*ignored.*'). This will prevent Dash
from loading files which contain the above pattern.

4 - If you want to include CSS from a remote URL, then see the next section.

5 - Your custom CSS will be included after the Dash component CSS

6 - It is recommended to add __name__ to the dash init to ensure the resources
in the assets folder are loaded, eg: app = dash.Dash(__name__,
meta_tags=[...]). When you run your application through some other command line
(like the flask command or gunicorn/waitress), the __main__ module will no
longer be located where app.py is. By explicitly setting __name__, Dash will
be able to locate the relative assets folder correctly.


Example: Including Local CSS and JavaScript

We'll create several files: app.py, a folder named assets, and three files in
that folder:

    - app.py
    - assets/
        |-- typography.css
        |-- header.css
        |-- custom-script.js


Hot Reloading

By default, Dash includes "hot-reloading". This means that Dash will
automatically refresh your browser when you make a change in your Python code
and your CSS code.

Load Assets from a Folder Hosted on a CDN

If you duplicate the file structure of your local assets folder to a folder
hosted externally to your Dash app, you can use
assets_external_path='http://your-external-assets-folder-url' in the Dash
constructor to load the files from there instead of locally. Dash will index
your local assets folder to find all of your assets, map their relative path
onto assets_external_path and then request the resources from there.
app.scripts.config.serve_locally = False must also be set in order for this to
work.

NOTE: In Dash 0.43.0 and before, app.scripts.config.serve_locally = False was
the default, except when dev bundles are served (such as during debugging).
Starting with Dash 1.0.0, serve_locally defaults to True.

Embedding Images in Your Dash Apps

In addition to CSS and javascript files, you can include images in the assets
folder. An example of the folder structure:

- app.py
- assets/
    |-- image.png


Adding external CSS/Javascript

You can add resources hosted externally to your Dash app with the
external_stylesheets/stylesheets init keywords.

The resources can be either a string or a dict containing the tag attributes
(src, integrity, crossorigin, etc). You can mix both.

External css/js files are loaded before the assets.

RESUME HERE : https://dash.plot.ly/external-resources
>>>>>>> Customizing Dash's HTML Index Template <<<<<<<<

"""

import dash
import dash_core_components as dcc
import dash_html_components as html

#####################
# Version 2.
#  Using a CDN.

app = dash.Dash(
    __name__,
    assets_external_path='http://your-external-assets-folder-url/'
)
app.scripts.config.serve_locally = False

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
    app.run_server(debug=True)
