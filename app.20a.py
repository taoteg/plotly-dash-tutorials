# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
from dash.dependencies import Input, Output


"""
Sharing Data Between Callbacks

In order to share data safely across multiple python processes, we need to store
the data somewhere that is accessible to each of the processes.

There are three main places to store this data:

    1 - In the user's browser session
    2 - On the disk (e.g. on a file or on a new database)
    3 - In a shared memory space like with Redis

The following three examples illustrate these approaches.
"""

"""
Example 1 - Storing Data in the Browser with a Hidden Div

To save data in user's browser's session:

    - Implemented by saving the data as part of Dash's front-end store through
      methods explained in https://community.plot.ly/t/sharing-a-dataframe-between-plots/6173
    - Data has to be converted to a string like JSON for storage and transport
    - Data that is cached in this way will only be available in the user's current session.
        -- If you open up a new browser, the app's callbacks will always compute the data.
           The data is only cached and transported between callbacks within the session.
        -- As such, unlike with caching, this method doesn't increase the memory footprint of the app.
        -- There could be a cost in network transport. If you're sharing 10MB of data between callbacks,
           then that data will be transported over the network between each callback.
        -- If the network cost is too high, then compute the aggregations upfront and transport those.
           Your app likely won't be displaying 10MB of data, it will just be displaying a subset or an aggregation of it.

This example outlines how you can perform an expensive data processing step in one callback, serialize the output at JSON,
and provide it as an input to the other callbacks. This example uses standard Dash callbacks and stores the JSON-ified data
inside a hidden div in the app.
"""

# Example 1 - Storing Data in the Browser with a Hidden Div

global_df = pd.read_csv('data.csv')

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='graph'),
    html.Table(id='table'),
    dcc.Dropdown(id='dropdown'),

    # Hidden div inside the app that stores the intermediate value
    html.Div(id='intermediate-value', style={'display': 'none'})
])

@app.callback(Output('intermediate-value', 'children'), [Input('dropdown', 'value')])
def clean_data(value):
     # some expensive clean data step
     cleaned_df = your_expensive_clean_or_compute_step(value)

     # more generally, this line would be
     # json.dumps(cleaned_df)
     return cleaned_df.to_json(date_format='iso', orient='split')

@app.callback(Output('graph', 'figure'), [Input('intermediate-value', 'children')])
def update_graph(jsonified_cleaned_data):

    # more generally, this line would be
    # json.loads(jsonified_cleaned_data)
    dff = pd.read_json(jsonified_cleaned_data, orient='split')

    figure = create_figure(dff)
    return figure

@app.callback(Output('table', 'children'), [Input('intermediate-value', 'children')])
def update_table(jsonified_cleaned_data):
    dff = pd.read_json(jsonified_cleaned_data, orient='split')
    table = create_table(dff)
    return table
