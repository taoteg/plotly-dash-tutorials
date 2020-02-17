import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

"""
Multiple Outputs

 - New in dash 0.39.0

So far all the callbacks we've written only update a single Output property.

We can also update several at once: put all the properties you want to update as
a list in the decorator, and return that many items from the callback.

This is particularly nice if two outputs depend on the same computationally
intense intermediate result, such as a slow database query.

A word of caution: it's not always a good idea to combine Outputs, even if you can:

- If the Outputs depend on some but not all of the same Inputs, keeping them
  separate can avoid unnecessary updates.

- If they have the same Inputs but do independent computations with these inputs,
  keeping the callbacks separate can allow them to run in parallel.
"""

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(
        id='num-multi',
        type='number',
        value=5
    ),
    html.Table([
        # Added html.Tbody and html.Tr([html.Th]) lines to make component tree compiant.
        html.Tbody([
            html.Tr([html.Th(['Formula']), html.Th('Value')]),
            html.Tr([html.Td(['x', html.Sup(2)]), html.Td(id='square')]),
            html.Tr([html.Td(['x', html.Sup(3)]), html.Td(id='cube')]),
            html.Tr([html.Td([2, html.Sup('x')]), html.Td(id='twos')]),
            html.Tr([html.Td([3, html.Sup('x')]), html.Td(id='threes')]),
            html.Tr([html.Td(['x', html.Sup('x')]), html.Td(id='x^x')])
        ])
    ]),
])


@app.callback(
    [Output('square', 'children'),
     Output('cube', 'children'),
     Output('twos', 'children'),
     Output('threes', 'children'),
     Output('x^x', 'children')],
    [Input('num-multi', 'value')])
def callback_a(x):
    return x**2, x**3, 2**x, 3**x, x**x


if __name__ == '__main__':
    app.run_server(debug=True)
