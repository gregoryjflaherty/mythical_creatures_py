import pytest
from vampire import Vampire  

def test_vampire_has_name():
    pytest.skip("Test is not implemented yet")
    vampire = Vampire('Dracula')
    assert vampire.name == 'Dracula'

def test_vampire_can_be_named_something_else():
    pytest.skip("Test is not implemented yet")
    vampire = Vampire('Vladimir')
    assert vampire.name == 'Vladimir'

def test_vampire_keeps_a_pet_bat_by_default():
    pytest.skip("Test is not implemented yet")
    vampire = Vampire('Ruthven')
    assert vampire.pet == 'bat'

def test_vampire_can_keep_other_pets():
    pytest.skip("Test is not implemented yet")
    vampire = Vampire('Varney', 'fox')
    assert vampire.pet == 'fox'

def test_vampire_is_thirsty_by_default():
    pytest.skip("Test is not implemented yet")
    vampire = Vampire('The Count')
    assert vampire.thirsty

def test_vampire_is_not_thirsty_after_drinking():
    pytest.skip("Test is not implemented yet")
    vampire = Vampire('Elizabeth Bathory')
    
    vampire.drink()
    assert not vampire.thirsty
