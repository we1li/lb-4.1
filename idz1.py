#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Pair:
    def __init__(self, first, second):
        # Инициализация объекта Pair с двумя целыми числами: first и second.
        # Проверка, что оба числа являются целыми.
        if not isinstance(first, int) or not isinstance(second, int):
            raise ValueError("Поля first и second должны быть целыми числами.")
        # Проверка, что first меньше second.
        if first >= second:
            raise ValueError("Поле first должно быть меньше поля second.")
        self.first = first
        self.second = second

    def read(self):
        # Чтение значений first и second с клавиатуры.
        try:
            self.first = int(input("Введите первое число (левая граница диапазона): "))
            self.second = int(input("Введите второе число (правая граница диапазона, не включается): "))
            # Проверка, что first меньше second.
            if self.first >= self.second:
                raise ValueError("Левая граница должна быть меньше правой границы.")
        except ValueError as e:
            print(f"Ошибка ввода: {e}")

    def display(self):
        # Отображение текущей пары чисел.
        print(f"Пара чисел: [{self.first}, {self.second})")

    def rangecheck(self, number):
        """Проверка, принадлежит ли число number интервалу [first, second)."""
        return self.first <= number < self.second

def make_pair(first, second):
    """Функция для создания объекта типа Pair."""
    try:
        return Pair(first, second)
    except ValueError as e:
        print(f"Ошибка создания объекта: {e}")
        return None

if __name__ == '__main__':
    # Демонстрация работы программы

    # Создание объекта Pair
    pair = make_pair(10, 20)
    if pair:

        # Ввод новой пары чисел с клавиатуры.
        print("\nВвод новой пары с клавиатуры:")
        pair.read()
        pair.display()

        # Проверка числа, введенного пользователем, на принадлежность интервалу.
        number_to_check = int(input("\nВведите число для проверки принадлежности интервалу: "))
        print(f"Число {number_to_check} в интервале [{pair.first}, {pair.second}): {pair.rangecheck(number_to_check)}")
