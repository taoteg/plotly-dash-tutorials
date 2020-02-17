import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

"""
Basic Dash Callbacks

Dash App Layout

In the previous chapter on `app.layout` we learned that the app.layout describes
what the app looks like and is a hierarchical tree of components.

The dash_html_components library provides classes for all of the HTML tags,
and the keyword arguments describe the HTML attributes like style, className, and id.

The dash_core_components library generates higher-level components like controls and graphs.

This app demonstrates how to make your Dash apps interactive.

Try typing in the text box.
The children of the output component updates right away.
Let's break down what's happening here:

    - The "inputs" and "outputs" of our application interface are described declaratively through the app.callback decorator.

    - In Dash, the inputs and outputs of our application are simply the properties of a particular component.
      In this example, our input is the "value" property of the component that has the ID "my-id".
      Our output is the "children" property of the component with the ID "my-div".

    - Whenever an input property changes, the function that the callback decorator wraps will get called automatically.
      Dash provides the function with the new value of the input property as an input argument and Dash updates the property
      of the output component with whatever was returned by the function.

    - The component_id and component_property keywords are optional (there are only two arguments for each of those objects).
      I have included them here for clarity but I will omit them from here on out for brevity and readability.

    - Don't confuse the dash.dependencies.Input object and the dash_core_components.Input object.
      The former is just used in these callbacks and the latter is an actual component.

    - Notice how we don't set a value for the children property of the my-div component in the layout.
      When the Dash app starts, it automatically calls all of the callbacks with the initial values of the input components in
      order to populate the initial state of the output components. In this example, if you specified something like
      html.Div(id='my-div', children='Hello world'), it would get overwritten when the app starts.

It's sort of like programming with Microsoft Excel: whenever an input cell changes, all of the cells that depend on that cell
will get updated automatically. This is called "Reactive Programming".

Remember how every component was described entirely through its set of keyword arguments?
Those properties are important now.
With Dash interactivity, we can dynamically update any of those properties through a callback function.

Frequently we'll update the children of a component to display new text or the figure of a dcc.Graph component to display new data,
but we could also update the style of a component or even the available options of a dcc.Dropdown component!
"""

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(id='my-id', value='initial value', type='text'),
    html.Div(id='my-div')
])


@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)


if __name__ == '__main__':
    app.run_server(debug=True)
