import pandas as pd
import statsmodels.api as sm
# noinspection PyProtectedMember
from statsmodels.discrete.discrete_model import PoissonResultsWrapper


def fit(data: pd.DataFrame) -> PoissonResultsWrapper:
    """
    Run a Poisson regression using the provided DataFrame.
    :return: Poisson result object
    """
    print('Starting: run_poisson.run()')

    # Define a list of columns to use as exogenous variables
    regressor_columns = ['occupation', 'occupation_husb', 'children']
    exogenous_data = data[regressor_columns]

    # Select the column to use for the endogenous variable
    endogenous_data = data['religious']

    # Modify this line to change how the *model* is defined
    poisson_model = sm.Poisson(endogenous_data, exogenous_data)

    # Modify this line to change how the model behaves
    poisson_result = poisson_model.fit()

    print('Exiting: run_poisson.run()')

    return poisson_result
