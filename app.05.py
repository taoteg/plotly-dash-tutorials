# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

"""
Part 2E: Markdown

While Dash exposes HTML through the dash_html_components library, it can be
tedious to write your copy in HTML. For writing blocks of text, you can use the
Markdown component in the dash_core_components library.

Dash apps can be written in Markdown.
Dash uses the CommonMark specification of Markdown.
Check out their 60 Second Markdown Tutorial if this is your first introduction to Markdown!

CommonMark: http://commonmark.org/
Tutorial: http://commonmark.org/help/
"""

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

markdown_text = '''
### Dash and Markdown

Dash apps can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org/)
specification of Markdown.
Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown!
'''

app.layout = html.Div([
    dcc.Markdown(children=markdown_text)
])

if __name__ == '__main__':
    app.run_server(debug=True)
