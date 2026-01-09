# 2. Basic Streamlit app using the paralympics data

In this and the following two activities, you will recreate the same app which will have a simple
title, a table showing all the data from the paralympics data set and a chart. The purpose is to
give you an intro to each of the apps so that you can make a more informed choice of which to use
for the coursework.

## Streamlit reference and tutorials

[Streamlit concepts](https://docs.streamlit.io/get-started/fundamentals/main-concepts)

[Streamlit API reference](https://docs.streamlit.io/develop/api-reference)

[Streamlit create your first app tutorial](https://docs.streamlit.io/get-started/tutorials/create-an-app)

[Streamlit tutorials](https://docs.streamlit.io/develop/tutorials)

If you decide to use Streamlit, you should follow their full tutorial as it explains concepts and
features of Streamlit that you will need to know but that are not covered in this simple activity.

## Run a streamlit app

[src/streamlit_app/streamlit_demo_app.py](../../src/streamlit_app/streamlit_demo_app.py) contains a
completed example of the Streamlit tutorial.

Have a look at the code and then run the app by entering
`streamlit run src/streamlit_app/streamlit_demo_app.py` in the terminal.

The app runs by default on http://localhost:8501

Use Ctrl + C to stop the running app.

## Create a basic streamlit app

Create a new streamlit_app.py file in the streamlit_app directory.

Add import:

```python
import streamlit as st
```

Add a title for the streamlit app.

```python
st.title('Paralympics data')
```

Run the app and leave it running.

Streamlit changes can be dynamically seen in the browser. Every time you want to update your app,
save the source file. Streamlit detects if there is a change and asks you whether you want to rerun
your app.
Choose "Always rerun" at the top-right of your browser window to automatically update your app every
time you change its source code. You can then quickly see changes in your app as you make them.

## Load the data

Load the data into a pandas DataFrame. The data will be in JSON format.

You can just load the data into a dataframe without writing a function. Writing it as a function
lets you use the streamlit cache_data decorator; this will speed the time to reload the page when
changes are made.

https://docs.streamlit.io/develop/api-reference/data/st.table
Add code such as the following to your app:

```python
from io import StringIO
import pandas as pd
from src.data.mock_api import get_event_data


@st.cache_data
def load_data():
    """ Read the JSON structured data into a pandas DataFrame

    @st.cache_data allows the data to be cached

    Returns:
        df  pandas DataFrame with the unstructured paralympics data i.e. single table
    """
    para_data = get_event_data()
    df = pd.read_json(StringIO(para_data))
    df['start'] = pd.to_datetime(df['start'], dayfirst=True)
    df['end'] = pd.to_datetime(df['end'], dayfirst=True)
    return df
```

## Display a table

Streamlit has functions that allow you to add tables, charts or widgets to a page. Use their
reference to see what is available.

Use the [dataframe](https://docs.streamlit.io/develop/api-reference/data/st.dataframe) function to
display
all the data from the dataframe. Add the code yourself to your app file after the title element.

The app should update when you save your app file.

## Display a Plotly line chart

Charts are covered in a later week. For now, use the line_chart() function
in [src/utils/line_chart.py](../../src/utils/line_chart.py) by adding the import:

```python
from src.utils.line_chart import line_chart
```

To create a chart, use one of the allowable parameters (e.g. "participants") and your dataframe.

```python
chart = line_chart("participants", df)
```

Use the
streamlit [plotly_chart function](https://docs.streamlit.io/develop/api-reference/charts/st.plotly_chart)
to add this to your app.

## Next

Stop the running streamlit app using Ctrl + C

You will now recreate a similar app using the other two frameworks, Dash and Flask.

[Next activity](3-basic-dash-app.md)