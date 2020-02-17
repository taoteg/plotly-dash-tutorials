# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

"""
Basic Plotly Dash App.

- The layout is composed of a tree of "components" like html.Div and dcc.Graph.

- The dash_html_components library has a component for every HTML tag.
  The html.H1(children='Hello Dash') component generates a <h1>Hello Dash</h1>
  HTML element in your application.

- Not all components are pure HTML. The dash_core_components describe higher-level
  components that are interactive
  and are generated with JavaScript, HTML, and CSS through the React.js library.

- Each component is described entirely through keyword attributes. Dash is declarative:
  you will primarily describe your application through these attributes.

- The children property is special. By convention, it's always the first attribute
  which means that you can omit it: html.H1(children='Hello Dash') is the same as
  html.H1('Hello Dash'). Also, it can contain a string, a number, a single component,
  or a list of components.

- The fonts in your application will look a little bit different than what is displayed here.
  This application is using a custom CSS stylesheet to modify the default styles of the elements.

You can learn more in the css tutorial, but for now you can initialize your app with:
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
to get the same look and feel of these examples.
"""

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Presenting Dash'),

    html.Div(children='''Dash: A web application framework for Python.'''),

    dcc.Graph(
        id='example-01',
        figure={
            'data': [
                {'x': [3, 6, 9], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 8, 13], 'y': [7, 4, 5],
                    'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
