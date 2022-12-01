# import random
jump = '\n'
types_of_armor = ['armor.headgear','armor.chestgear','armor.legs','armor.gloves','armor.boots','armor.shields']


'''def set_random_melee_weapon(self, melee_type=None):
    melee_metal = random.choice(weapons.metals)
    if melee_type is None:
        melee_type = random.choice(weapons.melee_types)
    elif melee_type.lower() in weapons.melee_types:
        pass
    else:
        print('\nInvalid type of weapon')
        valid_weapons = ' \n'.join(str(types) for types in weapons.melee_types)
        print(f'Valid types:\n{valid_weapons.title()}')
        return

    self.__name = str(f'{melee_metal} {melee_type}')
    return self.__name


def set_custom_melee_weapon(self):
    melee_metal = str(input(f'Select a metal: '))
    melee_type = str(input(f'Select a melee weapon: '))
    if melee_metal.lower() in weapons.metals:
        pass
    else:
        print('\nInvalid metal component')
        valid_metals = ' \n'.join(str(metals) for metals in weapons.metals)
        print(f'Valid metal components:\n{valid_metals.title()}')
        return

    if melee_type.lower() in weapons.melee_types:
        pass
    else:
        print('\nInvalid type of ammo')
        valid_weapons = ' \n'.join(str(types) for types in weapons.melee_types)
        print(f'Valid types:\n{valid_weapons.title()}')
        return

    self.__name = str(f'{melee_metal} {melee_type}')
    return self.__name.title()'''