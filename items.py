# loot types
# rarity = {"Bad": 40, "Normal": 110, "Good": 30, "Great": 13, "Amazing": 6, "Perfect": 1}

import random
import rarity
import jewelery_library


# import armor


class Item:
    def __init__(self, name, item_type):
        self.__name = name.title()
        self.__item_type = item_type

    class Jewelery:
        def __init__(self, name=''):
            self._name = name.title()
            self.item_type = 'Jewelery'
            self.rarity = rarity.rarity()

        def set_random_jewelery(self, jewelery_type=None):  # jewelery_type 0=rings/1=necklaces/2=earrings
            chosen_metal = random.choice(jewelery_library.metals)
            chosen_gem = random.choice(jewelery_library.gems)
            if jewelery_type is None:
                chosen_type_of_jewelery = random.choice(jewelery_library.type_of_jewelery)
            else:
                chosen_type_of_jewelery = jewelery_library.type_of_jewelery[jewelery_type]

            self._name = str(f'{chosen_metal} {chosen_gem} {chosen_type_of_jewelery}')

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

    class Armor:
        def __init__(self):
            pass
