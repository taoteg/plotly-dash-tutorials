# -*- coding: utf-8 -*-

"""
Multi-Page Apps and URL Support

Dash renders web applications as a "single-page app".
This means that the application does not completely reload when the user
navigates the application, making browsing very fast.

There are two new components that aid page navigation:
`dash_core_components.Location` and `dash_core_components.Link`.

dash_core_components.Location represents the location bar in your web browser
through the pathname property.

This is a simple example.

In this example, the callback display_page receives the current pathname (the
last part of the URL) of the page. The callback simply displays the pathname
on page but it could use the pathname to display different content.

The Link element updates the pathname of the browser without refreshing the
page. If you used a html.A element instead, the pathname would update but the
page would refresh.

Note how clicking on the Link doesn't refresh the page even though it
updates the URL!
"""

import dash
import dash_core_components as dcc
import dash_html_components as html

print(dcc.__version__) # 0.6.0 or above is required

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    # represents the URL bar, doesn't render anything
    dcc.Location(id='url', refresh=False),

    dcc.Link('Navigate to "/"', href='/'),
    html.Br(),
    dcc.Link('Navigate to "/page-2"', href='/page-2'),

    # content will be rendered in this element
    html.Div(id='page-content')
])


@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    return html.Div([
        html.H3('You are on page {}'.format(pathname)),
        html.Br(),
        html.H4(html.I('...same page, different content'))
    ])


if __name__ == '__main__':
    app.run_server(debug=True)
