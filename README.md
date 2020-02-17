# Plotly Dash Tutorials

_Notes on Dash apps_

- New in dash 0.30.0 and dash-renderer 0.15.0, Dash includes "hot-reloading", this features
  is activated by default when you run your app with app.run_server(debug=True). This means
  that Dash will automatically refresh your browser when you make a change in your code.

- The layout of a Dash app describes what the app looks like. The layout is a hierarchical tree of components. The dash_html_components library provides classes for all of the HTML tags and the keyword arguments describe the HTML attributes like style, className, and id. The dash_core_components library generates higher-level components like controls and graphs.

For reference, see these:

- dash_core_components gallery: https://dash.plot.ly/dash-core-components

- dash_html_components gallery: https://dash.plot.ly/dash-html-components
