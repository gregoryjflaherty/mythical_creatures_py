from ogre import Ogre, Human  # Assuming you have Ogre and Human classes defined in a module named "ogre"

def test_ogre_has_name():
    ogre = Ogre('Brak')
    assert ogre.name == 'Brak'

def test_ogre_lives_somewhere_by_default():
    ogre = Ogre('Brak')
    assert ogre.home == 'Swamp'

def test_ogre_doesnt_have_to_live_in_a_swamp():
    ogre = Ogre('Brak', 'Castle')
    assert ogre.home == 'Castle'

def test_ogre_can_meet_humans():
    ogre = Ogre('Brak')
    human = Human()
    assert human.name == 'Jane'

    ogre.encounter(human)

    assert human.encounter_counter == 1

def test_ogre_is_noticed_by_humans_every_third_encounter():
    ogre = Ogre('Brak')
    human = Human()

    ogre.encounter(human)
    ogre.encounter(human)
    assert not human.notices_ogre

    ogre.encounter(human)

    assert human.notices_ogre

def test_ogre_is_noticed_by_humans_the_sixth_time():
    ogre = Ogre('Brak')
    human = Human()

    for _ in range(6):
        ogre.encounter(human)

    assert human.notices_ogre

def test_ogre_can_swing_a_club():
    ogre = Ogre('Brak')
    human = Human()

    ogre.swing_at(human)

    assert ogre.swings == 1

def test_ogre_swings_its_club_when_noticed_by_a_human():
    ogre = Ogre('Brak')
    human = Human()
    ogre.encounter(human)

    assert ogre.swings == 0

    ogre.encounter(human)
    ogre.encounter(human)

    assert ogre.swings == 1
    assert human.notices_ogre

def test_ogre_hits_the_human_every_second_time_it_swings():
    ogre = Ogre('Brak')
    human = Human()

    for _ in range(6):
        ogre.encounter(human)

    assert human.encounter_counter == 6
    assert ogre.swings == 2
    assert human.knocked_out

def test_ogre_apologizes_and_the_human_wakes_up():
    ogre = Ogre('Brak')
    human = Human()

    for _ in range(6):
        ogre.encounter(human)

    assert human.knocked_out

    ogre.apologize(human)
    assert not human.knocked_out