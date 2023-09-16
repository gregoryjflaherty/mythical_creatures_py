from medusa import Medusa, Person  # Assuming you have Medusa and Person classes defined in a module named "medusa"

def test_medusa_has_name():
    medusa = Medusa('Cassiopeia')
    assert medusa.name == 'Cassiopeia'

def test_medusa_has_no_statues_when_created():
    medusa = Medusa('Cassiopeia')
    assert len(medusa.statues) == 0

def test_medusa_gains_a_statue_when_staring_at_a_person():
    medusa = Medusa('Cassiopeia')
    victim = Person('Perseus')

    medusa.stare(victim)
    assert len(medusa.statues) == 1
    assert medusa.statues[0].name == 'Perseus'
    assert isinstance(medusa.statues[0], Person)

def test_medusa_turns_a_person_to_stone_when_staring_at_them():
    medusa = Medusa('Cassiopeia')
    victim = Person('Perseus')

    assert not victim.stoned
    medusa.stare(victim)
    assert victim.stoned

def test_medusa_can_only_have_three_victims():
    # Your code here to test the limit of victims (similar to the previous tests)
    pass

def test_medusa_unstones_the_first_victim_when_a_fourth_is_stoned():
    # Your code here to test unstoning the first victim when a fourth is stoned
    pass