# -*- coding: utf-8 -*-

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
    # Here, `df` is an example of a variable that is
    # "outside the scope of this function".
    # *It is not safe to modify or reassign this variable
    #  inside this callback.*
    global df = df[df['c'] == value]  # do not do this, this is not safe!
    return len(df)

# To fix this example, simply re-assign the filter to a new variable inside the callback,
# or follow one of the strategies outlined in the next part of this guide.

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
    # Safely reassign the filter to a new variable
    filtered_df = df[df['c'] == value]  # do this instead.
    return len(filtered_df)


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

global_df = pd.read_csv('...')
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

"""
Example 2 - Computing Aggregations Upfront

Sending the computed data over the network can be expensive if the data is large.
In some cases, serializing this data and JSON can also be expensive.

In many cases, your app will only display a subset or an aggregation of the computed
or filtered data. In these cases, you could precompute your aggregations in your data
processing callback and transport these aggregations to the remaining callbacks.
Here's a simple example of how you might transport filtered or aggregated data to
 multiple callbacks.
"""

# Example 2 - Computing Aggregations Upfront

@app.callback(
    Output('intermediate-value', 'children'),
    [Input('dropdown', 'value')])
def clean_data(value):
     # an expensive query step
     cleaned_df = your_expensive_clean_or_compute_step(value)

     # a few filter steps that compute the data
     # as it's needed in the future callbacks
     df_1 = cleaned_df[cleaned_df['fruit'] == 'apples']
     df_2 = cleaned_df[cleaned_df['fruit'] == 'oranges']
     df_3 = cleaned_df[cleaned_df['fruit'] == 'figs']

     datasets = {
         'df_1': df_1.to_json(orient='split', date_format='iso'),
         'df_2': df_2.to_json(orient='split', date_format='iso'),
         'df_3': df_3.to_json(orient='split', date_format='iso'),
     }

     return json.dumps(datasets)

@app.callback(
    Output('graph', 'figure'),
    [Input('intermediate-value', 'children')])
def update_graph_1(jsonified_cleaned_data):
    datasets = json.loads(jsonified_cleaned_data)
    dff = pd.read_json(datasets['df_1'], orient='split')
    figure = create_figure_1(dff)
    return figure

@app.callback(
    Output('graph', 'figure'),
    [Input('intermediate-value', 'children')])
def update_graph_2(jsonified_cleaned_data):
    datasets = json.loads(jsonified_cleaned_data)
    dff = pd.read_json(datasets['df_2'], orient='split')
    figure = create_figure_2(dff)
    return figure

@app.callback(
    Output('graph', 'figure'),
    [Input('intermediate-value', 'children')])
def update_graph_3(jsonified_cleaned_data):
    datasets = json.loads(jsonified_cleaned_data)
    dff = pd.read_json(datasets['df_3'], orient='split')
    figure = create_figure_3(dff)
    return figure
