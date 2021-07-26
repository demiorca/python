# Задания 4, 5 и 6

from datetime import datetime
from pprint import pprint


class Warehouse:
    def __init__(self):
        self._warehouse = {}

    def to_warehouse(self, equipment, count):
        try:
            if type(count) != int:
                raise OnlyIntInCount('Для указания количества товаров нужно указать число (0-9).')
        except OnlyIntInCount as err:
            print(err)
        else:
            time_of_acceptance = datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
            self._warehouse.update({equipment.model: [equipment.group_name(), count, self, time_of_acceptance]})
            print(f'Оборудование {equipment.model} отправлено на склад в количестве {count} штук. '
                  f'Дата отправки: {time_of_acceptance}.')

    def to_subdivision(self, equipment, subdivision, count):
        try:
            if type(count) != int:
                raise OnlyIntInCount('Для указания количества товаров нужно указать число (0-9).')
        except OnlyIntInCount as err1:
            print(err1)
        else:
            transfer_time = datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
            try:
                if self._warehouse[equipment.model]:
                    if [i for i in self._warehouse[equipment.model]][1] - count < 0:
                        raise NotEnoughItems(f'На складе недостаточно единиц выбранного товара ({equipment.model}).')
                    self._warehouse.update({equipment.model: [equipment.group_name(),
                                                              [i for i in self._warehouse[equipment.model]][1] - count,
                                                              self, transfer_time]})
                print(f'Оборудование {equipment.model} передано в подразделение "{subdivision}" в количестве '
                      f'{count} штук. Дата передачи: {transfer_time}.')
            except NotEnoughItems as err2:
                print(err2)
            except KeyError:
                print(f'Товара {equipment.model} нет на складе')

    def __str__(self):
        return self._warehouse


class OnlyIntInCount(Exception):
    def __init__(self, txt):
        self.txt = txt


class NotEnoughItems(Exception):
    def __init__(self, txt):
        self.txt = txt


class OfficeEquipment:
    def __init__(self, model, colour, max_format, year):
        self.model = model
        self.colour = colour
        self.max_format = max_format
        self.year = year
        self.group = self.__class__.__name__

    def group_name(self):
        return self.group


class Printer(OfficeEquipment):
    def __init__(self, model, colour, max_format, year, printing, pr_speed, pr_resolution):
        super().__init__(model, colour, max_format, year)
        self.printing = printing
        self.pr_speed = pr_speed
        self.pr_resolution = pr_resolution

    def to_print(self, papers):
        return f'Принтер {self.model} печатает {papers} страниц(ы)...'


class Scanner(OfficeEquipment):
    def __init__(self, model, colour, max_format, year, sc_speed, sc_resolution):
        super().__init__(model, colour, max_format, year)
        self.sc_speed = sc_speed
        self.sc_resolution = sc_resolution

    def to_scan(self, papers):
        return f'Сканер {self.model} сканирует {papers} страниц(ы)...'


class MFP(OfficeEquipment):
    def __init__(self, model, colour, max_format, year, printing, pr_speed, sc_speed, copy_speed, pr_resolution,
                 sc_resolution, copy_resolution):
        super().__init__(model, colour, max_format, year)
        self.printing = printing
        self.pr_speed = pr_speed
        self.sc_speed = sc_speed
        self.copy_speed = copy_speed
        self.pr_resolution = pr_resolution
        self.sc_resolution = sc_resolution
        self.copy_resolution = copy_resolution

    def to_print(self, papers):
        return f'МФУ {self.model} печатает {papers} страниц(ы)...'

    def to_scan(self, papers):
        return f'МФУ {self.model} сканирует {papers} страниц(ы)...'

    def to_copy(self, papers):
        return f'МФУ {self.model} копирует {papers} страниц(ы)...'


warehouse = Warehouse()

printer1 = Printer(model='Canon PIXMA TS704', colour='чёрный', max_format='A4', year=2020, printing='цветная',
                   pr_speed=15, pr_resolution='4800x1200')
warehouse.to_warehouse(printer1, 4)
printer2 = Printer(model='Pantum P2200', colour='серый', max_format='A4', year=2019, printing='чёрно-белая',
                   pr_speed=22, pr_resolution='1200x1200')
warehouse.to_warehouse(printer2, '12')
scanner1 = Scanner(model='Epson Perfection V19', colour='чёрный', max_format='A4', year=2020, sc_speed=10,
                   sc_resolution='4800x4800')
warehouse.to_warehouse(scanner1, 22)
scanner2 = Scanner(model='Xerox DocuMate 3220', colour='серый', max_format='A4', year=2018, sc_speed=23,
                   sc_resolution='600x600')
warehouse.to_warehouse(scanner2, 16)
mfp1 = MFP(model='HP LaserJet Pro MFP M28w', colour='белый', max_format='A4', year=2019, printing='чёрно-белая',
           pr_speed=18, sc_speed=18, copy_speed=18, pr_resolution='600x600', sc_resolution='600x600',
           copy_resolution='600x400')
warehouse.to_warehouse(mfp1, 18)
mfp2 = MFP(model='Brother DCP-L2520DWR', colour='чёрный', max_format='A4', year=2018, printing='чёрно-белая',
           pr_speed=26, sc_speed=26, copy_speed=26, pr_resolution='2400x600', sc_resolution='600x2400',
           copy_resolution='600x600')
warehouse.to_warehouse(mfp2, 17)

print()
pprint(warehouse._warehouse)

print()
warehouse.to_subdivision(printer1, 'Финансовый отдел', 8)
warehouse.to_subdivision(scanner1, 'Финансовый отдел', 7)
warehouse.to_subdivision(mfp1, 'Финансовый отдел', 6)
warehouse.to_subdivision(printer2, 'Юридический отдел', 6)
warehouse.to_subdivision(scanner2, 'Юридический отдел', 4)
warehouse.to_subdivision(mfp2, 'Юридический отдел', '2')

print()
pprint(warehouse._warehouse)

print()
print(printer1.to_print(100))
print(scanner1.to_scan(14))
print(mfp1.to_copy(41))
print(mfp1.to_print(10))
print(mfp1.to_scan(4))
print(printer2.to_print(50))
print(scanner2.to_scan(7))
print(mfp2.to_copy(23))
print(mfp2.to_print(5))
print(mfp2.to_scan(2))
