from copy import copy
from random import choice, randint, uniform
from typing import List

from settings import Settings as S
from things import Thing


class Person:
    ''' Базовый персонаж. '''

    def __init__(
        self,
        name: str,
        base_health: float,
        base_protection: float,
        base_attack_damage: float,
    ):
        self.name = name
        self.base_health = base_health
        self.base_protection = base_protection
        self.base_attack_damage = base_attack_damage
        self.equipments: List[Thing] = []
        self.equipment_types: List[str] = []

        self.current_health: float = copy(base_health)
        self.finalProtection: float = copy(base_protection)
        self.current_attack_damage: float = copy(base_attack_damage)
        self.is_alife: bool = True

        self.EQUIPMENT_MSG = '{name} взял {equipments}!'

    def set_things(self, things: List[Thing]) -> None:
        ''' Берет случайные вещи из предложенного списка экипировки. '''
        for i in range(
            randint(S.MIN_THINGS, S.MAX_THINGS)
        ):
            thing = choice(things)
            # Исключаем дублирование экипы одного типа.
            if thing.__class__.__name__ not in self.equipment_types:
                self._add_thing(thing)
        self.get_equipment()

    def _add_thing(self, thing) -> None:
        ''' Одевает одну вещь. Прибавляет статы. '''
        self.equipments.append(thing)
        self.equipment_types.append(thing.__class__.__name__)
        self.current_health += thing.health_boost
        self.finalProtection += thing.protection_boost
        self.current_attack_damage += thing.attack_boost

    def input_damage(self, attacker_name: str, damage: float) -> str:
        ''' Подсчет входящего урона. '''
        dodge = uniform(0.1, 1)
        clear_damage = (
            damage - damage * self.base_protection
        ) * dodge
        protected_damage = damage - clear_damage
        if not clear_damage > self.current_health:
            self.current_health -= clear_damage
            return (f'{attacker_name} наносит удар по '
                    f'{self.name} на {clear_damage:.2f} урона. '
                    f'{protected_damage:.2f} урона заблокировано.')
        else:
            self.is_alife = False
            return (f'{attacker_name} наносит смертельный урон '
                    f'{clear_damage:.2f} по {self.name}. {self.name} умирает.')

    def get_equipment(self) -> str:
        ''' Информация о полученной экипировке. '''
        equipments = ', '.join(
            [
                equipment.name for equipment in self.equipments
            ]
        )
        return self.EQUIPMENT_MSG.format(
            name=self.name,
            equipments=equipments
        )

    def __repr__(self):
        return f'{self.__class__.__name__}{self.__dict__}'


class Paladin(Person):
    ''' Палладин. Имеет удвоенные статы здоровья и защиты '''

    def __init__(
        self,
        name: str,
        base_health: float,
        base_protection: float,
        base_attack_damage: float,
    ):
        base_health *= 2
        base_protection *= 2
        super().__init__(
            name,
            base_health,
            base_protection,
            base_attack_damage
        )


class Warior(Person):
    '''Воин. Имеет удвоенную атаку. '''

    def __init__(
        self,
        name: str,
        base_health: float,
        base_protection: float,
        base_attack_damage: float,
    ):
        base_attack_damage *= 2
        super().__init__(
            name,
            base_health,
            base_protection,
            base_attack_damage
        )
