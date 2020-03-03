# -*- coding: utf-8 -*-

"""
Adding CSS & JS and Overriding the Page-Load Template

Dash applications are rendered in the web browser with CSS and JavaScript. On
page load, Dash serves a small HTML template that includes references to the
CSS and JavaScript that are required to render the application. This chapter
covers everything that you need to know about configuring this HTML file and
about including external CSS and JavaScript in Dash applications.


Customizing dash-renderer with request v2.

When you provide your own DashRenderer, you can also pass in a hooks object that
holds request_pre and request_post functions. These request hooks will be fired
before and after Dash makes a request to its backend.

Below is an example.

Notice the request_pre function takes the payload of the request being sent as
its argument, and the request_post fuction takes both the payload and the
response of the server as arguments. These can be altered in our function,
allowing you to modify the response and request objects that Dash sends to the
server. In the example above, the request_pre function is fired before each
server call, and in the case of this example, it will console.log() the request
parameter. The request_post function will fire after each server call, and in
our example will also print out the response parameter.
"""

import dash
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.renderer = '''var renderer = new DashRenderer({
    request_pre: (payload) => {
        // print out payload parameter
        console.log(" ");
        console.log("REQUEST_PRE");
        console.log("-- payload: ", payload);
        console.log("_______________________________");
    },
    request_post: (payload, response) => {
        // print out payload and response parameter
        console.log(" ");
        console.log("REQUEST_POST");
        console.log("-- payload: ", payload);
        console.log(" ");
        console.log("-- response: ", response);
        console.log("_______________________________");
    }
})'''

app.layout = html.Div('Simple Dash App - Custom Template 4')

if __name__ == '__main__':
    app.run_server(debug=True)
