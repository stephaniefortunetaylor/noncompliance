from analysis import run_poisson
from data import load_data


def run_analysis() -> None:
    """
    Main entry point used to run the analysis for the noncompliance project.
    :rtype: None
    """
    print("Starting: __main__.run_analysis()")
    load_data.run()
    run_poisson.run()
    print("Exiting: __main__.run_analysis()")


if __name__ == '__main__':
    run_analysis()
