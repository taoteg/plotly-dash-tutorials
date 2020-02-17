import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

"""
The dash_core_components library includes a component called Graph.

Graph renders interactive data visualizations using the open source plotly.js JavaScript graphing library.
Plotly.js supports over 35 chart types and renders charts in both vector-quality SVG and high-performance WebGL.

The figure argument in the dash_core_components.Graph component is the same figure argument that is used by plotly.py,
Plotly's open source Python graphing library. Check out the plotly.py documentation and gallery to learn more.

Here's an example that creates a scatter plot from a Pandas dataframe for life expectancy vs GDP.

These graphs are interactive and responsive. Hover over points to see their values, click on legend items to
toggle traces, click and drag to zoom, hold down shift, and click and drag to pan.
"""

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

app.layout = html.Div([
    dcc.Graph(
        id='example-04',
        figure={
            'data': [
                dict(
                    x=df[df['continent'] == i]['gdp per capita'],
                    y=df[df['continent'] == i]['life expectancy'],
                    text=df[df['continent'] == i]['country'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.continent.unique()
            ],
            'layout': dict(
                xaxis={'type': 'log', 'title': 'GDP Per Capita'},
                yaxis={'title': 'Life Expectancy'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
