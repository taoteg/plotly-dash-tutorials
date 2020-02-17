import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd

"""
Here is an example where a dcc.Slider updates a dcc.Graph.

In this example, the "value" property of the Slider is the input of the app and
the output of the app is the "figure" property of the Graph. Whenever the value
of the Slider changes, Dash calls the callback function update_figure with the
new value.

The function filters the dataframe with this new value, constructs a figure
object, and returns it to the Dash application.

There are a few nice patterns in this example:

- We're using the Pandas library for importing and filtering datasets in memory.

- We load our dataframe at the start of the app: df = pd.read_csv('...').
  This dataframe df is in the global state of the app and can be read inside the
  callback functions.

- Loading data into memory can be expensive. By loading querying data at the
  start of the app instead of inside the callback functions, we ensure that this
  operation is only done when the app server starts. When a user visits the app
  or interacts with the app, that data (the df) is already in memory. If possible,
  expensive initialization (like downloading or querying data) should be done in
  the global scope of the app instead of within the callback functions.

- The callback does not modify the original data, it just creates copies of the
  dataframe by filtering through pandas filters. This is important: your callbacks
  should never mutate variables outside of their scope. If your callbacks modify
  global state, then one user's session might affect the next user's session and
  when the app is deployed on multiple processes or threads, those modifications
  will not be shared across sessions.

- We are turning on transitions with layout.transition to give an idea of how the
  dataset evolves with time: transitions allow the chart to update from one state
  to the next smoothly, as if it were animated.
"""

df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='year-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()},
        step=None
    )
])


@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('year-slider', 'value')])
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]
    traces = []
    for i in filtered_df.continent.unique():
        df_by_continent = filtered_df[filtered_df['continent'] == i]
        traces.append(dict(
            x=df_by_continent['gdpPercap'],
            y=df_by_continent['lifeExp'],
            text=df_by_continent['country'],
            mode='markers',
            opacity=0.7,
            marker={
                'size': 15,
                'line': {'width': 0.5, 'color': 'white'}
            },
            name=i
        ))

    return {
        'data': traces,
        'layout': dict(
            xaxis={'type': 'log', 'title': 'GDP Per Capita',
                   'range': [2.3, 4.8]},
            yaxis={'title': 'Life Expectancy', 'range': [20, 90]},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            hovermode='closest',
            transition={'duration': 500},
        )
    }


if __name__ == '__main__':
    app.run_server(debug=True)
