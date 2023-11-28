import datetime
from dateutil.relativedelta import relativedelta

from constants import variable


def calculate_age(date_of_birth: datetime.date) -> int:
    a = datetime.date.today()
    b = relativedelta(a, date_of_birth).years
    return b


if __name__ == "__main__":
    assert calculate_age(date_of_birth=datetime.date(1965, 6, 2)) == 58
