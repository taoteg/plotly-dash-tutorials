# -*- coding: utf-8 -*-

"""
Adding CSS & JS and Overriding the Page-Load Template

Dash applications are rendered in the web browser with CSS and JavaScript. On
page load, Dash serves a small HTML template that includes references to the
CSS and JavaScript that are required to render the application. This chapter
covers everything that you need to know about configuring this HTML file and
about including external CSS and JavaScript in Dash applications.


Customizing dash-renderer with request hooks v1.

To instantiate your own version of dash-renderer, you can override Dash's HTML
Index Template and provide your own script that will be used instead of the
standard script. This script should somewhere call:

    var renderer = new DashRenderer();

which instantiates the DashRenderer class. You can add this script to your index
HTML when you're setting app.index_string, or you could simply override
app.renderer like this example.
"""

import dash
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# app.index_string = '''
# <!DOCTYPE html>
# <html>
#     <head>
#         {%metas%}
#         <title>{%title%}</title>
#         {%favicon%}
#         {%css%}
#     </head>
#     <body>
#         <div>My Custom header</div>
#         {%app_entry%}
#         <footer>
#             {%config%}
#             {%scripts%}
#             {%renderer%}
#         </footer>
#         <div>My Custom footer</div>
#     </body>
# </html>
# '''

app.renderer = 'var renderer = new DashRenderer();'

app.layout = html.Div('Simple Dash App - Custom Template 3')

if __name__ == '__main__':
    app.run_server(debug=True)
