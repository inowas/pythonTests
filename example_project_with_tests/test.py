#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from reservoir_and_rivers import Reservoir
from reservoir_and_rivers import River_flow_in
from reservoir_and_rivers import River_flow_out

#  Пример использования скрипта из командной строки: 'python test.py'

class Test_geoimage(unittest.TestCase):

    def setUp(self):
        """
        Обязательная функция. Вводим параметры и создаем объекты как в run_reservoir.py
        """
        self.initial_storage = 1000 #  Ввод параметров из команды python run_reservoir.py 1000 10 30 15 (1000)
        self.discharge_riv1 = 10 #  Ввод параметров из команды python run_reservoir.py 1000 10 30 15 (10)
        self.discharge_riv2 = 30 #  Ввод параметров из команды python run_reservoir.py 1000 10 30 15 (30)
        self.number_of_days = 15 #  Ввод параметров из команды python run_reservoir.py 1000 10 30 15 (15)

        self.reservoir = Reservoir(init_stor=self.initial_storage) #  Создаем объект резервуара из класса на основе класса Reservoir
        self.river1 = River_flow_in(reservoir=self.reservoir) #  Создаем объект реки 1 из класса на основе класса River_flow_in. Объект reservoir созданный выше
        self.river2 = River_flow_out(reservoir=self.reservoir) #  Создаем объект реки 2 из класса на основе класса River_flow_out. Объект reservoir созданный выше
        self.river1.inflow(discharge=self.discharge_riv1, days=self.number_of_days) # Вызываем метод inflow у объекта река1
        self.river2.outflow(discharge=self.discharge_riv2, days=self.number_of_days) #  Вызываем метод outflow у объекта река1

    def tearDown(self):
        """
        Обязательная функция. Очищаем все
        """
        self.initial_storage = None
        self.discharge_riv1 = None
        self.discharge_riv2 = None
        self.number_of_days = None

        self.reservoir = None
        self.river1 = None
        self.river2 = None

    def test_image_properities(self):
        """
        Тест. Проверяет равен ли расчитанный объем резервуара (reservoir.storage) тому что мы ожидаем получить (initial_storage + discharge_riv1 * number_of_days - discharge_riv2 * number_of_days)
        """
        self.assertEqual(self.reservoir.storage,
                         self.initial_storage + self.discharge_riv1 * self.number_of_days - self.discharge_riv2 * self.number_of_days)

if __name__ == '__main__':
    unittest.main()
