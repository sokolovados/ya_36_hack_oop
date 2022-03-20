from dataclasses import dataclass


@dataclass
class Thing:
    '''Базовый класс экипировки. '''
    name: str
    protection_boost: float
    attack_boost: float
    health_boost: float


@dataclass
class Weapon(Thing):
    ''' Оружие. Не может добавлять здоровья. Множитель урона = 5 '''
    DAMAGE_COEF = 5

    def __post_init__(self):
        self.attack_boost *= self.DAMAGE_COEF
        self.protection_boost


@dataclass
class Jewelery(Thing):
    ''' Украшения. Не могут добавлять защиту. Множитель здоровья =5 '''
    HEALTH_COEF = 5

    def __post_init__(self):
        self.health_boost *= self.HEALTH_COEF
        self.protection_boost = 0


@dataclass
class Armor(Thing):
    ''' Доспех. Не может добавлять атаку. '''

    def __post_init__(self):
        self.attack_boost = 0


@dataclass
class Boots(Armor):
    ''' Сапоги. Не может добавлять атаку. '''
    pass


@dataclass
class Hat(Armor):
    ''' Головной убор. Не может добавлять атаку. '''
    pass


@dataclass
class Gloves(Armor):
    ''' Перчатки. Не может добавлять атаку. '''
    pass


@dataclass
class Shield(Armor):
    ''' Щит. Не может добавлять атаку. '''
    pass
