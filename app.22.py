# -*- coding: utf-8 -*-

"""
PART 6C: Sharing State Between Callbacks

Example 4 - User-Based Session Data on the Server

The previous example cached computations on the filesystem and those
computations were accessible for all users.

In some cases, you want to keep the data isolated to user sessions:
one user's derived data shouldn't update the next user's derived data.

One way to do this is to save the data in a hidden Div, as demonstrated
in the first example.

Another way to do this is to save the data on the filesystem cache with a
session ID and then reference the data using that session ID. Because data is
saved on the server instead of transported over the network, this method is
generally faster than the "hidden div" method.

This example was originally discussed in a Dash Community Forum thread.

This example:

    - Caches data using the flask_caching filesystem cache. You can also save
      to an in-memory database like Redis.
    - Serializes the data as JSON.
        -- If you are using Pandas, consider serializing with Apache Arrow.
    - Saves session data up to the number of expected concurrent users.
      This prevents the cache from being overfilled with data.
    - Creates unique session IDs by embedding a hidden random string into the
      app's layout and serving a unique layout on every page load.

    Note: As with all examples that send data to the client, be aware that these
    sessions aren't necessarily secure or encrypted. These session IDs may be
    vulnerable to Session Fixation style attacks.

Here's what this example looks like in code.

There are three things to notice in this example:

    - The timestamps of the dataframe don't update when we retrieve the data.
      This data is cached as part of the user's session.
    - Retrieving the data initially takes five seconds but successive queries
      are instant, as the data has been cached.
    - The second session displays different data than the first session: the
      data that is shared between callbacks is isolated to individual user sessions.
"""

# Example 4 - User-Based Session Data on the Server

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import datetime
from flask_caching import Cache
import os
import pandas as pd
import time
import uuid

external_stylesheets = [
    # Dash CSS
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    # Loading screen CSS
    'https://codepen.io/chriddyp/pen/brPBPO.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
cache = Cache(app.server, config={
    'CACHE_TYPE': 'redis',
    # Note that filesystem cache doesn't work on systems with ephemeral
    # filesystems like Heroku.
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory',

    # should be equal to maximum number of users on the app at a single time
    # higher numbers will store more data in the filesystem / redis cache
    'CACHE_THRESHOLD': 200
})


def get_dataframe(session_id):
    @cache.memoize()
    def query_and_serialize_data(session_id):
        # expensive or user/session-unique data processing step goes here

        # simulate a user/session-unique data processing step by generating
        # data that is dependent on time
        now = datetime.datetime.now()

        # simulate an expensive data processing task by sleeping
        time.sleep(5)

        df = pd.DataFrame({
            'time': [
                str(now - datetime.timedelta(seconds=15)),
                str(now - datetime.timedelta(seconds=10)),
                str(now - datetime.timedelta(seconds=5)),
                str(now)
            ],
            'values': ['a', 'b', 'a', 'c']
        })
        return df.to_json()

    return pd.read_json(query_and_serialize_data(session_id))


def serve_layout():
    session_id = str(uuid.uuid4())

    return html.Div([
        html.Div(session_id, id='session-id', style={'display': 'none'}),
        html.Button('Get data', id='get-data-button'),
        html.Div(id='output-1'),
        html.Div(id='output-2')
    ])


app.layout = serve_layout


@app.callback(Output('output-1', 'children'),
              [Input('get-data-button', 'n_clicks'),
               Input('session-id', 'children')])
def display_value_1(value, session_id):
    df = get_dataframe(session_id)
    return html.Div([
        'Output 1 - Button has been clicked {} times'.format(value),
        html.Pre(df.to_csv())
    ])


@app.callback(Output('output-2', 'children'),
              [Input('get-data-button', 'n_clicks'),
               Input('session-id', 'children')])
def display_value_2(value, session_id):
    df = get_dataframe(session_id)
    return html.Div([
        'Output 2 - Button has been clicked {} times'.format(value),
        html.Pre(df.to_csv())
    ])


if __name__ == '__main__':
    app.run_server(debug=True)
