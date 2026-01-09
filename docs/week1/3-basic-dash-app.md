# Basic Dash app using the paralympics data

In this activity you will recreate the same app using the Plotly Dash (Python) open source
framework.

## Dash reference and tutorial

[Dash documentation](https://dash.plotly.com)

[Minimal Dash app tutorial](https://dash.plotly.com/minimal-app)

[Charming Data YouTube channel](https://www.youtube.com/@CharmingData/playlists) - not an
official Dash tutorial; however, it has lots of useful Dash videos.

Dash changed significantly in version 2, so take care with older tutorials showing earlier
versions.

## Run a Dash app

[src/dash_app/dash_demo_app.py](../../src/dash_app/dash_demo_app.py) contains a
completed example of the [Dash tutorial](https://dash.plotly.com/tutorial).

Have a look at the code and then run the app by entering
`python src/dash_app/dash_demo_app.py` in the terminal (or use the 'Run' feature in your IDE).

The app runs by default on http://127.0.0.1:8050/

Use Ctrl + C to stop the running app.

## Create a basic Dash app

In Dash, you create an instance of a Dash app object, add a layout to the app, and then run the app.

Create a new Dash app Python file in the dash_app directory.

First, import `Dash` and `html`:

```python
from dash import Dash, html
```

To create the app:

```python
app = Dash()
```

To add a title, you first need to create a layout for the app and then add an HTML H1 heading
within the layout. You don't write HTML code directly. Dash uses Python functions to create HTML
elements, which Dash calls components.

```python
app.layout = [
    html.H1(children='Title of Dash App'),
]
```

You can then run the app using:

```python
if __name__ == '__main__':
    app.run(debug=True)
```

Add the code to your app Python file and run the Dash app.

Dash, like Streamlit, will attempt to auto-reload the page when you save changes to your Python
app file. Leave the app running in the browser.

## Load the data

Load the JSON format data into a pandas DataFrame.

Import the mock_api function and pandas:

```python
import pandas as pd
from src.data.mock_api import get_event_data
```

Add code such as the following to your app before the `app.layout` section to load the data:

```python
para_data = get_event_data()
df = pd.DataFrame(para_data)
df['start'] = pd.to_datetime(df['start'], dayfirst=True)
df['end'] = pd.to_datetime(df['end'], dayfirst=True)
```

## Display a table

Dash has a [DataTable component](https://dash.plotly.com/datatable) that you will use.

Add the dash_table import as follows:

```python
from dash import Dash, html, dash_table
```

Use the [DataTable reference](https://dash.plotly.com/datatable) to add code to create a table from
the dataframe e.g. ``

Add the code within the `app.layout` section after the `html.H1` component. Use a comma `,` after
the H1 component before you create the datatable component.

The app should update in the browser when you save your app file.

Note: [Dash AG Grid](https://dash.plotly.com/dash-ag-grid/javascript-and-the-grid) could also be used for this e.g.

```python
import dash_ag_grid as dag

# Add this in the app.layout
dag.AgGrid(
        rowData=df.to_dict("records"),
        columnDefs=[{"field": col} for col in df.columns]
),
```

## Display a Plotly line chart

Charts are covered in a later week. For now, use the line_chart() function
in [src/utils/line_chart.py](../../src/utils/line_chart.py) by adding the import:

```python
from src.utils.line_chart import line_chart
```

To create a chart, use one of the allowable parameters (e.g. "participants") and your dataframe.

```python
line_chart("participants", df)
```

Add a chart component containing the chart to the `app.layout`. This uses the Dash Core Components 
(dcc) which you need to add to the imports:

```python
from dash import Dash, html, dash_table, dcc
```

Add the chart component, e.g. `dcc.Graph(figure=line_chart("participants", df))`, to the
`app.layout`.

## Improving the look and layout

This is a very basic layout. The look and layout can be improved using CSS, this is covered in a
later week. If you want to add it now,
investigate [dash-bootstrap-components](https://www.dash-bootstrap-components.com/docs/).

## Next

Stop the running Dash app using Ctrl + C

Dash has much more functionality to improve the look and feel and add interactive components using
'callbacks'. If you decide to use Dash for the coursework, these will be introduced in later
weeks activities.

You will now recreate a similar app using the other two frameworks, Dash and Flask.

[Next activity](3-basic-dash-app.md)
