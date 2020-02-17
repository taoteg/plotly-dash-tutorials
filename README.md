# Plotly Dash Tutorials


_Resources & Documentation_

### Python, Flask Framework & ReactJS
- Python: https://www.python.org/download/releases/3.0/
- Flask: https://palletsprojects.com/p/flask/
- ReactJS: https://reactjs.org/

### Plotly & Dash.js Library
- plotlyJS: https://plot.ly/python/
- https://plot.ly/dash/
- https://github.com/plotly/dash

### Dash Tutorial
- Tutorials: https://dash.plot.ly/
- Part 1: https://dash.plot.ly/installation
- Part 2: https://dash.plot.ly/getting-started
- Part 3: https://dash.plot.ly/getting-started-part-2
- Part 4: https://dash.plot.ly/state
- Part 5: https://dash.plot.ly/interactive-graphing
- Part 6: https://dash.plot.ly/sharing-data-between-callbacks
- Part 7: https://dash.plot.ly/faqs

### Additional Resources
- CSS & JS:  https://dash.plot.ly/external-resources


_Notes on Dash apps_

- New in dash 0.30.0 and dash-renderer 0.15.0, Dash includes "hot-reloading", this features
  is activated by default when you run your app with app.run_server(debug=True). This means
  that Dash will automatically refresh your browser when you make a change in your code.

- The layout of a Dash app describes what the app looks like. The layout is a hierarchical tree of components. The dash_html_components library provides classes for all of the HTML tags and the keyword arguments describe the HTML attributes like style, className, and id. The dash_core_components library generates higher-level components like controls and graphs.

For reference, see these:

- dash_core_components gallery: https://dash.plot.ly/dash-core-components

- dash_html_components gallery: https://dash.plot.ly/dash-html-components

- Dash apps are built off of a set of simple but powerful principles: declarative UIs that are customizable through reactive and functional Python callbacks. Every element attribute of the declarative components can be updated through a callback and a subset of the attributes, like the value properties of the dcc.Dropdown, are editable by the user in the interface.
