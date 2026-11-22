
import pytest
from scores import process_scores


def test_sum():
    assert process_scores([80, 90, 70, 60, 100])[0] == 400


def test_average():
    assert process_scores([80, 90, 70, 60, 100])[1] == 80


def test_maximum():
    assert process_scores([80, 90, 70, 60, 100])[2] == 100


def test_minimum():
    assert process_scores([80, 90, 70, 60, 100])[3] == 60


def test_empty_list():
    with pytest.raises(ValueError):
        process_scores([])
