# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
from dash.dependencies import Input, Output

"""
PART 5C: Generic Crossfilter Recipe

Here's a slightly more generic example for crossfiltering across a six-column
data set. Each scatter plot's selection filters the underlying dataset.

Try clicking and dragging in any of the plots to filter different regions.
On every selection, the three graph callbacks are fired with the latest selected
regions of each plot. A pandas dataframe is filtered based off of the selected
points and the graphs are replotted with the selected points highlighted and
the selected region drawn as a dashed rectangle.

- As an aside, if you find yourself filtering and visualizing highly-dimensional
datasets, you should consider checking out the parallel coordinates chart type.

Current Limitations

There are a few limitations in graph interactions right now.

- It is not currently possible to customize the style of the hover interactions
  or the select box. This issue is being worked on in
  https://github.com/plotly/plotly.js/issues/1847.
"""

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# make a sample data frame with 6 columns
np.random.seed(0)
df = pd.DataFrame({"Col " + str(i + 1): np.random.rand(30) for i in range(6)})

app.layout = html.Div([
    html.Div(
        dcc.Graph(id='g1', config={'displayModeBar': False}),
        className='four columns'
    ),
    html.Div(
        dcc.Graph(id='g2', config={'displayModeBar': False}),
        className='four columns'
    ),
    html.Div(
        dcc.Graph(id='g3', config={'displayModeBar': False}),
        className='four columns'
    )
], className='row')


def get_figure(df, x_col, y_col, selectedpoints, selectedpoints_local):

    if selectedpoints_local and selectedpoints_local['range']:
        ranges = selectedpoints_local['range']
        selection_bounds = {'x0': ranges['x'][0], 'x1': ranges['x'][1],
                            'y0': ranges['y'][0], 'y1': ranges['y'][1]}
    else:
        selection_bounds = {'x0': np.min(df[x_col]), 'x1': np.max(df[x_col]),
                            'y0': np.min(df[y_col]), 'y1': np.max(df[y_col])}

    # set which points are selected with the `selectedpoints` property
    # and style those points with the `selected` and `unselected`
    # attribute. see
    # https://medium.com/@plotlygraphs/notes-from-the-latest-plotly-js-release-b035a5b43e21
    # for an explanation
    return {
        'data': [{
            'x': df[x_col],
            'y': df[y_col],
            'text': df.index,
            'textposition': 'top',
            'selectedpoints': selectedpoints,
            'customdata': df.index,
            'type': 'scatter',
            'mode': 'markers+text',
            'marker': {'color': 'rgba(0, 116, 217, 0.7)', 'size': 12},
            'unselected': {
                'marker': {'opacity': 0.3},
                # make text transparent when not selected
                'textfont': {'color': 'rgba(0, 0, 0, 0)'}
            }
        }],
        'layout': {
            'margin': {'l': 20, 'r': 0, 'b': 15, 't': 5},
            'dragmode': 'select',
            'hovermode': False,
            # Display a rectangle to highlight the previously selected region
            'shapes': [dict({
                'type': 'rect',
                'line': {'width': 1, 'dash': 'dot', 'color': 'darkgrey'}
            }, **selection_bounds
            )]
        }
    }

# this callback defines 3 figures
# as a function of the intersection of their 3 selections


@app.callback(
    [Output('g1', 'figure'),
     Output('g2', 'figure'),
     Output('g3', 'figure')],
    [Input('g1', 'selectedData'),
     Input('g2', 'selectedData'),
     Input('g3', 'selectedData')]
)
def callback(selection1, selection2, selection3):
    selectedpoints = df.index
    for selected_data in [selection1, selection2, selection3]:
        if selected_data and selected_data['points']:
            selectedpoints = np.intersect1d(selectedpoints,
                                            [p['customdata'] for p in selected_data['points']])

    return [get_figure(df, "Col 1", "Col 2", selectedpoints, selection1),
            get_figure(df, "Col 3", "Col 4", selectedpoints, selection2),
            get_figure(df, "Col 5", "Col 6", selectedpoints, selection3)]


if __name__ == '__main__':
    app.run_server(debug=True)
