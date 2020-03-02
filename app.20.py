# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
from dash.dependencies import Input, Output

#  NOTE: This is not an executable script, only partial code examples.

"""
PART 6A: Sharing State Between Callbacks

One of the core Dash principles explained in the Getting Started Guide on Callbacks
is that Dash Callbacks must never modify variables outside of their scope.
It is not safe to modify any global variables.

Why Share State?

In some apps, you may have multiple callbacks that depend on expensive data
processing tasks like making SQL queries, running simulations, or downloading data.

Rather than have each callback run the same expensive task, you can have one callback
run the task and then share the results to the rest of the callbacks.

This need has been somewhat ameliorated now that you can have multiple outputs for
one callback. This way, that expensive task can be done once and immediately used
in all the outputs.

But in some cases this still isn't ideal, for example if there are simple follow-on
tasks that modify the results, like unit conversions. We shouldn't need to repeat a
large database query just to change the results from Fahrenheit to Celsius!

Why global variables will break your app!

Dash is designed to work in multi-user environments where multiple people may view
the application at the same time and will have independent sessions.

If your app uses modified global variables, then one user's session could set the
variable to one value which would affect the next user's session.

Dash is also designed to be able to run with multiple python workers so that callbacks
can be executed in parallel. This is commonly done with gunicorn using syntax like:

    $ gunicorn --workers 4 app:server

    (app refers to a file named app.py and server refers to
    a variable in that file named server: server = app.server).

When Dash apps run across multiple workers, their memory is not shared.
This means that if you modify a global variable in one callback, that modification
will not be applied to the rest of the workers.
"""

# Here is a sketch of an app with a callback that modifies data out of its scope.
# This type of pattern *will not work reliably* for the reasons outlined above.

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app = dash.Dash(__name__)

df = pd.DataFrame({
    'a': [1, 2, 3],
    'b': [4, 1, 4],
    'c': ['x', 'y', 'z'],
})

app.layout = html.Div([
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in df['c'].unique()],
        value='a'
    ),
    html.Div(id='output'),
])

@app.callback(Output('output', 'children'),
              [Input('dropdown', 'value')])
def update_output_1(value):
    #  INCORRECT
    # Here, `df` is an example of a variable that is
    # "outside the scope of this function".
    # *It is not safe to modify or reassign this variable
    #  inside this callback.*
    # global df = df[df['c'] == value]  # do not do this, this is not safe!
    # return len(value)

    #  CORRECT
    # To fix this example, simply re-assign the filter to a new variable inside the callback,
    # or follow one of the strategies outlined in the next part of this guide.
    # Safely reassign the filter to a new variable
    filtered_df = df[df['c'] == value]  # do this instead.
    print(filtered_df)
    return len(filtered_df)
