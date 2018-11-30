from analysis import run_poisson
from data import load_data


def run_analysis() -> None:
    """
    Main entry point used to run the analysis for the noncompliance project.
    :rtype: None
    """
    print('Starting: __main__.run_analysis()')

    data = load_data.load_data()

    poisson_result = run_poisson.fit(data)

    print('Print result summary:')
    print(poisson_result.summary())

    print('Exiting: __main__.run_analysis()')


if __name__ == '__main__':
    run_analysis()
