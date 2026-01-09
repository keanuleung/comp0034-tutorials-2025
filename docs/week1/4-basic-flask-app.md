# 4. Basic Flask app using the paralympics data

In this activity you will recreate the same app using the Flask framework.

## Flask reference and tutorials

[Flask documentation](https://flask.palletsprojects.com/en/stable/)

[Flask tutorial](https://flask.palletsprojects.com/en/stable/tutorial/)

[Pretty Printed YouTube videos](https://www.youtube.com/@prettyprinted/videos)

[Miguel Grinberg Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

[Patrick Kennedy](https://testdriven.io/guides/flask-deep-dive/) explains specific aspects of flask
such as contexts.

There are many Flask courses and tutorials that are freely available. Flask has been around since
2010; avoid early tutorials as Flask has changed over the years. Focus on tutorials based on
Flask 3.0 or later.

## Run a flask app

[src/flask_app/flask_demo_app.py](../../src/streamlit_app/streamlit_demo_app.py) contains a
completed example of a basic Flask app using the data from the Streamlit app.

Have a look at the code and then run the app by entering
`flask --app src/flask_app/flask_demo_app run` in the terminal.

The app runs by default on http://127.0.0.1:5000

Use Ctrl + C to stop the running app.

## Create a basic Flask app

For a Flask app you create an instance of the app and then define routes. The routes determine
what should be returned to a page.

Create a new Flask app Python file in the flask_app directory and add the following code:

```python
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```

Run the app using code like this `flask --app src/flask_app/flask_demo_app run --debug` replacing
`flask_demo_app` with the name of the new Python file you just created.

The `--debug` parameter enables debug mode in which the app will try to reload automatically when
you save a change to the code.

## Create a template for the page

Unlike Dash, Flask does not have a Python API to HTML. Instead, you create an HTML template and then
use a Flask function called `render_template()` to render the page.

Flask makes use of Jinja templating. This will be covered in a later week's activities for those
that decide to use Flask. The code that you see in the example below in `{{ }}` or `{% %}` is
Jinja template syntax.

Create a new HTML file in `flask_app/templates` named `paralympics.html` with the following code:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Flask paralympics app</title>
</head>
<body>

<h1>Flask paralympics app</h1>
<h2>Data table</h2>
<!-- HTML table reference: https://www.w3schools.com/html/html_tables.asp -->
<table>
    <thead>
    <tr>
        <!-- Use Jinja to iterate through the JSON to get the column headers -->
        {% for key in data[0].keys() %}
        <th>{{ key }}</th>
        {% endfor %}
    </tr>
    </thead>
    <tbody>
    <!-- Use Jinja to iterate through the JSON to get the row values -->
    {% for row in data %}
    <tr>
        {% for value in row.values() %}
        <td>{{ value }}</td>
        {% endfor %}
    </tr>
    {% endfor %}
    </tbody>
</table>

<h2>Line chart</h2>
<!-- Pass the plotly chart data to Jinja -->
{{ plot_html|safe }}

</body>
</html>
```

## Define a route that creates the page

In a Flask app you define routes that map to URLs. Each route has a function that carries out
the steps needed to generate the content for that route.

In this case, the route returns an HTML page using the Flask's render_template() function.

Add the following import:

```python
from flask import Flask, render_template
```

Delete the hello_world() function. Leave `@app.route("/")`, `("/")` is the base route for the app i.e. the home page.

```python
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```

Replace it with a function that:

- gets the data for the table
- generates a plotly line chart
- passes both the data and the chart to the `render_template()` function. In the template HTML the
  table data is named `data` and the chart is named `plot_html`.

```python
from io import StringIO

import pandas as pd
from flask import Flask, render_template

from src.data.mock_api import get_event_data
from src.utils.line_chart import line_chart

app = Flask(__name__)

@app.route("/")
def paralympics():
    # Get the data
    para_data = get_event_data()
    df = pd.read_json(StringIO(para_data))
    df['start'] = pd.to_datetime(df['start'], dayfirst=True)
    df['end'] = pd.to_datetime(df['end'], dayfirst=True)

    # Convert the data to a type the Jinja template will accept for the table
    data = df.to_dict('records')

    # Generate the plotly chart as HTML
    fig = line_chart("participants", df)
    plot_html = fig.to_html()

    # Render the template using the data and the chart_html
    return render_template("paralympics.html", data=data, plot_html=plot_html)
```

Flask by default looks for templates in the `templates` subdirectory so you only need to
provide the HTML file name and not the path to the template.

Flask / Jinja templates are designed to work with simple Python objects (dicts, lists, strings).
`df.to_dict('records')` converts the data to a format that the template can work with.

## Improving the style
As with Dash, Flask does not explicitly apply styles. You can use CSS (e.g. Bootstrap) to style the 
table to achieve something similar to the tables displayed in Streamlit or Dash.

Use Ctrl + C to stop the Flask app.

[Next activity](5-start-coursework.md)