# -*- coding: utf-8 -*-

"""
Structuring a Multi-Page App

Here's how to structure a multi-page app, where each app is contained in a
separate file.

Nested File structure:

- app.py
- index.py
- apps
   |-- __init__.py
   |-- app1.py
   |-- app2.py


Alternatively, you may prefer a flat project layout with callbacks and layouts
separated into different files.

Flat File Structure:
- app.py
- index.py
- callbacks.py
- layouts.py

It is worth noting that in both of these project structures, the Dash instance
is defined in a separate app.py, while the entry point for running the app is
index.py.

This separation is required to avoid circular imports, the files containing
the callback definitions require access to the Dash app instance
however if this were imported from index.py, the initial loading of index.py
would ultimately require itself to be already imported, which cannot be
satisfied.
"""

import dash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.config.suppress_callback_exceptions = True
