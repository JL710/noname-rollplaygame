import Weapon, Heroguild
from random import randint
from typing import Literal


class Figure:
    def __init__(self, name: str, guild: Heroguild.HeroGuild, weapon: Weapon.Weapon=Weapon.Weapon("hand", 1),  fight: int=randint(8, 16), 
    skill: int=randint(8, 16), intelligence: int=randint(8, 16), crafting: int=randint(8, 16)):
        # error check


        # set attributes
        self.__name = name
        self.__weapon = weapon
        self.__lifepoints = 30
        self.__fight = fight
        self.__skill = skill
        self.__intelligence = intelligence
        self.__crafting = crafting
        self.__guild = guild

    def attack(self) -> int:
        if randint(1, 20) <= self.__fight:
            return randint(1, 6) + self.__weapon.get_strength()
        self.__lifepoints -= 5
        return 0

    def pickpocket(self) -> bool:
        if randint(1, 20) <= self.__crafting:
            self.__guild.set_xp(10)
            return True
        return False

    def puzzle(self) -> bool:
        if randint(1, 20) <= self.__intelligence:
            self.__guild.set_xp(self.__intelligence * 2)
            return True
        return False

    def balance(self) -> bool:
        if randint(1, 20) <= self.__skill:
            self.__guild.set_xp(2)
            return True
        else:
            self.__lifepoints -= 10
            return False

    def set_attr(self, attr: Literal["fight", "skill", "crafting", "crafting", "intelligence", "weapon"]):
        match attr:
            case "fight":
                if self.__fight < 16:
                    self.__fight += 1
                    return True
            case "skill":
                if self.__skill < 16:
                    self.__skill += 1
                    return True
            case "crafting":
                if self.__crafting < 16:
                    self.__crafting += 1
                    return True
            case "intelligence":
                if self.__intelligence < 16:
                    self.__intelligence += 1
                    return True
            case "weapon":
                pass # TODO: shit here
        return False