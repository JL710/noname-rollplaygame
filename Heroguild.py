from Figure import Figure
from typing import Literal


class HeroGuild:
    def __init__(self, name: str, heros: list):
        self.__name = name
        self.__heros = [Figure(hero) for hero in heros]
        self.__xp = 0

    def raising(self, attribute: Literal["fight", "skill", "crafting", "crafting", "intelligence", "weapon"]):
        if self.__xp >= 100:
            # TODO: do shit with the hero

            self.__xp -= 100
            return True
        return False

    def set_xp(self, amount: int):
        """will add the amount to the guilds xp"""
        self.__xp += amount

