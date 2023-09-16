from lib.direwolf import Direwolf
from lib.direwolf import Stark

def test_direwolf_has_name():
    wolf = Direwolf('Nymeria')
    assert wolf.name == 'Nymeria'

def test_direwolf_can_have_different_name_and_home():
    wolf = Direwolf('Lady')
    assert wolf.home == 'Beyond the Wall'
    assert wolf.name == 'Lady'

def test_direwolf_is_massive_by_default():
    wolf = Direwolf('Ghost')
    assert wolf.size == 'Massive'
    assert wolf.name == 'Ghost'

def test_direwolf_can_have_another_home_and_size():
    wolf = Direwolf('Shaggydog', 'Winterfell', 'Smol Pupper')
    assert wolf.name == 'Shaggydog'
    assert wolf.home == 'Winterfell'
    assert wolf.size == 'Smol Pupper'

def test_starks_are_in_winterfell_by_default():
    wolf = Direwolf('Summer', 'Winterfell')
    stark = Stark('Bran')
    assert wolf.home == 'Winterfell'
    assert stark.location == 'Winterfell'

def test_direwolf_starts_with_no_starks_to_protect():
    wolf = Direwolf('Nymeria')
    stark = Stark('Arya')
    assert not wolf.starks_to_protect

def test_direwolf_protects_stark_children_in_same_location():
    wolf = Direwolf('Nymeria', 'Riverlands')
    arya_stark = Stark('Arya', 'Riverlands')
    wolf.protects(arya_stark)
    assert wolf.starks_to_protect[0].name == 'Arya'

def test_direwolf_does_not_protect_stark_children_in_different_location():
    wolf = Direwolf('Ghost')
    stark = Stark('Jon', 'King\'s Landing')
    wolf.protects(stark)
    assert len(wolf.starks_to_protect) == 0

def test_direwolf_can_protect_up_to_two_stark_children():
    summer_wolf = Direwolf('Summer', 'Winterfell')
    lady_wolf = Direwolf('Lady', 'Winterfell')
    sansa_stark = Stark('Sansa')
    jon_stark = Stark('Jon')
    rob_stark = Stark('Rob')
    bran_stark = Stark('Bran')
    arya_stark = Stark('Arya')

    summer_wolf.protects(sansa_stark)
    summer_wolf.protects(jon_stark)
    lady_wolf.protects(rob_stark)
    lady_wolf.protects(bran_stark)
    lady_wolf.protects(arya_stark)

    assert len(summer_wolf.starks_to_protect) == 2
    assert len(lady_wolf.starks_to_protect) == 2
    assert summer_wolf.starks_to_protect[0] == sansa_stark
    assert summer_wolf.starks_to_protect[1] == jon_stark
    assert lady_wolf.starks_to_protect[0] == rob_stark
    assert lady_wolf.starks_to_protect[1] == bran_stark
    assert arya_stark not in summer_wolf.starks_to_protect
    assert arya_stark not in lady_wolf.starks_to_protect

def test_starks_are_unsafe_by_default():
    stark = Stark('Jon', 'The Wall')
    assert not stark.safe()
    assert stark.house_words() == 'Winter is Coming'

def test_direwolf_protects_starks():
    wolf = Direwolf('Nymeria', 'Winterfell')
    arya_stark = Stark('Arya')
    sansa_stark = Stark('Sansa')
    wolf.protects(arya_stark)

    assert arya_stark.safe()
    assert not sansa_stark.safe()

def test_direwolf_hunts_white_walkers():
    wolf = Direwolf('Nymeria', 'Winterfell')
    assert wolf.hunts_white_walkers()

def test_direwolf_does_not_hunt_white_walkers_when_protecting_starks():
    wolf = Direwolf('Nymeria', 'Winterfell')
    arya_stark = Stark('Arya')
    wolf.protects(arya_stark)
    assert not wolf.hunts_white_walkers()

def test_direwolf_can_leave_and_stop_protecting_starks():
    summer_wolf = Direwolf('Summer', 'Winterfell')
    lady_wolf = Direwolf('Lady', 'Winterfell')
    sansa_stark = Stark('Sansa')
    arya_stark = Stark('Arya')

    summer_wolf.protects(arya_stark)
    lady_wolf.protects(sansa_stark)
    summer_wolf.leaves(arya_stark)
