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

OPTION 1

The {%key%}s are template variables that Dash will fill in automatically with
default properties.

The available keys are:

{%metas%} (optional)

The registered meta tags included by the meta_tags argument in dash.Dash

{%favicon%} (optional)

A favicon link tag if found in the assets folder.

{%css%} (optional)

<link/> tags to css resources. These resources include the Dash component
library CSS resources as well as any CSS resources found in the assets folder.

{%title%} (optional)

The contents of the page <title> tag. Learn more about <title/>

{%config%} (required)

An auto-generated tag that includes configuration settings passed from Dash's
backend to Dash's front-end (dash-renderer).

{%app_entry%} (required)

The container in which the Dash layout is rendered.

{%scripts%} (required)

The set of JavaScript scripts required to render the Dash app. This includes the
Dash component JavaScript files as well as any JavaScript files found in the
assets folder.

{%renderer%} (required)

The JavaScript script that instantiates dash-renderer by calling new
DashRenderer()

"""

import dash
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        <div>My Custom header</div>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
        <div>My Custom footer</div>
    </body>
</html>
'''

app.layout = html.Div('Simple Dash App - Custom Template 1')

if __name__ == '__main__':
    app.run_server(debug=True)
