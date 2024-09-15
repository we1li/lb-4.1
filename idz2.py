#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self._normalize()

    @classmethod
    def from_string(cls, time_string):
        try:
            h, m, s = map(int, time_string.split(':'))
            return cls(h, m, s)
        except ValueError:
            print("Неправильный формат времени. Ожидается формат 'HH:MM:SS'.")
            return None

    @classmethod
    def from_seconds(cls, total_seconds):
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return cls(hours, minutes, seconds)

    def _normalize(self):
        """Нормализация времени для корректного представления."""
        if self.seconds >= 60:
            self.minutes += self.seconds // 60
            self.seconds %= 60
        if self.minutes >= 60:
            self.hours += self.minutes // 60
            self.minutes %= 60
        if self.hours >= 24:
            self.hours %= 24

    def to_seconds(self):
        """Перевод времени в общее количество секунд."""
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def to_minutes(self):
        """Перевод времени в минуты с округлением до целого числа."""
        total_seconds = self.to_seconds()
        return round(total_seconds / 60)

    def time_difference(self, other_time):
        """Вычисление разницы между двумя моментами времени в секундах."""
        return abs(self.to_seconds() - other_time.to_seconds())

    def add_seconds(self, seconds):
        """Добавление секунд к текущему времени."""
        total_seconds = self.to_seconds() + seconds
        return Time.from_seconds(total_seconds)

    def subtract_seconds(self, seconds):
        """Вычитание секунд из текущего времени."""
        total_seconds = self.to_seconds() - seconds
        return Time.from_seconds(total_seconds)

    def __eq__(self, other):
        return self.to_seconds() == other.to_seconds()

    def __lt__(self, other):
        return self.to_seconds() < other.to_seconds()

    def __gt__(self, other):
        return self.to_seconds() > other.to_seconds()

    def read(self):
        """Ввод времени с клавиатуры в формате HH:MM:SS."""
        time_string = input("Введите время в формате HH:MM:SS: ")
        new_time = Time.from_string(time_string)
        if new_time:
            self.hours, self.minutes, self.seconds = new_time.hours, new_time.minutes, new_time.seconds

    def display(self):
        """Вывод времени в формате HH:MM:SS."""
        print(f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}")

if __name__ == '__main__':
    # Ввод первого времени с клавиатуры
    print("Введите первое время:")
    time1 = Time()
    time1.read()

    # Ввод второго времени с клавиатуры для сравнения
    print("\nВведите второе время для сравнения:")
    time2 = Time()
    time2.read()

    # Вывод времени
    print("\nПервое время:")
    time1.display()
    print("Второе время:")
    time2.display()

    # Сравнение времени
    print("\nСравнение:")
    if time1 == time2:
        print("Времена равны.")
    elif time1 < time2:
        print("Первое время меньше второго.")
    else:
        print("Первое время больше второго.")

    # Ввод количества секунд для добавления
    seconds_to_add = int(input("\nВведите количество секунд для добавления к первому времени: "))
    new_time = time1.add_seconds(seconds_to_add)
    print(f"\nНовое время после добавления {seconds_to_add} секунд:")
    new_time.display()

    # Ввод количества секунд для вычитания
    seconds_to_subtract = int(input("\nВведите количество секунд для вычитания из первого времени: "))
    new_time = time1.subtract_seconds(seconds_to_subtract)
    print(f"\nНовое время после вычитания {seconds_to_subtract} секунд:")
    new_time.display()

    # Вывод времени в секундах и минутах
    print(f"\nПервое время в секундах: {time1.to_seconds()} секунд")
    print(f"Первое время в минутах (с округлением): {time1.to_minutes()} минут")
