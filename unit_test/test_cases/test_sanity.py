import pytest

from code.app import Calculation
import pytest

from code.app import Math


@pytest.mark.sanity
def test_add():
    assert Math().add(1, 2) == 3


@pytest.mark.sanity
def test_sub():
    assert Math().sub(2, 2) == 1
