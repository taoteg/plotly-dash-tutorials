# -*- coding: utf-8 -*-

"""
PART 7A: FAQs

This is the 7th and final chapter of the essential Dash Tutorial. The previous
chapter described how to share data between callbacks. The rest of the Dash
documentation covers other topics like multi-page apps and component libraries.

- https://dash.plot.ly/

-----------------------
Q: How can I customize the appearance of my Dash app?

A: Dash apps are rendered in the browser as modern standards-compliant web apps.
   This means that you can use CSS to style your Dash app as you would standard HTML.

   All dash-html-components support inline CSS styling through a style attribute.
   An external CSS stylesheet can also be used to style dash-html-components and
   dash-core-components by targeting the ID or class names of your components.
   Both dash-html-components and dash-core-components accept the attribute className,
   which corresponds to the HTML element attribute class.

   The Dash HTML Components section in the Dash User Guide explains how to supply
   dash-html-components with both inline styles and CSS class names that you can
   target with CSS style sheets. The Adding CSS & JS and Overriding the Page-Load
   Template section in the Dash Guide explains how you can link your own style
   sheets to Dash apps.

   - https://dash.plot.ly/dash-html-components
   - https://dash.plot.ly/external-resources

-----------------------
Q: How can I add JavaScript to my Dash app?

A: You can add your own scripts to your Dash app, just like you would add a
   JavaScript file to an HTML document. See the Adding CSS & JS and Overriding
   the Page-Load Template section in the Dash Guide.

   - https://dash.plot.ly/dash-html-components
   - https://dash.plot.ly/external-resources

-----------------------
Q: Can I make a Dash app with multiple pages?

A: Yes! Dash has support for multi-page apps.
   See the Multi-Page Apps and URL Support section in the Dash User Guide.

   - https://dash.plot.ly/urls

-----------------------
Q: How I can I organise my Dash app into multiple files?

A: A strategy for doing this can be found in the Multi-Page Apps and URL
   Support section in the Dash User Guide.

   - https://dash.plot.ly/urls

-----------------------
Q: How do I determine which Input has changed?

A: New in v0.38.0! In addition to event properties like n_clicks that change
   whenever an event happens (in this case a click), there is a global variable
   dash.callback_context, available only inside a callback. It has properties:

    triggered: list of changed properties.
            This will be empty on initial load, unless an Input prop got its
            value from another initial callback. After a user action it is a
            length-1 list, unless two properties of a single component update
            simultaneously, such as a value and a timestamp or event counter.
    inputs and states: allow you to access the callback params by id and prop
            instead of through the function args. These have the form of
            dictionaries { 'component_id.prop_name': value }

Here's an example of how this can be done:
"""

# Detecting Changed Inputs Example.

import json

import dash
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Button('Button 1', id='btn-1'),
    html.Button('Button 2', id='btn-2'),
    html.Button('Button 3', id='btn-3'),
    html.Div(id='container')
])


@app.callback(Output('container', 'children'),
              [Input('btn-1', 'n_clicks'),
               Input('btn-2', 'n_clicks'),
               Input('btn-3', 'n_clicks')])
def display(btn1, btn2, btn3):
    ctx = dash.callback_context

    if not ctx.triggered:
        button_id = 'No clicks yet'
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    ctx_msg = json.dumps({
        'states': ctx.states,
        'triggered': ctx.triggered,
        'inputs': ctx.inputs
    }, indent=2)

    return html.Div([
        html.Table([
            html.Tr([html.Th('Button 1'),
                     html.Th('Button 2'),
                     html.Th('Button 3'),
                     html.Th('Most Recent Click')]),
            html.Tr([html.Td(btn1 or 0),
                     html.Td(btn2 or 0),
                     html.Td(btn3 or 0),
                     html.Td(button_id)])
        ]),
        html.Pre(ctx_msg)
    ])


if __name__ == '__main__':
    app.run_server(debug=True)


"""
Prior to v0.38.0, you needed to compare timestamp properties like
n_clicks_timestamp to find the most recent click.

While existing uses of *_timestamp continue to work for now, this approach is
deprecated, and may be removed in a future update.

The one exception is modified_timestamp from dcc.Store, which is safe to use,
it is NOT deprecated.

-----------------------
Q: Can I use Jinja2 templates with Dash?

A: Jinja2 templates are rendered on the server (often in a Flask app) before
   being sent to the client as HTML pages. Dash apps, on the other hand, are
   rendered on the client using React. This makes these fundamentally different
   approaches to displaying HTML in a browser, which means the two approaches
   can't be combined directly. You can however integrate a Dash app with an
   existing Flask app such that the Flask app handles some URL endpoints, while
   your Dash app lives at a specific URL endpoint.

-----------------------
Q: Can I use jQuery with Dash?

A: For the most part, you can't. Dash uses React to render your app on the
   client browser. React is fundamentally different to jQuery in that it makes
   use of a virtual DOM (Document Object Model) to manage page rendering.
   Since jQuery doesn't speak React's virtual DOM, you can't use any of
   jQuery's DOM manipulation facilities to change the page layout, which is
   frequently why one might want to use jQuery. You can however use parts of
   jQuery's functionality that do not touch the DOM, such as registering event
   listeners to cause a page redirect on a keystroke.

In general, if you are looking to add custom clientside behavior in your
application, we recommend encapsulating that behavior in a custom Dash component.

  - https://dash.plot.ly/plugins

-----------------------
Q: Where did those cool undo and redo buttons go?

A: OK, mostly we got the opposite question: How do I get rid of the undo/redo
   buttons. While this feature is neat from a technical standpoint most people
   don't find it valuable in practice. As of Dash 1.0 the buttons are removed by
   default, no hacky CSS tricks needed. If you want them back, use show_undo_redo:

        app = Dash(show_undo_redo=True)

  - https://community.plot.ly/t/is-it-possible-to-hide-the-floating-toolbar/4911/10?_ga=2.77204374.2023386239.1582568405-1984378524.1582568405

-----------------------
 Q: I have more questions! Where can I go to ask them?

A: The Dash Community forums is full of people discussing Dash topics, helping
   each other with questions, and sharing Dash creations. Jump on over and join
   the discussion.

   - https://community.plot.ly/c/dash?_ga=2.77204374.2023386239.1582568405-1984378524.1582568405

"""
