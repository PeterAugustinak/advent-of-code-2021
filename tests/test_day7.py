import pytest
from src.day7 import *


def test_count_to_desired_position():
    # TC01
    desired_position = count_to_desired_position(0, 1)
    assert 1 == desired_position

    # TC02
    desired_position = count_to_desired_position(0, 0)
    assert 0 == desired_position

   # TC03
    desired_position = count_to_desired_position(0, 1000)
    assert 1000 == desired_position
 
    # TC04
    desired_position = count_to_desired_position(1000, 0)
    assert 1000 == desired_position
 
    # TC05
    desired_position = count_to_desired_position(500, 250)
    assert 250 == desired_position
 
    # TC06
    desired_position = count_to_desired_position(1000, 1)
    assert 999 == desired_position
 