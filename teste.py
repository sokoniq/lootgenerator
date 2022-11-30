import jewelery_library


def set_custom_jewelery(self, chosen_metal='', chosen_type_of_jewelery='', chosen_gem=None):
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
