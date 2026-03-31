from crab_game import display_arrows_left, random_int_mod
import pytest 

def test_display_arrows():
    
    assert display_arrows_left(10) == "You have 10 arrows left."
    assert display_arrows_left(0) == "You have 0 arrows left."
    assert display_arrows_left(7) == "You have 7 arrows left."

def test_randomont_mod():

    assert random_int_mod(0, 0, 0) == 0
    assert random_int_mod (0, 0, 1) == 1
    assert random_int_mod (10, 20, 0) >= 9
    assert random_int_mod (0, 10, 0) <= 11
    assert random_int_mod (1, 5, 10) >= 11


if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN"])