#! /usr/bin/env python
# -*- coding: utf-8 -*-

#  Пример использования скрипта из командной строки: 'python run_reservoir.py 1000 10 30 15'


#  Импортируем создфнные классы из соседнего файла
from reservoir_and_rivers import Reservoir
from reservoir_and_rivers import River_flow_in
from reservoir_and_rivers import River_flow_out
#  Импротируем библиотеку sys
import sys


initial_storage = float(sys.argv[1]) #  Ввод параметров из команды python run_reservoir.py 1000 10 30 15 (1000)
discharge_riv1 = float(sys.argv[2]) #  Ввод параметров из команды python run_reservoir.py 1000 10 30 15 (10)
discharge_riv2 = float(sys.argv[3]) #  Ввод параметров из команды python run_reservoir.py 1000 10 30 15 (30)
number_of_days = float(sys.argv[4]) #  Ввод параметров из команды python run_reservoir.py 1000 10 30 15 (15)

reservoir = Reservoir(init_stor=initial_storage) #  Создаем объект резервуара из класса на основе класса Reservoir

river1 = River_flow_in(reservoir=reservoir) #  Создаем объект реки 1 из класса на основе класса River_flow_in. Объект reservoir созданный выше
river2 = River_flow_out(reservoir=reservoir) #  Создаем объект реки 2 из класса на основе класса River_flow_out. Объект reservoir созданный выше

river1.inflow(discharge=discharge_riv1, days=number_of_days) # Вызываем метод inflow у объекта река1
river2.outflow(discharge=discharge_riv2, days=number_of_days) #  Вызываем метод outflow у объекта река1

print(reservoir.storage) #  Вывод результата - итоговый объем воды в резервуаре
