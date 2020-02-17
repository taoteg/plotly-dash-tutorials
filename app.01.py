# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

"""
Basic Plotly Dash Example App.
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
