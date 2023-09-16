from lib.centaur import Centaur

def test_centaur_has_name(): 
    centaur = Centaur('George', 'Palomino')
    assert centaur.name == 'George'

def test_centaur_has_breed():
    centaur = Centaur('George', 'Palomino')
    assert centaur.breed == 'Palomino'

def test_has_excellent_bow_skills():
    centaur = Centaur('George', 'Palomino')
    assert centaur.shoot == 'Twang!!!'

def test_makes_a_horse_sound_when_it_runs():
    centaur = Centaur('George', 'Palomino')
    assert centaur.run == 'Clop clop clop clop!'

def test_when_created_it_is_not_cranky():
    centaur = Centaur('George', 'Palomino')
    assert centaur.is_cranky() == False

def test_new_centaur_is_standing():
    centaur = Centaur('George', 'Palomino')
    assert centaur.standing()

def test_centaur_gets_tired_after_running_and_shooting_thrice():
    centaur = Centaur('George', 'Palomino')
    assert not centaur.cranky()

    centaur.run()
    centaur.shoot()
    centaur.run()

    assert centaur.cranky()

def test_centaur_cannot_shoot_when_cranky():
    centaur = Centaur('George', 'Palomino')
    assert not centaur.cranky()

    for _ in range(3):
        centaur.shoot()

    assert centaur.shoot() == 'NO!'

def test_centaur_cannot_sleep_when_standing():
    centaur = Centaur('George', 'Palomino')
    assert centaur.sleep() == 'NO!'

def test_centaur_is_not_standing_after_laying_down():
    centaur = Centaur('George', 'Palomino')
    centaur.lay_down()

    assert not centaur.standing()
    assert centaur.laying()

def test_centaur_can_sleep_when_laying_down():
    centaur = Centaur('George', 'Palomino')
    centaur.lay_down()

    assert centaur.sleep() == 'ZZZ'

def test_centaur_cannot_shoot_or_run_or_stand_when_laying_down():
    centaur = Centaur('George', 'Palomino')
    centaur.lay_down()

    assert centaur.shoot() == 'NO!'
    assert centaur.run() == 'NO!'
    assert not centaur.standing()

def test_centaur_can_stand_up():
    centaur = Centaur('George', 'Palomino')
    centaur.lay_down()
    centaur.stand_up()

    assert centaur.standing()

def test_centaur_becomes_rested_after_sleeping():
    centaur = Centaur('George', 'Palomino')

    centaur.shoot()
    centaur.run()
    centaur.shoot()

    assert centaur.cranky()

    centaur.lay_down()
    centaur.sleep()

    assert not centaur.cranky()

    centaur.stand_up()

    assert centaur.shoot() == 'Twang!!!'
    assert centaur.run() == 'Clop clop clop clop!'

def test_centaur_becomes_rested_after_drinking_potion():
    # write own test here
    pass 

def test_can_only_drink_potion_while_standing():
    # write own test here
    pass 

def test_gets_sick_if_potion_is_drunk_while_rested():
    # write own test here
    pass 
