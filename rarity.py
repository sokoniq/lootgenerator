import random


def rarity():
    rarity_chance = {"Bad": 0.20, "Normal": 0.50, "Good": 0.2, "Great": 0.07, "Amazing": 0.03, "Perfect": 0.01}
    return random.choices(population=list(rarity_chance.keys()), weights=list(rarity_chance.values()))
