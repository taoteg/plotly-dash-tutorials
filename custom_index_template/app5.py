# -*- coding: utf-8 -*-

"""
Customizing Meta Tags

Not sure what meta tags are?
Check out this tutorial on meta tags and why you might want to use them.
https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/The_head_metadata_in_HTML

To add custom meta tags to your application, you can always override Dash's HTML
Index Template. Alternatively, Dash provides a shortcut: you can specify meta
tags directly in the Dash constructor.

If you inspect the source of your app, you should see the meta tags appear.
"""

import dash
import dash_html_components as html

app = dash.Dash(meta_tags=[
    # A description of the app, used by e.g.
    # search engines when displaying search results.
    {
        'name': 'description',
        'content': 'My description'
    },
    # A tag that tells Internet Explorer (IE)
    # to use the latest renderer version available
    # to that browser (e.g. Edge)
    {
        'http-equiv': 'X-UA-Compatible',
        'content': 'IE=edge'
    },
    # A tag that tells the browser not to scale
    # desktop widths to fit mobile screens.
    # Sets the width of the viewport (browser)
    # to the width of the device, and the zoom level
    # (initial scale) to 1.
    #
    # Necessary for "true" mobile support.
    {
      'name': 'viewport',
      'content': 'width=device-width, initial-scale=1.0'
    }
])

app.layout = html.Div('Simple Dash App')

if __name__ == '__main__':
    app.run_server(debug=True)
