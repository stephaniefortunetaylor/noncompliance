import pandas as pd


# TODO: define how to load and clean project data here
def load_data(path: str) -> pd.DataFrame:
    """
    The main function in load_data.py
    :return: None
    """
    print('Starting: load_data.load_data()')

    # Read in the data
    data = pd.read_csv(path)

    # Here is where reshaping/cleaning should happen

    print('Exiting: load_data.load_data()')

    return data
