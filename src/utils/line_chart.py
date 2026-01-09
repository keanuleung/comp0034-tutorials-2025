import plotly.express as px

def line_chart(feature, df):
    """ Creates a line chart with data

    Data is displayed over time from 1960 onwards.
    The figure shows separate trends for the winter and summer events.

     Parameters
     feature: events, sports or participants

     Returns
     fig: Plotly Express line figure
     """

    # take the feature parameter from the function and check it is valid
    if feature not in ["sports", "participants", "events", "countries"]:
        raise ValueError(
            'Invalid value for "feature". Must be one of ["sports", "participants", "events", "countries"]')
    else:
        # Make sure it is lowercase to match the dataframe column names
        feature = feature.lower()

    # Read the data from pandas into a dataframe
    cols = ["type", "year", "host", "events", "sports", "participants", "countries"]
    line_chart_data = df[cols]

    # Set the title for the chart using the value of 'feature'
    title_text = f"How has the number of {feature} changed over time?"

    '''
    Create a Plotly Express line chart with the following parameters
      line_chart_data is the DataFrane
      x="year" is the column to use as a x-axis
      y=feature is the column to use as the y-axis
      color="type" indicates if winter or summer
      title=title_text sets the title using the variable title_text
      labels={} sets the X label to Year, sets the Y axis and the legend to nothing (an empty string)
      template="simple_white" uses a Plotly theme to style the chart
    '''
    fig = px.line(line_chart_data,
                  x="year",
                  y=str(feature),
                  color="type",
                  title=title_text,
                  labels={'year': 'Year', str(feature): '', 'type': ''},
                  template="simple_white"
                  )
    return fig