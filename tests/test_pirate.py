import pytest
from lib.pirate import Pirate  # Assuming you have a Pirate class defined in a module named "pirate"

def test_pirate_has_name():
    pytest.skip("Test is not implemented yet")
    pirate = Pirate('Jane')
    assert pirate.name == 'Jane'

def test_pirate_can_have_a_different_name():
    pytest.skip("Test is not implemented yet")
    pirate = Pirate('Blackbeard')
    assert pirate.name == 'Blackbeard'

def test_pirate_is_a_scallywag_by_default():
    pytest.skip("Test is not implemented yet")
    pirate = Pirate('Jane')
    assert pirate.job == 'Scallywag'

def test_pirate_is_not_always_a_scallywag():
    pytest.skip("Test is not implemented yet")
    pirate = Pirate('Jack', 'cook')
    assert pirate.job == 'cook'

def test_pirate_is_not_cursed_by_default():
    pytest.skip("Test is not implemented yet")
    pirate = Pirate('Jack')

    assert not pirate.cursed

    pirate.commit_heinous_act()
    assert not pirate.cursed

    pirate.commit_heinous_act()
    assert not pirate.cursed

    pirate.commit_heinous_act()
    assert pirate.cursed

def test_pirate_has_booty():
    pytest.skip("Test is not implemented yet")
    # create a pirate
    # check that the pirate starts with 0 booty

def test_pirate_gets_100_booty_for_robbing_a_ship():
    pytest.skip("Test is not implemented yet")
    # create a pirate
    # rob some ships
    # check that the pirate got 100 booty for each ship it robbed
