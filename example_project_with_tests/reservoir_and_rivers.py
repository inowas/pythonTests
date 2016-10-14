#! /usr/bin/env python
# -*- coding: utf-8 -*-

class Reservoir(object):
    """
    Класс Резервуар. Имеет один обязательны парпметр - объем воды
    """
    def __init__(self, init_stor):
        self.storage = init_stor

class River_flow_in(object):
    """
    Класс Река втекающая. Имеет параметр - резервуар в который втекает,
    расход воды и время
    и метод - увеличивать объем воды в нем
    """
    def __init__(self, reservoir):
        self.reservoir = reservoir # Здесь будет объект резервуара
    def inflow(self, discharge, days): # Метод inflow требует 2 параметра - время и расход
        self.reservoir.storage = self.reservoir.storage + discharge * days # Перерасчет объема в резервуаре по формуле

class River_flow_out(object):
    """
    Класс Река вытекающая. Имеет параметр - резервуар из которого вытекает,
    расход воды и время
    и метод - уменьшать объем воды в нем
    """
    def __init__(self, reservoir):
        self.reservoir = reservoir # Здесь будет объект резервуара
    def outflow(self, discharge, days): # Метод outflow требует 2 параметра - время и расход
        self.reservoir.storage = self.reservoir.storage - discharge * days # Перерасчет объема в резервуаре по формуле
