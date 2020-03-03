# -*- coding: utf-8 -*-

"""
Adding CSS & JS and Overriding the Page-Load Template

Dash applications are rendered in the web browser with CSS and JavaScript. On
page load, Dash serves a small HTML template that includes references to the
CSS and JavaScript that are required to render the application. This chapter
covers everything that you need to know about configuring this HTML file and
about including external CSS and JavaScript in Dash applications.

Sample Dash CSS Stylesheet

Currently, Dash does not include styles by default.

To get started with Dash styles, we recommend starting with this CSS stylesheet
hosted on Codepen.

To include this stylesheet in your application, copy and paste it into a file in
your assets folder. You can view the raw CSS source here:

    https://codepen.io/chriddyp/pen/bWLwgP.css.

Here is an embedded version of this stylesheet using an example template.


Syntax Highlighting With Markdown

Both dash-table and dash-core-components support markdown formatting; this
includes syntax highlighting for inline code.

Highlighting is taken care of by highlight.js. By default, only certain
languages are recognized, and there is only one color scheme available. However,
you can override this by downloading a custom highlight.js package. To do this,
visit:

    https://highlightjs.org/download/

and in the "Custom package" section, check off all of the languages that you
require, download your package, and place the resultant highlight.pack.js file
into the assets/ folder for your app. The package should also come with a
styles/ directory; to use a different color scheme, simply copy the
corresponding stylesheet into your app's assets/ folder.
"""

import dash
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.index_string = '''
<!DOCTYPE html>
<html>

<head>
  {%metas%}
  <title>{%title%}</title>
  {%favicon%}
  {%css%}
</head>

<body>
  <div>
    <center>
      <h1>My Custom header</h1>
    </center>
  </div>
  <br />
  {%app_entry%}
  <br />
  <!-- Primary Page Layout –––––––––––––––––––––––––––––––––––––––––––––––––– -->
  <div class="container">
    <section class="header">
      <div>
        This Codepen is a work-in-progress CSS styleguide. By default, Dash is unstyled. You can add CSS stylesheets to your dash apps by URL or you can style elements individually: <a href="https://dash-docs.herokuapp.com/custom-css-and-js">documentation
          on CSS stylesheets and Dash</a>
      </div>
      <br />
      <div>
        This stylesheet is based off of <a href="http://getskeleton.com" target="_blank">Skeleton</a>. Give them a <a href="https://github.com/dhg/skeleton/" target="_blank">☆</a>!
      </div>

      <hr />
      <h4>Usage</h4>
      <div>
        You can embed custom stylesheets in your dash apps via a custom URL:
        <pre>app.css.append_css({
            "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
        })</pre> You can extract the stylesheet from the Codepen playground by appending ".css" to the end of any codepen URL (e.g. <a href="https://codepen.io/chriddyp/pen/bWLwgP.css">https://codepen.io/chriddyp/pen/bWLwgP.css</a>. You can either
        use this
        Codepen directly or you can fork this Codepen and modify it and embed the forked URL.
        <br /><br /> If your Dash app receives a lot of traffic, you should host the CSS somewhere else. One option is hosting it on GitHub's <a href="https://gist.github.com">Gist</a> and serving it through the free CDN <a href="https://rawgit.com/">RawGit</a>.
      </div>

      <hr />
      <h3>Styles Index</h3>
      <ul class="popover-list">
        <li>
          <a href="#grid">Grid</a>
        </li>
        <li>
          <a href="#typography">Typography</a>
        </li>
        <li>
          <a href="#buttons">Buttons</a>
        </li>
        <li>
          <a href="#forms">Forms</a>
        </li>
        <li>
          <a href="#lists">Lists</a>
        </li>
        <li>
          <a href="#code">Code</a>
        </li>
        <li>
          <a href="#tables">Tables</a>
        </li>
      </ul>
    </section>

    <!-- Grid -->
    <div id="grid">
      <hr />
      <h3>The grid</h3>
      <p>The grid is a <u>12-column fluid grid with a max width of 960px</u>, that shrinks with the browser/device at smaller sizes. The max width can be changed with one line of CSS and all columns will resize accordingly. The syntax is simple and
        it
        makes
        coding responsive much easier. Go ahead, resize the browser. </p>
      <div>
        <div class="row">
          <div class="one column" style="text-align: center; border-radius: 4px; margin: 2px; background-color: lightgrey;">One</div>
          <div class="eleven columns" style="text-align: center; border-radius: 4px; margin: 2px; background-color: lightgrey;">Eleven</div>
        </div>
        <div class="row">
          <div class="two columns" style="text-align: center; border-radius: 4px; margin: 2px; background-color: lightgrey;">Two</div>
          <div class="ten columns" style="text-align: center; border-radius: 4px; margin: 2px; background-color: lightgrey;">Ten</div>
        </div>
        <div class="row">
          <div class="three columns" style="text-align: center; border-radius: 4px; margin: 2px; background-color: lightgrey;">Three</div>
          <div class="nine columns" style="text-align: center; border-radius: 4px; margin: 2px; background-color: lightgrey;">Nine</div>
        </div>
        <div class="row">
          <div class="four columns" style="text-align: center; border-radius: 4px; margin: 2px; background-color: lightgrey;">Four</div>
          <div class="eight columns" style="text-align: center; border-radius: 4px; margin: 2px; background-color: lightgrey;">Eight</div>
        </div>
        <div class="row">
          <div class="five columns" style="text-align: center; border-radius: 4px; margin: 2px; background-color: lightgrey;">Five</div>
          <div class="seven columns" style="text-align: center; border-radius: 4px; margin: 2px; background-color: lightgrey;">Seven</div>
        </div>
        <div class="row">
          <div class="six columns" style="text-align: center; border-radius: 4px; margin: 2px; background-color: lightgrey;">Six</div>
          <div class="six columns" style="text-align: center; border-radius: 4px; margin: 2px; background-color: lightgrey;">Six</div>
        </div>
        <div class="row">
          <div class="seven columns" style="text-align: center; border-radius: 4px; margin: 2px; background-color: lightgrey;">Seven</div>
          <div class="five columns" style="text-align: center; border-radius: 4px; margin: 2px; background-color: lightgrey;">Five</div>
        </div>
        <div class="row">
          <div class="eight columns" style="text-align: center; border-radius: 4px; margin: 2px; background-color: lightgrey;">Eight</div>
          <div class="four  columns" style="text-align: center; border-radius: 4px; margin: 2px; background-color: lightgrey;">Four</div>
        </div>
        <div class="row">
          <div class="nine columns" style="text-align: center; border-radius: 4px; margin: 2px; background-color: lightgrey;">Nine</div>
          <div class="three columns" style="text-align: center; border-radius: 4px; margin: 2px; background-color: lightgrey;">Three</div>
        </div>
        <div class="row">
          <div class="ten columns" style="text-align: center; border-radius: 4px; margin: 2px; background-color: lightgrey;">Ten</div>
          <div class="two columns" style="text-align: center; border-radius: 4px; margin: 2px; background-color: lightgrey;">Two</div>
        </div>
        <div class="row">
          <div class="eleven columns" style="text-align: center; border-radius: 4px; margin: 2px; background-color: lightgrey;">Eleven</div>
          <div class="one column" style="text-align: center; border-radius: 4px; margin: 2px; background-color: lightgrey;">One</div>
        </div>
      </div>
    </div>

    <!-- Typography -->
    <div id="typography">
      <hr />
      <h3>Typography</h3>
      <p>Type is all set with the <code>rems</code>, so font-sizes and spacial relationships can be responsively sized based on a single <code>&lt;html&gt;</code> font-size property. Out of the box, Dash never changes the <code>&lt;html&gt;</code>
        font-size,
        but it's there in case you need it for your project. All measurements are still base 10 though so, an <code>&lt;h1&gt;</code> with <code>5.0rem</code>font-size just means <code>50px</code>.</p>

      <hr />

      <div class="docs-example">
        <p><strong>The typography base</strong> is <a href="https://fonts.google.com/specimen/Open+Sans">Open Sans</a> served by Google, set at 15rem (15px) over a 1.6 line height (24px). Other type basics like <a href="#">anchors</a>, <strong>strong</strong>,
          <em>emphasis</em>, and <u>underline</u> are all obviously included.</p>

        <p>
          <blockquote>
            Don't forget <b>blockquotes!</b> Blockquotes have a simple
            left border and an indent, there is nothing too fancy
            here. These styles are meant to be familiar to GitHub markdown users.
          </blockquote>
        </p>

        <p><strong>Headings</strong> create a family of distinct sizes each with specific <code>letter-spacing</code>, <code>line-height</code>, and <code>margins</code>.</p>
      </div>
      <div>
        <h1>Heading<span> <code>&lt;h1&gt;</code> 4.5rem</span></h1>
        <h2>Heading<span> <code>&lt;h2&gt;</code> 3.6rem</span></h2>
        <h3>Heading<span> <code>&lt;h3&gt;</code> 3.0rem</span></h3>
        <h4>Heading<span> <code>&lt;h4&gt;</code> 2.6rem</span></h4>
        <h5>Heading<span> <code>&lt;h5&gt;</code> 2.2rem</span></h5>
        <h6>Heading<span> <code>&lt;h6&gt;</code> 2.0rem</span></h6>
      </div>
    </div>

    <!-- Buttons -->
    <div id="buttons">
      <hr />
      <h3>Buttons</h3>
      <p>Buttons come in two basic flavors in Dash. The standard <code>&lt;button&gt;</code> element is plain, whereas the <code>.button-primary</code> button is vibrant and prominent. Button styles are applied to a number of appropriate form
        elements,
        but can also be arbitrarily attached to anchors with a <code>.button</code> class.</p>
      <div class="docs-example">
        <div>
          <a class="button" href="#">Anchor button</a>
          <button>Button element</button>
          <input type="submit" value="submit input">
          <input type="button" value="button input">
        </div>
        <div>
          <a class="button button-primary" href="#">Anchor button</a>
          <button class="button-primary">Button element</button>
          <input class="button-primary" type="submit" value="submit input">
          <input class="button-primary" type="button" value="button input">
        </div>
      </div>
    </div>

    <!-- Forms -->
    <div id="forms">
      <hr />
      <h3>Forms</h3>
      <p>Forms are a huge pain, but hopefully these styles make it a bit easier. All inputs, select, and buttons are normalized for a common height cross-browser so inputs can be stacked or placed alongside each other.</p>
      <div class="docs-example docs-example-forms">
        <form>
          <div class="row">
            <div class="six columns">
              <label for="exampleEmailInput">Your email</label>
              <input class="u-full-width" type="email" placeholder="test@mailbox.com" id="exampleEmailInput">
            </div>
            <div class="six columns">
              <label for="exampleRecipientInput">Reason for contacting</label>
              <select class="u-full-width" id="exampleRecipientInput">
                <option value="Option 1">Questions</option>
                <option value="Option 2">Admiration</option>
                <option value="Option 3">Can I get your number?</option>
              </select>
            </div>
          </div>
          <label for="exampleMessage">Message</label>
          <textarea class="u-full-width" placeholder="Hi Dave &hellip;" id="exampleMessage"></textarea>
          <label class="example-send-yourself-copy">
            <input type="checkbox">
            <span class="label-body">Send a copy to yourself</span>
          </label>
          <input class="button-primary" type="submit" value="Submit">
        </form>
      </div>
    </div>

    <div>
      <label>Text Input</label>
      <input type="text" value="hello" />

      <label>Radio Input</label>
      <input type="radio" />

      <label>Numeric Input</label>
      <input type="number" />
    </div>

    <!-- Lists -->
    <div id="lists">
      <hr />
      <h3>Lists</h3>
      <div class="row docs-example">
        <div class="six columns">
          <ul>
            <li>Unordered lists have basic styles</li>
            <li>
              They use the circle list style
              <ul>
                <li>Nested lists styled to feel right</li>
                <li>Can nest either type of list into the other</li>
              </ul>
            </li>
            <li>Just more list items mama san</li>
          </ul>
        </div>
        <div class="six columns">
          <ol>
            <li>Ordered lists also have basic styles</li>
            <li>
              They use the decimal list style
              <ul>
                <li>Ordered and unordered can be nested</li>
                <li>Can nest either type of list into the other</li>
              </ul>
            </li>
            <li>Last list item just for the fun</li>
          </ol>
        </div>
      </div>
    </div>

    <!-- Code -->
    <div id="code">
      <hr />
      <h3>Code</h3>
      <p>Code styling is kept basic – just wrap anything in a <code>&lt;code&gt;</code> and it will appear like <code>this</code>. For blocks of code, wrap a <code>&lt;code&gt;</code> with a <code>&lt;pre&gt;</code>.</p>
      <div class="docs-example">
        <pre><code>.some-class {
          background-color: red;
        }</code></pre>
      </div>
    </div>

    <!-- Tables -->
    <div id="tables">
      <hr />
      <h3>Tables</h3>
      <p>Be sure to use properly formed table markup with <code>&lt;thead&gt;</code> and <code>&lt;tbody&gt;</code> when building a <code>table</code>.</p>
      <div class="docs-example">
        <table class="u-full-width">
          <thead>
            <tr>
              <th>Name</th>
              <th>Age</th>
              <th>Sex</th>
              <th>Location</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Dave Gamache</td>
              <td>26</td>
              <td>Male</td>
              <td>San Francisco</td>
            </tr>
            <tr>
              <td>Dwayne Johnson</td>
              <td>42</td>
              <td>Male</td>
              <td>Hayward</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Queries -->
    <div id="queries">
      <hr />
      <h3>Media queries</h3>
      <p>Dash uses media queries to serve its scalable grid, but also has a list of queries for convenience of styling your site across devices. The queries are mobile-first, meaning they target <code>min-width</code>. Mobile-first queries are how
        Dash's
        grid is built and is the preferrable method of organizing CSS. It means all styles outside of a query apply to all devices, then larger devices are targeted for enhancement. This prevents small devices from having to parse tons of unused
        CSS.
        The
        sizes for the queries are:</p>
      <div class="docs-example row">
        <div class="six columns">
          <ul>
            <li><strong>Desktop HD</strong>: 1200px</li>
            <li><strong>Desktop</strong>: 1000px</li>
            <li><strong>Tablet</strong>: 750px</li>
          </ul>
        </div>
        <div class="six columns">
          <ul>
            <li><strong>Phablet</strong>: 550px</li>
            <li><strong>Mobile</strong>: 400px</li>
          </ul>
        </div>
      </div>
    </div>
    <footer>
      {%config%}
      {%scripts%}
      {%renderer%}
    </footer>
  <!-- END Primary Page Layout –––––––––––––––––––––––––––––––––––––––––––––––––– -->
  </div>
  <br />
  <div>
    <center>
      <h5>My Custom footer</h5>
    </center>
  </div>
</body>

</html>
'''

app.layout = html.Div()

if __name__ == '__main__':
    app.run_server(debug=True)
