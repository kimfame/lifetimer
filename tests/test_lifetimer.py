import pytest

from datetime import datetime, timedelta
from lifetimer import Lifetimer


def test_get_lifespan():
    lifetimer = Lifetimer(datetime.today().year + 100)
    assert lifetimer.get_lifespan() > 0


def test_init_str_type():
    with pytest.raises(TypeError) as e:
        Lifetimer(year="a")

    assert str(e.value) == "Invalid datetime type"


def test_wrong_day():
    with pytest.raises(ValueError) as e:
        Lifetimer(year=datetime.today().year + 100, month=4, day=31)

    assert str(e.value) == "Invalid datetime value"


def test_past_day():
    today = datetime.today()
    yesterday = today - timedelta(days=1)

    with pytest.raises(ValueError) as e:
        Lifetimer(year=yesterday.year, month=yesterday.month, day=yesterday.day)

    assert str(e.value) == "Invalid datetime value"


def test_overflow_datetime():
    with pytest.raises(OverflowError) as e:
        Lifetimer(9999)

    assert str(e.value) == "Too large to count the datetime"
