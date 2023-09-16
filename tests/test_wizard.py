import pytest
from lib.wizard import Wizard

def test_has_name():
    pytest.skip("Test is not implemented yet")
    wizard = Wizard('Eric')
    assert wizard.name == 'Eric'

def test_has_different_name():
    pytest.skip("Test is not implemented yet")
    wizard = Wizard('Alex')
    assert wizard.name == 'Alex'

def test_is_bearded_by_default():
    pytest.skip("Test is not implemented yet")
    wizard = Wizard('Ben')
    assert wizard.bearded() is True

def test_is_not_always_bearded():
    pytest.skip("Test is not implemented yet")
    wizard = Wizard('Valerie', bearded=False)
    assert wizard.bearded() is False

def test_has_root_powers():
    pytest.skip("Test is not implemented yet")
    wizard = Wizard('Stella', bearded=False)
    assert wizard.incantation('chown ~/bin') == 'sudo chown ~/bin'

def test_has_many_root_powers():
    pytest.skip("Test is not implemented yet")
    wizard = Wizard('Sal', bearded=True)
    assert wizard.incantation('rm -rf /home/mirandax') == 'sudo rm -rf /home/mirandax'

def test_starts_rested():
    pytest.skip("Test is not implemented yet")
    # create wizard
    # .rested? returns true

def test_can_cast_spells():
    pytest.skip("Test is not implemented yet")
    # create wizard
    # .cast returns "MAGIC MISSILE!"

def test_gets_tired_after_casting_three_spells():
    pytest.skip("Test is not implemented yet")
    # create wizard
    # casts spell twice
    # check if wizard is rested
    # casts spell
    # check wizard is not rested
