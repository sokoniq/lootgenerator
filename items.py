# loot types
# rarity = {"Bad": 40, "Normal": 110, "Good": 30, "Great": 13, "Amazing": 6, "Perfect": 1}

import random

import rarity
import jewelery_library
import weapons
import armor
import food


class Item:
    def __init__(self, name=None, item_type=None):
        self.__name = name.title()
        self.__item_type = item_type
        self.rarity = rarity.rarity()

    class Jewelery:
        def __init__(self, name=None):
            self._name = name.title()
            self.item_type = 'Jewelery'

        def set_random_jewelery(self, jewelery_type=None):  # jewelery_type 0=rings/1=necklaces/2=earrings
            chosen_metal = random.choice(jewelery_library.metals)
            chosen_gem = random.choice(jewelery_library.gems)
            if jewelery_type is None:
                jewelery_type = random.choice(jewelery_library.type_of_jewelery)
            elif jewelery_type in jewelery_library.type_of_jewelery:
                pass
            else:
                print('Invalid type of jewelery')
                return

            self._name = str(f'{chosen_metal} {chosen_gem} {jewelery_type}')

            return self._name.title()

        def set_custom_jewelery(self):
            chosen_metal = str(input(f'Select a metal: '))
            chosen_type_of_jewelery = str(input(f'Select a type of jewelery: '))
            chosen_gem = str(input(f'Select a gem: '))
            if chosen_metal in jewelery_library.metals:
                pass
            else:
                print('\nInvalid metal component')
                valid_metals = ' \n'.join(str(metals) for metals in jewelery_library.metals)
                print(f'Valid metal components:\n{valid_metals.title()}')
                return

            if chosen_type_of_jewelery in jewelery_library.type_of_jewelery:
                pass
            else:
                print('\nInvalid type of jewelery')
                valid_types_of_jewelery = ' \n'.join(str(types) for types in jewelery_library.type_of_jewelery)
                print(f'Valid types:\n{valid_types_of_jewelery.title()}')
                return

            if chosen_gem is None:
                self._name = str(f'{chosen_metal} {chosen_type_of_jewelery}')
            elif chosen_gem in jewelery_library.gems:
                self._name = str(f'{chosen_metal} {chosen_gem} {chosen_type_of_jewelery}')
            else:
                print('\nInvalid type of gem')
                valid_gems = ' \n'.join(str(gem) for gem in jewelery_library.gems)
                print(f'Valid gems:\n{valid_gems.title()}')
                return

            return self._name.title()

        def get_jewelery_name(self):
            return self._name.title()

    class Weapon:
        def __init__(self, name=None):
            self._name = name.title()

        class RangedWeapon:
            def __init__(self):
                self.item_type = 'Ranged weapon'

            class Ammo:
                def __init__(self, name=None):
                    self.__name = name.title()
                    self.item_type = 'Ammo'

                def set_random_ammo(self, ammo_type=None):
                    ammo_metals = random.choice(weapons.metals)
                    if ammo_type is None:
                        ammo_type = random.choice(weapons.ammo)
                    elif ammo_type.lower() in weapons.ammo:
                        pass
                    else:
                        print('\nInvalid type of ammo')
                        valid_types_of_ammo = ' \n'.join(str(types) for types in weapons.ammo)
                        print(f'Valid types:\n{valid_types_of_ammo.title()}')
                        return

                    self.__name = str(f'{ammo_metals} {ammo_type}')
                    return self.__name

                def set_custom_ammo(self):
                    ammo_metal = str(input(f'Select a metal: '))
                    ammo_type = str(input(f'Select a type of ammo: '))
                    if ammo_metal.lower() in weapons.metals:
                        pass
                    else:
                        print('\nInvalid metal component')
                        valid_metals = ' \n'.join(str(metals) for metals in weapons.metals)
                        print(f'Valid metal components:\n{valid_metals.title()}')
                        return

                    if ammo_type.lower() in weapons.ammo:
                        pass
                    else:
                        print('\nInvalid type of ammo')
                        valid_types_of_ammo = ' \n'.join(str(types) for types in weapons.ammo)
                        print(f'Valid types:\n{valid_types_of_ammo.title()}')
                        return

                    self.__name = str(f'{ammo_metal} {ammo_type}')
                    return self.__name.title()

        class Thrown:
            def __init__(self, name=None):
                self.__name = name.title()
                self.item_type = 'Thrown Weapon'

            def set_random_thrown_weapon(self, throw_type=None):
                throw_metals = random.choice(weapons.metals)
                if throw_type is None:
                    throw_type = random.choice(weapons.throwable_types)
                elif throw_type.lower() in weapons.throwable_types:
                    pass
                else:
                    print('\nInvalid type of throwable weapon')
                    valid_throw_weapons = ' \n'.join(str(types) for types in weapons.throwable_types)
                    print(f'Valid types:\n{valid_throw_weapons.title()}')
                    return

                self.__name = str(f'{throw_metals} {throw_type}')
                return self.__name

            def set_custom_thrown_weapon(self):
                throw_metal = str(input(f'Select a metal: '))
                throw_type = str(input(f'Select a thrown weapon: '))
                if throw_metal.lower() in weapons.metals:
                    pass
                else:
                    print('\nInvalid metal component')
                    valid_metals = ' \n'.join(str(metals) for metals in weapons.metals)
                    print(f'Valid metal components:\n{valid_metals.title()}')
                    return

                if throw_type.lower() in weapons.throwable_types:
                    pass
                else:
                    print('\nInvalid type of throwable weapon')
                    valid_throw_weapons = ' \n'.join(str(types) for types in weapons.throwable_types)
                    print(f'Valid types:\n{valid_throw_weapons.title()}')
                    return

                self.__name = str(f'{throw_metal} {throw_type}')
                return self.__name.title()

        class Melee:
            def __init__(self, name=None):
                self.__name = name.title()
                self.item_type = 'Melee weapon'

            def set_random_melee_weapon(self, melee_type=None):
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
                return self.__name.title()

    class Armor:
        def __init__(self, name=None):
            self._name = name.title()
            self.item_type = 'Armor'

    class Food:
        def __init__(self, name=None):
            self._name = name.title()
            self.item_type = 'Food'
