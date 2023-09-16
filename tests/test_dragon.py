from dragon import Dragon

def test_has_name():
    dragon = Dragon('Ramoth', 'gold', 'Lessa')
    assert dragon.name == 'Ramoth'

def test_has_rider():
    dragon = Dragon('Ramoth', 'gold', 'Lessa')
    assert dragon.rider == 'Lessa'

def test_has_color():
    dragon = Dragon('Ramoth', 'gold', 'Lessa')
    assert dragon.color == 'gold'

def test_is_a_different_dragon():
    dragon = Dragon('Mnementh', 'bronze', 'Flar')
    assert dragon.name == 'Mnementh'

def test_has_a_different_rider():
    dragon = Dragon('Mnementh', 'bronze', 'Flar')
    assert dragon.rider == 'Flar'

def test_has_a_different_color():
    dragon = Dragon('Mnementh', 'bronze', 'Flar')
    assert dragon.color == 'bronze'

def test_was_born_hungry():
    dragon = Dragon('Mnementh', 'bronze', 'Flar')
    assert dragon.hungry() is True

def test_eats_a_lot():
    dragon = Dragon('Mnementh', 'bronze', 'Flar')
    assert dragon.hungry() is True
    dragon.eat()
    assert dragon.hungry() is True
    dragon.eat()
    assert dragon.hungry() is True
    dragon.eat()
    assert dragon.hungry() is False
