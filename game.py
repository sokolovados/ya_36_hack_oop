from random import choice, randint, uniform
from typing import List, Type, Union

from colorama import Fore

from arena import Arena
from engine import Paladin, Person, Warior
from settings import Settings as S


class EpicGame:
    ''' Основной класс игры. Создает персонажей, предметы, открывает арену'''

    def lets_play(self):
        self.things = self._create_things()
        self.characters = self._create_characters()

        print(Fore.BLUE + 'Подготовка...')
        for character in self.characters:
            character.set_things(self.things)
            print(Fore.LIGHTRED_EX + character.get_equipment())

        if input(
            Fore.LIGHTMAGENTA_EX +
            'Мы готовы сражаться!\n'
            '1) Начинаем!\n2) Я погорячился.Расходимся!\n'
        ) == '1':
            arena = Arena(self.characters)
            arena.battle()

    @staticmethod
    def _create_things() -> List:
        ''' Создает от 10 до 50 рандомных предметов. '''
        result = []
        for i in range(randint(10, 50)):
            name = choice(list(S.THINGS_CATHEGORY.keys()))
            thing_type = S.THINGS_CATHEGORY[name]
            result.append(
                thing_type(
                    name=name,
                    protection_boost=round(
                        uniform(S.MIN, S.MAX_PROTECTION_BOOST), 3
                    ),
                    attack_boost=round(uniform(S.MIN, S.MAX_ATTACK_BOOST), 3),
                    health_boost=round(uniform(S.MIN, S.MAX_HEALTH_BOOST), 3),
                )
            )
        return result

    @staticmethod
    def _create_characters() -> List[Person]:
        ''' Создает 10 рандомных персонажей. '''
        proffesions: List[
            Union[Type[Warior], Type[Paladin]]
        ] = [Warior, Paladin]
        return [
            choice(proffesions)(
                name=choice(S.CHARACTER_NAMES),
                base_health=round(
                    uniform(S.MIN_BASE_HEALTH, S.MAX_BASE_HEALTH), 3),
                base_protection=round(
                    uniform(S.MIN_BASE_PROTECTION, S.MAX_BASE_PROTECTION), 3),
                base_attack_damage=uniform(
                    S.MIN_BASE_ATTACK, S.MAX_BASE_ATTACK),
            )
            for i in range(9)
        ]


if __name__ == '__main__':
    game = EpicGame()
    game.lets_play()
