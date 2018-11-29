import datetime


# TODO: define how to load and clean data here
def run() -> None:
    """
    The main function in load_data.py
    :return: None
    """
    current_datetime = datetime.datetime.now()
    print("Starting: load_data.run()")
    print(f"doing data stuff at {current_datetime}")
    print(f"doing data stuff at {datetime.datetime.now()}")
    print("Exiting: load_data.run()")
