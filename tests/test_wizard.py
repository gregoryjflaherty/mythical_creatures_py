from wizard import Wizard

def test_has_name():
    wizard = Wizard('Eric')
    assert wizard.name == 'Eric'

def test_has_different_name():
    wizard = Wizard('Alex')
    assert wizard.name == 'Alex'

def test_is_bearded_by_default():
    wizard = Wizard('Ben')
    assert wizard.bearded() is True

def test_is_not_always_bearded():
    wizard = Wizard('Valerie', bearded=False)
    assert wizard.bearded() is False

def test_has_root_powers():
    wizard = Wizard('Stella', bearded=False)
    assert wizard.incantation('chown ~/bin') == 'sudo chown ~/bin'

def test_has_many_root_powers():
    wizard = Wizard('Sal', bearded=True)
    assert wizard.incantation('rm -rf /home/mirandax') == 'sudo rm -rf /home/mirandax'

def test_starts_rested():
    # create wizard
    # .rested? returns true

def test_can_cast_spells():
    # create wizard
    # .cast returns "MAGIC MISSILE!"

def test_gets_tired_after_casting_three_spells():
    # create wizard
    # casts spell twice
    # check if wizard is rested
    # casts spell
    # check wizard is not rested
