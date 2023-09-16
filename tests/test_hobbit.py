from hobbit import Hobbit  # Assuming you have a Hobbit class defined in a module named "hobbit"

def test_hobbit_has_name():
    hobbit = Hobbit('Bilbo')
    assert hobbit.name == 'Bilbo'

def test_hobbit_can_have_another_name():
    hobbit = Hobbit('Peregrin')
    assert hobbit.name == 'Peregrin'

def test_hobbit_has_unadventurous_disposition():
    hobbit = Hobbit('Samwise')
    assert hobbit.disposition == 'homebody'

def test_hobbit_can_have_different_disposition():
    hobbit = Hobbit('Frodo', 'adventurous')
    assert hobbit.disposition == 'adventurous'

def test_hobbit_can_grow_older_when_celebrating_birthdays():
    hobbit = Hobbit('Meriadoc')
    assert hobbit.age == 0

    for _ in range(5):
        hobbit.celebrate_birthday()

    assert hobbit.age == 5

def test_hobbit_is_considered_a_child_at_32():
    hobbit = Hobbit('Gerontius')

    for _ in range(32):
        hobbit.celebrate_birthday()

    assert not hobbit.adult()

def test_hobbit_comes_of_age_at_33():
    hobbit = Hobbit('Otho')

    for _ in range(33):
        hobbit.celebrate_birthday()

    assert hobbit.adult()

    # Still an adult one year later
    hobbit.celebrate_birthday()
    assert hobbit.adult()

# The following tests are pending (marked with xit), you can implement them similarly as needed.
def test_hobbit_is_old_at_age_101():
    # create a hobbit
    # have hobbit age 101 years
    # check that hobbit.old? returns true
    pass

def test_hobbit_has_the_ring_if_its_name_is_frodo():
    # create a hobbit named Frodo
    # create a second hobbit named Sam
    # check that .has_ring? for Frodo returns true
    # check that .has_ring? for Sam returns false
    pass

def test_hobbit_is_short():
    # create a hobbit
    # check that is_short? returns true
    pass
