from sys import stderr


class TelephoneExist(Exception):
    """Класс исключения если тнлефон уже имеется в БД"""
    pass


class TelephoneDB(dict):
    """
    Класс БД на основе списка. Должен добавлять,
    искать, изменять и удалять из БД.
    """

    def __init__(self):
        self.db = {}

    def __person_exist_check(self, person):
        for i in self.db.keys():
            if person.key == i:
                return True

    def add(self, person):
        if self.__person_exist_check(person) is True:
            raise TelephoneExist('Запись с таким номером уже существует!')
        else:
            self.db.update({person.key: person.value})

    def find(self, request):
        result = {}
        for key, value in self.db.items():
            if (
                    request.lower() in key.lower()) or (
                    request.lower() in value[0].lower() or (
                    request.lower() in value[1].lower())
            ):
                result.update({key: value})
        return result

    def edit(self, data):
        # print('data', type(data), data)
        for key in self.db.keys():
            if data.key in key:
                self.db.update({data.key: data.value})

    def remove(self, request):
        for key, value in self.db.items():
            if (
                    request.lower() in key.lower()) or (request.lower() in value[0].lower()) or (
                    request.lower() in value[1].lower()
            ):
                return self.db.pop(key)


class Person(TelephoneDB):
    """
    Конструктор для "Персоны" и представление для печати.
    """

    def __init__(self, telephone, fullname, address):
        self.value = (fullname, address)
        self.key = telephone

    def __repr__(self):
        return f'Телефон: {self.key}, ФИО: {self.value[0]}, Адрес: {self.value[1]}'


if __name__ == '__main__':
    db = TelephoneDB()
    for add_person in (
            Person('+70000000001', 'Иванов Иван Иванович', 'Ленина, 45, 23'),
            Person('+70000000002', 'Прекрасная Елена Павловна', 'Кутузова, 6, 123'),
            Person('+70000000003', 'Вольная Ольга Александровна', 'Парковая, 50, 82'),
            Person('+70000000004', 'Гордый Михаил Львович', 'Центральный, 142, 73'),
    ):
        try:
            db.add(add_person)
            print('Add success:', add_person)
        except Exception as e:
            print(type(e), add_person, file=stderr)

    for exist_person in (
            Person('+70000000002', 'Прекрасная Елена Павловна', 'Кутузова, 6, 123'),
            Person('+70000000004', 'Гордый Михаил Львович', 'Центральный, 142, 73'),
    ):
        try:
            db.add(exist_person)
            print('Add exist:', exist_person)
        except Exception as e:
            print(e, exist_person, file=stderr)

    for find_person in (
            'Ольга',
            'Ивано',
            'Центральный',
            '+70000000002',
            'вна',
    ):
        try:
            p = db.find(find_person)
            print(f'{find_person} find in:', p)
        except Exception as e:
            print(type(e), find_person, file=stderr)

    for edit_person in (
            Person('+70000000003', 'Невольная Мария Викторовна', 'Лесная, 12, 5'),
            Person('+70000000003', 'ГыГыГыГЫ', 'Луговая, 26, 20'),
    ):
        try:
            db.edit(edit_person)
            print(len(db.db), db.db)
        except Exception as e:
            print(type(e), edit_person, file=stderr)

    for remove_person in (
            '+70000000001',
            'ГыГы',
    ):
        try:
            db.remove(remove_person)
            print(len(db.db), db.db)
        except Exception as e:
            print(type(e), remove_person, file=stderr)
