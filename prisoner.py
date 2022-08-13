import random


class Prisoner:
    def __init__(self):
        self.__counter = False
        self.__switched = False

    def visit_room(self, is_switch_on):
        # ha szamlalo es felkapcsolt lampa
        if self.__counter and is_switch_on:
            return True
        # ha nem szamlalo es lekapcsolt lampa es meg nem kapcsolt
        if not self.__counter and not is_switch_on and not self.__switched:
            self.__switched = True
            return True
        return False

    # szamlalo kinevezese
    def assign_counter(self):
        self.__counter = True

    def is_counter(self):
        return self.__counter


class Prison:
    def __init__(self, prisoners):
        self.__prisoners = [Prisoner() for _ in range(prisoners)]
        self.__count = 0
        self.__days = 0
        self.__switch = False

    def __send_prisoner(self, index):
        self.__days += 1
        prisoner = self.__prisoners[index]
        # ha elso nap, szamlalot kinevezzuk
        if self.__days == 1:
            prisoner.assign_counter()
        # ha a rab hozzanyult kapcsolohoz
        if prisoner.visit_room(self.__switch):
            self.__switch = not self.__switch
            # ha a szamlalo hozzanyult kapcsolohoz
            if prisoner.is_counter():
                self.__count += 1

    def prison_break(self):
        while self.__count < len(self.__prisoners)-1:
            # random rab valasztasa
            index = random.randint(0, len(self.__prisoners) - 1)
            self.__send_prisoner(index)
        return self.__days




