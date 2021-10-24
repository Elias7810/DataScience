import pandas as pd
import datetime as dt
from itertools import zip_longest

pd.set_option('display.max_columns', None)
pd.options.display.width = 1000


# Определяет ошибку, которая будет появляться, когда будут нарушены
# смысловые соотношения проекта (например, дата поступления техники позже даты
# ее выдачи в подразделения, дата поступления/выдачи позже текущей даты и т. п. )
class BaseError(Exception):
    pass


class Equipment:
    instances = []

    def __init__(self, price, brand, serial, equip_type):
        self.price = price
        self.brand = brand
        self.serial = serial  # серийный номер изделия
        self.equip_type = equip_type
        self.instances.append(self)

    def __iter__(self):
        for el in self.instances:
            return el

    # Метод проверяет соотвествие вводиммой информации о номенклатуре требуемому
    # типу данных и может использоваться как самостоятельно, так и в других
    # методах
    @staticmethod
    def equip_val(name):
        if type(name.price) == str:
            raise BaseError(f"Цена '{name.price}' должна быть выражена числом")
        if type(name.brand) != str or type(name.equip_type) != str:
            raise BaseError(f"Марка '{name.brand}' и тип оргтехники"
                            f"'{name.equip_type}'должны быть в текстовом формате")
        else:
            return name

    # Метод выводит справочник номенклатуры оргтехники (указаны все использованные
    # или планируемые к использованию в проекте типы оргтехники со всеми признаками
    # независимо от того,есть данная оргтехника на складе или нет)
    @staticmethod
    def assort_list():
        # Формирование исходного списка
        list1 = []
        for obj in Equipment.instances:
            Equipment.equip_val(obj)
            list1.append(type(obj).__name__)
            list1.append(obj.brand)
            list1.append(obj.equip_type)
            list1.append(obj.price)
            list1.append(obj.serial)
        # Разделение списка на список списков для pandas
        i_ = iter(list1)
        list1 = list(zip_longest(i_, i_, i_, i_, i_))
        list1 = [list(el) for el in list1]
        # Формирование таблицы в  pandas
        title = ["Изделие", "Марка", "Тип", "Цена, р.", "Серийный номер"]
        equip_list = pd.DataFrame(data=list1, columns=title)
        # Нумерация позиций с 1, а не с 0
        equip_list = equip_list.reset_index(drop=True)
        equip_list.index += 1
        print()
        print("             Справочник номенклатуры оргтехники")
        print()
        print(equip_list)


class Printer(Equipment):

    def __init__(self, price, brand, serial, equip_type, print_speed):
        super().__init__(price, brand, serial, equip_type)
        self.print_speed = print_speed

    def __str__(self):
        return (f"{self.equip_type.capitalize()} принтер марки {self.brand}, "
                f"скорость печати - {self.print_speed} стр./мин.,\n"
                f"серийный номер - {self.serial}, цена - {self.price} р./шт.")


class Scanner(Equipment):

    def __init__(self, price, brand, serial, equip_type, resolution):
        super().__init__(price, brand, serial, equip_type)
        self.resolution = resolution

    def __str__(self):
        return (f"{self.equip_type.capitalize()} сканер марки {self.brand}, "
                f"разрешение- {self.resolution} dpi.,\n"
                f"серийный номер - {self.serial}, цена - {self.price} р./шт.")


class Copier(Equipment):

    def __init__(self, price, brand, serial, equip_type, paper_type):
        super().__init__(price, brand, serial, equip_type)
        self.paper_type = paper_type

    def __str__(self):
        return (f"{self.equip_type.capitalize()} ксерокс марки {self.brand}, "
                f"тип бумаги- {self.paper_type},\n"
                f"серийный номер - {self.serial}, цена - {self.price} р./шт.")


class Storage:
    instances = []

    def __init__(self):
        self.date_of_coming = None
        self.date_of_transfer = None
        self.transfer_dept = None
        self.equip = []
        self.transfer = []
        self.instances.append(self)

    def __iter__(self):
        for el in self.equip:
            return el

    def __str__(self):
        for el in self.equip:
            return (f"Объeкт {type(el).__name__} {el.brand}, цена - {el.price} р., "
                    f"оприходован на склад {self.date_of_coming.strftime('%d %m %y')}")

    # Приходование материала на склад с встроенной валидацией вводимых данных
    def add_equip(self, equipment, date_of_coming):
        try:
            raw_date = dt.datetime.strptime(date_of_coming, '%d %m %Y')
        except:
            raise BaseError("Дата поступления должна быть вида: 'ДД ММ ГГГГ'")
        if raw_date > dt.datetime.now():
            raise BaseError(f"Дата поступления '{date_of_coming}' "
                            f"не может быть позже текущей даты")
        self.date_of_coming = raw_date
        self.equip.append(equipment)

    # Передача материалов со склада с встроенной валидацией вводимых данных
    def transfer_equip(self, equipment, date_of_transfer, transfer_dept):
        try:
            raw_date_t = dt.datetime.strptime(date_of_transfer, '%d %m %Y')
        except:
            raise BaseError("Дата поступления должна быть вида: 'ДД ММ ГГГГ'")
        if self.date_of_coming:
            if raw_date_t < self.date_of_coming:
                raise BaseError(f"Дата списания '{date_of_transfer}' "
                                f"не может быть ранее даты поступления "
                                f"'{self.date_of_coming.strftime('%d %m %Y')}'")
        else:
            raise BaseError("Данная позиция на складе отсутствует")
        if raw_date_t > dt.datetime.now():
            raise BaseError(f"Дата поступления '{date_of_transfer}' "
                            f"не может быть позже текущей даты")
        self.date_of_transfer = raw_date_t
        self.transfer_dept = transfer_dept

    # Вспомогательный метод, выводящий полный список оргтехники, находящейся на складе
    # используется в методе Turnover
    @staticmethod
    def full_info():
        # Формирование исходного списка
        list2 = []
        for obj in Storage.instances:
            if obj.date_of_transfer == None:
                list2.append(obj.date_of_coming.strftime('%d %b %Y'))
                for el in obj.equip:
                    list2.append(type(el).__name__)
                    list2.append(el.brand)
                    list2.append(el.serial)
                    list2.append(el.price)
        # Разделение списка на список списков для pandas
        i_ = iter(list2)
        list2 = list(zip_longest(i_, i_, i_, i_, i_))
        list2 = [list(el) for el in list2]
        # Формирование таблицы в  pandas
        title = ["Дата поступления", "Изделие", "Марка", "Серийный номер", "Цена, р.", ]
        full_st = pd.DataFrame(data=list2, columns=title)
        return full_st

    # Вспомогательный метод, выводящий полный список оргтехники, переданной со склада
    # используется в методе Turnover
    @staticmethod
    def transfer_info():
        # Формирование исходного списка
        list3 = []
        for obj in Storage.instances:
            if obj.date_of_transfer:
                list3.append(obj.date_of_coming.strftime('%d %b %Y'))
                list3.append(obj.date_of_transfer.strftime('%d %b %Y'))
                for el in obj.equip:
                    list3.append(type(el).__name__)
                    list3.append(el.brand)
                    list3.append(el.serial)
                    list3.append(el.price)
                list3.append(obj.transfer_dept)
        # Разделение списка на список списков для pandas
        i_ = iter(list3)
        list3 = list(zip_longest(i_, i_, i_, i_, i_, i_, i_))
        list3 = [list(el) for el in list3]
        # Формирование таблицы в  pandas
        title = ["Дата поступления", "Дата передачи", "Изделие", "Марка", "Серийный номер", "Цена, р.", "Куда передано"]
        transfer_st = pd.DataFrame(data=list3, columns=title)
        return transfer_st

    # Основной метод, выводящий всю информацию по складу. Почти 1С))
    @staticmethod
    def turnover():
        Storage.full_info()
        Storage.transfer_info()
        table = pd.merge(Storage.full_info(), Storage.transfer_info(),
                         on=('Серийный номер', "Изделие", "Дата поступления", "Марка", "Цена, р."), how='outer')
        table = table.fillna("-")
        table = table.sort_values('Дата поступления')
        table = table.reset_index(drop=True)
        table.index += 1
        print()
        print("                             Обороты по складу оргтехники")
        print()
        print(table)
        tot_num = table[table["Дата передачи"] == "-"]["Марка"].count()
        tot_sum = table[table["Дата передачи"] == "-"]["Цена, р."].sum()
        scan_num = table[(table["Дата передачи"] == "-") & (table["Изделие"] == "Scanner")]["Марка"].count()
        scan_sum = table[(table["Дата передачи"] == "-") & (table["Изделие"] == "Scanner")]["Цена, р."].sum()
        prin_num = table[(table["Дата передачи"] == "-") & (table["Изделие"] == "Printer")]["Марка"].count()
        prin_sum = table[(table["Дата передачи"] == "-") & (table["Изделие"] == "Printer")]["Цена, р."].sum()
        cop_num = table[(table["Дата передачи"] == "-") & (table["Изделие"] == "Copier")]["Марка"].count()
        cop_sum = table[(table["Дата передачи"] == "-") & (table["Изделие"] == "Copier")]["Цена, р."].sum()
        print()
        print(f"На складе находятся {tot_num} единиц оргтехники на общую сумму "
              f"{tot_sum} р., в т. ч.:\nсканеров - {scan_num} шт. на сумму "
              f"{scan_sum} р., \nпринтеров - {prin_num} шт. на сумму {prin_sum}"
              f" р., \nксероксов - {cop_num} шт. на сумму {cop_sum} р.")

    # Исходные данные по номенклатуре


printer1 = Printer(7500, "HP107a", "sn123475", "лазерный", 20)
printer2 = Printer(4000, "CanonPixma", "sn368GH", "струйный", 8)
printer3 = Printer(7500, "HP107a", "sn123476", "лазерный", 20)
print(printer2)

scanner1 = Scanner(8000, "EpsonV19", "sn45421", "планшетный", "4800*4800")
scanner2 = Scanner(8000, "Canon208", "sn554FD", "протяжный", "600*600")
print(scanner2)

xerox1 = Copier(14500, "Xerox3025", "271165", "черно-белый", "A4")
xerox2 = Copier(138000, "Kyocera2553", "kc346", "цветной", "A3, A4")
xerox3 = Copier(138000, "Kyocera2553", "kc346", "цветной", "A3, A4")
print(xerox3)

# Оформление передачи оргтехники на склад производится с помощью создания
# нового экземпляра класса Storage с именем, аналогичным имени в номенклатуре,
# но с добавлением буквы s в начале, и путем применения к этому экземпляру
# методов add_equip и transfer_equip
s_printer1 = Storage()
s_printer1.add_equip(printer1, "22 10 2020")
s_printer2 = Storage()
s_printer2.add_equip(printer2, "21 10 2020")
s_printer3 = Storage()
s_printer3.add_equip(printer3, "18 10 2020")
print(s_printer3)
s_scanner1 = Storage()
s_scanner1.add_equip(scanner1, "8 10 2020")
s_scanner2 = Storage()
s_scanner2.add_equip(scanner2, "12 10 2020")
s_xerox1 = Storage()
s_xerox1.add_equip(xerox1, "8 10 2020")
s_xerox2 = Storage()
s_xerox2.add_equip(xerox2, "18 10 2020")
s_xerox3 = Storage()
s_xerox3.add_equip(xerox3, "24 10 2021")
s_printer1.transfer_equip(printer1, "23 10 2020", "бухгалтерия")
s_printer2.transfer_equip(printer2, "24 10 2020", "отдел кадров")
s_xerox3.transfer_equip(xerox3, "24 10 2021", "отдел кадров")
# Вывод отчетных форм
Equipment.assort_list()
Storage.turnover()
# Хотелось бы в развитие проекта добавить возможность количественного и
# стоимостного учета по группам однородных объектов, возможность
# формирования остатков по складу на конкретную дату, формирования
# отдельных отчетных форм по приходу и отпуску оргтехники (приходный ордер,
# требование-накладная), но, к сожалению, на это не хватило времени((
