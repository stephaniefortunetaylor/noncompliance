import pandas as pd
import statsmodels.api as sm


# TODO: define how to load and clean project data here
def load_data() -> pd.DataFrame:
    """
    The main function in load_data.py
    :return: None
    """
    print('Starting: load_data.load_data()')

    data = sm.datasets.fair.load_pandas().data

    print('Exiting: load_data.load_data()')

    return data
