""" Function to return the data in JSON format as you would get from an API """
import json
from pathlib import Path

import pandas as pd


def get_event_data():
    """ Method to return the data from the event csv file.

    NB: This is NOT how you will do it in the coursework, this is a simplified return of all
    data with no validation.

    Returns:
        json_data: json format data from the event file

    Raises:
        RuntimeError: if the data could not be read, converted to JSON
        FileNotFoundError: if no event file was found

        """
    data_file = Path(__file__).parent.joinpath("paralympic_events.csv")
    try:
        if not data_file.exists():
            raise FileNotFoundError(f"Data file not found: {data_file}")
        df = pd.read_csv(data_file)
        if df.empty:
            return []
        json_data = df.to_json(orient='records')
        # json_data = df.to_json()
        return json_data
    except FileNotFoundError:
        raise
    except (pd.errors.EmptyDataError, pd.errors.ParserError) as e:
        raise RuntimeError(f"Error reading CSV {data_file}: {e}") from e
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Error decoding JSON from CSV conversion: {e}") from e
    except Exception as e:
        raise RuntimeError(f"Unexpected error loading event data: {e}") from e
