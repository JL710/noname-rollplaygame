from Figure import Figure
from Weapon import Weapon
from typing import Literal, Union, List


class HeroGuild:
    def __init__(self, name: str, heros: list):
        self.__name = name
        self.__heros = [Figure(hero) for hero in heros]
        self.__xp = 0

    def raising(self, attribute: List[Union[Literal["fight", "skill", "crafting", "crafting", "intelligence"], Weapon]]):
        # check error
        for attr in attribute:
            if type(attr) != Weapon and attr not in ["fight", "skill", "crafting", "crafting", "intelligence"]:
                raise ValueError(f"{attr} is not a valid attribute.")
        
        # do the upgrade
        if self.__xp >= 100:
            for hero in self.__heros:
                hero.set_attr(attribute)
            
            self.__xp -= 100
            return True
        return False

    def set_xp(self, amount: int):
        """will add the amount to the guilds xp"""
        self.__xp += amount

