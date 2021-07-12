# Задание 3

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}
        print(f'Имя: {name}, фамилия: {surname}, должность: {position.lower()}, '
              f'оклад: {wage} кредитов, премия: {bonus} кредитов')


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'Имя и фамилия сотрудника на должности "{self.position}": {self.name} {self.surname}'

    def get_total_income(self):
        return f'Доход сотрудника на должности "{self.position}" с учётом премии: {sum(self._income.values())} кредитов'


worker_1 = Position("Джеймс", "Кирк", "Командующий", 100000, 50000)
print(worker_1.get_full_name())
print(worker_1.get_total_income())

print()

worker_2 = Position("С'чн-Т'гай", "Спок", "Офицер по науке", 80000, 30000)
print(worker_2.get_full_name())
print(worker_2.get_total_income())
