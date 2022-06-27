

class Weapon:
    def __init__(self, name: str, strength: int):
        # check errors
        if strength > 12 or strength < 1:
            raise ValueError(f"Strength can be a value between 1 and 12. Your value is {strength}.")

        # set attributes
        self.__name = name
        self.__strength = strength

    def abuse(self) -> bool:
        """decreases the stregth of the weapon and returns if the Weapon is broke"""
        self.__strength -= 1
        if self.__strength < 1:
            return True
        else:
            return False

    def get_strength(self):
        return self.__strength

