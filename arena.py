from random import sample
from typing import List, Union
from time import sleep

from colorama import Fore

from engine import Paladin, Warior


class Arena:
    '''Арена для битв. Для открытия нужна комманда бойцов(героев). '''

    def __init__(self, characters: List[
        Union[Warior, Paladin]
    ]) -> None:
        self.characters = characters

    def fight(
        self, character1: Union[Warior, Paladin],
        character2: Union[Warior, Paladin]
    ) -> None:
        ''' Бой между двумя героями. Оканчивается смертью одного из персонажей'''
        print(Fore.WHITE + '\n'+'#'*30)
        print(f'{Fore.YELLOW} {character1.name} VS {character2.name}')
        while character1.is_alife and character2.is_alife:
            sleep(0.2)
            print('-'*100)
            self.single_hit(
                'Атака',
                character1,
                character2
            )
            if character1.is_alife and character2.is_alife:
                self.single_hit(
                    'Контратака',
                    character2,
                    character1)
        else:
            if not character1.is_alife:
                self.characters.remove(character1)
            else:
                self.characters.remove(character2)

    def single_hit(
        self, attack_type: str,
        attacker: Union[Warior, Paladin],
        defender: Union[Warior, Paladin]
    ) -> None:
        '''
        Одиночный удар. Для удобочитаемости
        разделяется на Атаку и Контратаку.
        '''
        attack = defender.input_damage(
            attacker.name, attacker.current_attack_damage
        )
        if attack_type == 'Атака':
            print(f'{Fore.RED} ({attack_type}) {attack}')
        else:
            print(f'{Fore.GREEN} ({attack_type}) {attack}')

    def battle(self) -> Union[Warior, Paladin]:
        ''' Инициация битвы. Сталкивает персонажей попарно. '''
        while len(self.characters) > 1:
            self.fight(*(sample(self.characters, k=2)))
        print(Fore.CYAN + '\n'+'#'*30)
        print(f'{self.characters[0].name} IS WIN')
        print('#'*30)
        return self.characters[0]
