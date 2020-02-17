"""
Dash Installation

In your terminal, install several dash libraries.
These libraries are under active development, so install and upgrade frequently.
Python 2 and 3 are supported.

    pip install dash==1.8.0

Note: starting with dash 0.37.0, dash automatically installs known-compatible versions
of each of these pafkages:
    - dash-renderer
    - dash-core-components
    - dash-html-components
    - dash-table

You need not and should not install these separately any longer, only dash itself.

A quick note on checking your versions and on upgrading.

These docs are run using the versions listed above and these versions should be the
latest versions available.

To check which version that you have installed, you can run e.g.

>>> import dash_core_components
>>> print(dash_core_components.__version__)

To see the latest changes of any package, check the GitHub repo's CHANGELOG.md file:

- dash & dash-renderer changelog
    -- dash-renderer is a separate package installed automatically with dash but
       its updates are included in the main dash changelog.
       These docs are using dash-renderer==1.2.3.
- dash-core-components changelog
- dash-html-components changelog
- dash-table changelog
- plotly changelog
    -- the plotly package is also installed automatically with dash. It is the
       Python interface to the plotly.js graphing library, so is mainly used by
       dash-core-components, but it's also used by dash itself.
       These docs are using plotly==3.3.0.

All of these packages adhere to semver.
"""
