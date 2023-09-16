from lib.unicorn import Unicorn

def test_name():
    unicorn = Unicorn('Robert')
    assert unicorn.name == 'Robert'

def test_is_default_silver():
    unicorn = Unicorn('Robert')
    assert unicorn.color == 'silver'
    assert unicorn.is_silver() == True

def test_doesnt_have_to_be_silver():
    unicorn = Unicorn('Barbara', 'purple')
    assert unicorn.color == 'purple'
    assert unicorn.is_silver() == False

def test_says_sparkly_stuff():
    unicorn = Unicorn('Johnny')
    assert unicorn.say('Wonderful!') == '**;* Wonderful **;*'
    assert unicorn.say('I dont like you very much.') == '**;* I dont like you very much. **;*'
