import random

rarity = {"Bad": 0.200, "Normal": 0.550, "Good": 0.150, "Great": 0.07, "Amazing": 0.03, "Perfect": 0.01}
rarity_keys = list(rarity.keys())
rarity_value = list(rarity.values())
random.choices(population=rarity_keys, weights=rarity_value)

