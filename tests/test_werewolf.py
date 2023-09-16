from werewolf import Werewolf, Victim

def test_has_name():
    werewolf = Werewolf('David')
    assert werewolf.name == 'David'

def test_has_location():
    werewolf = Werewolf('David', 'London')
    assert werewolf.location == 'London'

def test_is_by_default_human():
    werewolf = Werewolf('David', 'London')
    assert werewolf.human is True

def test_starting_as_human_and_changing_turns_it_into_werewolf():
    werewolf = Werewolf('David', 'London')
    werewolf.change()
    assert werewolf.wolf is True
    assert werewolf.human is False

def test_starting_as_human_and_changing_again_makes_it_human_again():
    werewolf = Werewolf('David', 'London')
    assert werewolf.human is True

    werewolf.change()

    assert werewolf.human is False

    werewolf.change()

    assert werewolf.human is True

def test_starting_as_werewolf_and_changing_a_second_time_makes_it_werewolf():
    werewolf = Werewolf('David', 'London')

    werewolf.change()
    assert werewolf.wolf is True

    werewolf.change()
    werewolf.change()

    assert werewolf.wolf is True

def test_is_not_hungry_by_default():
    werewolf = Werewolf('David', 'London')
    assert werewolf.is_hungry() is False

def test_becomes_hungry_after_changing_to_werewolf():
    werewolf = Werewolf('David', 'London')
    werewolf.change()
    assert werewolf.is_hungry() is True

def test_consumes_a_victim():


def test_cannot_consume_a_victim_if_it_is_in_human_form():


def test_werewolf_that_has_consumed_a_human_being_is_no_longer_hungry():


def test_werewolf_who_has_consumed_a_victim_makes_the_victim_dead():

