from vampire import Vampire  # Assuming you have a Vampire class defined in a module named "vampire"

def test_vampire_has_name():
    vampire = Vampire('Dracula')
    assert vampire.name == 'Dracula'

def test_vampire_can_be_named_something_else():
    vampire = Vampire('Vladimir')
    assert vampire.name == 'Vladimir'

def test_vampire_keeps_a_pet_bat_by_default():
    vampire = Vampire('Ruthven')
    assert vampire.pet == 'bat'

def test_vampire_can_keep_other_pets():
    vampire = Vampire('Varney', 'fox')
    assert vampire.pet == 'fox'

def test_vampire_is_thirsty_by_default():
    vampire = Vampire('The Count')
    assert vampire.thirsty

def test_vampire_is_not_thirsty_after_drinking():
    vampire = Vampire('Elizabeth Bathory')
    
    vampire.drink()
    assert not vampire.thirsty
