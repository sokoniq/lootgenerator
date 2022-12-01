import random
import weapons
jump = '\\n'
types_of_melee_armor = ['armor.melee_headgear','armor.melee_chestgear','armor.melee_legs','armor.melee_gloves','armor.melee_boots','armor.melee_shields']
armor_names = ['head','chest','legs','gloves','boots','shields']
armor_index = 0
melee_materials = 'armor.melee_materials'
bracket_valid = '{valid_types}'
type_a = '{armor_type}'
type_m = '{material}'
for armor_type in types_of_melee_armor:
    print(f'''
class {armor_names[armor_index].title()}:
    def __init__(self, name=None):
        self.__name = name.title()
        self.item_type = '{armor_names[armor_index]} armor'        
    
    def set_random_melee_{armor_names[armor_index]}_armor(self, armor_type=None):
        material = random.choice({melee_materials})
        if armor_type is None:
            armor_type = random.choice({armor_type})
        elif armor_type.lower() in {armor_type}:
            pass
        else:
            print('{jump}Invalid type of {armor_names[armor_index]} armor')
            valid_types = ' {jump}'.join(str(types) for types in {armor_type})
            print(f'Valid types:{jump}{bracket_valid}.title()')
            return

        self.__name = str(f'{type_m} {type_a}')
        return self.__name
    def set_custom_melee_{armor_names[armor_index]}_armor(self):
        material = str(input(f'Select a material: '))
        armor_type = str(input(f'Select a {armor_names[armor_index]} armor: '))
        if material.lower() in {melee_materials}:
            pass
        else:
            print('{jump}Invalid component')
            valid_types = ' {jump}'.join(str(materials) for materials in {melee_materials})
            print(f'Valid components:{jump}{bracket_valid}.title()')
            return

        if armor_type.lower() in {armor_type}:
            pass
        else:
            print('{jump}Invalid type of {armor_names[armor_index]} armor')
            valid_types = ' {jump}'.join(str(types) for types in {armor_type})
            print(f'Valid types:{jump}{bracket_valid}.title()')
            return
        self.__name = str(f'{type_m} {type_a}')
        return self.__name.title()''')
    armor_index += 1