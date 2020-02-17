# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

"""
Dash State (continued)

dash.dependencies.State allows you to pass along extra values without firing the
callbacks.

Here's the same example as above but with the dcc.Input as
dash.dependencies.State and a button as dash.dependencies.Input.

In this example, changing text in the dcc.Input boxes won't fire the callback
but clicking on the button will. The current values of the dcc.Input values are
still passed into the callback even though they don't trigger the callback function itself.

Note that we're triggering the callback by listening to the n_clicks property of
the html.Button component. n_clicks is a property that gets incremented every time
the component has been clicked on.

It is available in every component in the dash_html_components library.
"""

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(id='input-1-state', type='text', value='Montréal'),
    dcc.Input(id='input-2-state', type='text', value='Canada'),
    html.Button(id='submit-button', n_clicks=0, children='Submit'),
    html.Div(id='output-state')
])


@app.callback(Output('output-state', 'children'),
              [Input('submit-button', 'n_clicks')],
              [State('input-1-state', 'value'),
               State('input-2-state', 'value')])
def update_output(n_clicks, input1, input2):
    return u'''
        The Button has been pressed {} times,
        Input 1 is "{}",
        and Input 2 is "{}"
    '''.format(n_clicks, input1, input2)


if __name__ == '__main__':
    app.run_server(debug=True)
