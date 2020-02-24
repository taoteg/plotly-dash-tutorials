# -*- coding: utf-8 -*-

"""
PART 7B: Gotchas

There are some aspects of how Dash works that can be counter-intuitive.
This can be especially true of how the callback system works.
This section outlines some common Dash gotchas that you might encounter as you
start building out more complex Dash apps. If you have read through the rest of
the Dash Tutorial and are encountering unexpected behaviour, this is a good
section to read through. If you still have residual questions, the Dash
Community forums is a great place to ask them.

-----------------------
GOTCHA 1:

Callbacks require their Inputs, States, and Output to be present in the layout

By default, Dash applies validation to your callbacks, which performs checks
such as validating the types of callback arguments and checking to see whether
the specified Input and Output components actually have the specified properties.
For full validation, all components within your callback must therefore appear
in the initial layout of your app, and you will see an error if they do not.

However, in the case of more complex Dash apps that involve dynamic modification
of the layout (such as multi-page apps), not every component appearing in your
callbacks will be included in the initial layout. You can remove this restriction
by disabling callback validation like this:

  app.config.suppress_callback_exceptions = True

-----------------------
GOTCHA 2:

Callbacks require all Inputs, States, and Output to be rendered on the page

If you have disabled callback validation in order to support dynamic layouts,
then you won't be automatically alerted to the situation where a component
within a callback is not found within a layout. In this situation, where a
component registered with a callback is missing from the layout, the callback
will fail to fire. For example, if you define a callback with only a subset of
the specified Inputs present in the current page layout, the callback will
simply not fire at all.

-----------------------
GOTCHA 3:

A component/property pair can only be the Output of one callback

For a given component/property pair (eg 'my-graph', 'figure'), it can only be
registered as the Output of one callback. If you want to associate two logically
separate sets of Inputs with the one output component/property pair, you’ll have
to bundle them up into a larger callback and detect which of the relevant Inputs
triggered the callback inside the function. For html.Button elements, detecting
which one triggered the callback ca be done using the n_clicks_timestamp
property. For an example of this, see the question in the FAQ, How do I
determine which Input has changed?.

-----------------------
GOTCHA 4:

All callbacks must be defined before the server starts

All your callbacks must be defined before your Dash app's server starts running,
which is to say, before you call app.run_server(debug=True). This means that
while you can assemble changed layout fragments dynamically during the handling
of a callback, you can't define dynamic callbacks in response to user input
during the handling of a callback. If you have a dynamic interface, where a
callback changes the layout to include a different set of input controls, then
you must have already defined the callbacks required to service these new
controls in advance.

For example, a common scenario is a Dropdown component that updates the current
layout to replace a dashboard with another logically distinct dashboard that has
a different set of controls (the number and type of which might which might
depend on other user input) and different logic for generating the underlying
data. A sensible organisation would be for each of these dashboards to have
separate callbacks. In this scenario, each of these callbacks much then be
defined before the app starts running.

Generally speaking, if a feature of your Dash app is that the number of Inputs
or States is determined by a user's input, then you must pre-define up front
every permutation of callback that a user can potentially trigger. For an
example of how this can be done programmatically using the callback decorator,
see this Dash Community forum post.

  - https://community.plot.ly/t/callback-for-dynamically-created-graph/5511?_ga=2.112487175.2023386239.1582568405-1984378524.1582568405

-----------------------
GOTCHA 5:

All Dash Core Components in a layout should be registered with a callback.

Note: This section is present for legacy purposes. Prior to v0.40.0, setProps
was only defined if the component was connected to a callback. This required
complex state management within the component like this. Now, setProps is always
defined which should simplify your component's state management. Learn more in
this community forum topic.

If a Dash Core Component is present in the layout but not registered with a
callback (either as an Input, State, or Output) then any changes to its value
by the user will be reset to the original value when any callback updates the
page.

This is a known issue and you can track its status in this GitHub Issue.

  - https://community.plot.ly/t/callbacks-clearing-all-unconnected-core-components-values/7631?_ga=2.49522469.2023386239.1582568405-1984378524.1582568405
  - https://github.com/plotly/dash-renderer/issues/40

"""
