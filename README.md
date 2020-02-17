# Plotly Dash Tutorials

_Notes on App_

- The layout is composed of a tree of "components" like html.Div and dcc.Graph.

- The dash_html_components library has a component for every HTML tag.
  The html.H1(children='Hello Dash') component generates a <h1>Hello Dash</h1>
  HTML element in your application.

- Not all components are pure HTML. The dash_core_components describe higher-level
  components that are interactive
  and are generated with JavaScript, HTML, and CSS through the React.js library.

- Each component is described entirely through keyword attributes. Dash is declarative:
  you will primarily describe your application through these attributes.

- The children property is special. By convention, it's always the first attribute
  which means that you can omit it: html.H1(children='Hello Dash') is the same as
  html.H1('Hello Dash'). Also, it can contain a string, a number, a single component,
  or a list of components.

- The fonts in your application will look a little bit different than what is displayed here.
  This application is using a custom CSS stylesheet to modify the default styles of the elements.
  You can learn more in the css tutorial, but for now you can initialize your app with:
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
  to get the same look and feel of these examples.

- New in dash 0.30.0 and dash-renderer 0.15.0, Dash includes "hot-reloading", this features
  is activated by default when you run your app with app.run_server(debug=True). This means
  that Dash will automatically refresh your browser when you make a change in your code.
