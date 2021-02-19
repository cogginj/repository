"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730237793"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    # TODO 2: Call days_to_target and store result in a variable.
    days_to_target: int = int:
    # TODO 4: Call future_date and store result in a variable.
    future_date: str = str:
    # TODO 5: Print the expected output using the variables above.
    string = ("We will reach {}% vaccination in {} days on {}").format(target, days_to_target, future_date)
    print(string)


# TODO 1: Define days_to_target function
additional_vaccines: float = ((2 * population * (target) / 100)) - doses) 
def days_to_target: int = int = additional_vaccines / doses_per_day


# TODO 3: Define future_date function
Days: timedelta = timedelta(days_to_target)
today: datetime = datetime.today()
Vaccination_date: datetime = today + Days
future_date: str = Vaccination_date.strftime("%B %d, %Y")


if __name__ == "__main__":
    main()