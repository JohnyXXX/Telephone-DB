class TelephoneExist(Exception):
    """Класс исключения если тнлефон уже имеется в БД"""
    pass


class TelephoneDB(list):
    """
    Класс БД на основе списка. Должен добавлять,
    искать, изменять и удалять из БД.
    """

    def __init__(self):
        self.db = []

    def __person_exist_check(self, person):
        for i in self.db:
            if person.telephone == i.telephone:
                return True

    def append(self, person):
        if self.__person_exist_check(person) is True:
            raise TelephoneExist('Запись с таким номером уже существует!')
        else:
            self.db.append(person)

    def find(self, request):
        result = []
        for row in self.db:
            if (
                    request.lower() in row.fullname.lower()) or (request.lower() in row.address.lower()) or (
                    request.lower() in row.telephone.lower()
            ):
                result.append(row)
        return result

    def edit(self, data):
        for row in self.db:
            if data[2] in row.telephone:
                row.fullname = data[0]
                row.address = data[1]

    def remove(self, request):
        for row in self.db:
            if (
                    request.lower() in row.fullname.lower()) or (request.lower() in row.address.lower()) or (
                    request.lower() in row.telephone.lower()
            ):
                return self.db.remove(row)


class Person:
    """
    Конструктор для "Персоны" и представление для печати.
    """

    def __init__(self, fullname, address, telephone):
        self.fullname = fullname
        self.address = address
        self.telephone = telephone

    def __repr__(self):
        return f'ФИО: {self.fullname}; Адрес: {self.address}; Телефон: {self.telephone}'


if __name__ == '__main__':
    db = TelephoneDB()
    for add_person in (
            Person('Иванов Иван Иванович', 'Ленина, 45, 23', '+70000000001'),
            Person('Прекрасная Елена Павловна', 'Кутузова, 6, 123', '+70000000002'),
            Person('Вольная Ольга Александровна', 'Парковая, 50, 82', '+70000000003'),
            Person('Гордый Михаил Львович', 'Центральный, 142, 73', '+70000000004'),
    ):
        try:
            db.append(add_person)
            print('Add success: ', add_person)
        except Exception as e:
            print(type(e), add_person)

    for exist_person in (
            Person('Прекрасная Елена Павловна', 'Кутузова, 6, 123', '+70000000002'),
            Person('Гордый Михаил Львович', 'Центральный, 142, 73', '+70000000004'),
    ):
        try:
            db.append(exist_person)
            print('Add exist: ', exist_person)
        except Exception as e:
            print(e, 'Not add: ', exist_person)

    for find_person in (
            'Ольга',
            'Ивано',
            'Центральный',
            '+70000000002',
            'вна',
    ):
        try:
            p = db.find(find_person)
            print(f'{find_person} find in: ', p)
        except Exception as e:
            print(type(e), find_person)

    for edit_person in (
            ('Невольная Мария Викторовна', 'Лесная, 12, 5', '+70000000003'),
            ('ГыГыГыГЫ', 'Луговая, 26, 20', '+70000000003'),
    ):
        try:
            db.edit(edit_person)
            print(len(db.db), db.db)
        except Exception as e:
            print(type(e), edit_person)

    for remove_person in (
            '+70000000001',
            'ГыГы',
    ):
        try:
            db.remove(remove_person)
            print(len(db.db), db.db)
        except Exception as e:
            print(type(e), remove_person)
