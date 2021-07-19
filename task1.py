# Задание 1

class Date:
    """
    Введите дату в формате 'день-месяц-год'
    """
    def __init__(self, date):
        self.date = str(date)

    def __str__(self):
        return self.date

    @classmethod
    def extract_date(cls, date):
        num_date = []
        for d in date.split('-'):
            num_date.append(int(d))
        return num_date

    @staticmethod
    def validation_date(date):
        date = date.split('-')
        if 1 <= int(date[0]) <= 31:
            pass
        else:
            print('Исправьте день')
        if 1 <= int(date[1]) <= 12:
            pass
        else:
            print('Исправьте месяц')
        if 1 <= int(date[2]) <= 2021:
            pass
        else:
            print('Исправьте год')
        if 1 <= int(date[0]) <= 31 and 1 <= int(date[1]) <= 12 and 1 <= int(date[2]) <= 2021:
            return 'Дата введена корректно'
        else:
            return 'Дата введена некорректно'

    """
    или:
    
    @staticmethod
    def validation_date(date):
        date = date.split('-')
        if 1 <= int(date[0]) <= 31 and 1 <= int(date[1]) <= 12 and 1 <= int(date[2]) <= 2021:
            return 'Дата введена корректно'
        else:
            return 'Исправьте дату. День - от 1 до 31, месяц - от 1 до 12, год - от 1 до 2021.'
    """


my_date = Date('19-07-2021')
print(my_date)
print(Date.extract_date('19-07-2021'))
print(Date.validation_date('19-07-2021'))
print()
print(Date.validation_date('99-99-9999'))
