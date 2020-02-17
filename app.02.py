# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

"""
In this example, we modified the inline styles of the html.Div and html.H1 components with the style property.

html.H1('Hello Dash', style={'textAlign': 'center', 'color': '#ac99dc'}) is rendered in the Dash application as <h1 style="text-align: center; color: #ac99dc">Hello Dash</h1>.

There are a few important differences between the dash_html_components and the HTML attributes:

    - The style property in HTML is a semicolon-separated string. In Dash, you can just supply a dictionary.
    - The keys in the style dictionary are camelCased. So, instead of text-align, it's textAlign.
    - The HTML class attribute is className in Dash.
    - The children of the HTML tag is specified through the children keyword argument.
      By convention, this is always the first argument and so it is often omitted.
"""

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Adding some custom inline styles.
colors = {
    'background': '#111111',
    'text': '#ac99dc'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Presenting Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-02',
        figure={
            'data': [
                {'x': [3, 6, 9], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 8, 13], 'y': [7, 4, 5],
                    'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization',
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
