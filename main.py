class TelephoneExist(Exception):
    pass


class TelephoneDB(list):
    """
    Класс БД на основе списка. Должен добавлять,
    искать, изменять и удалять из БД.
    """

    db = []

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
        for row in self.db:
            if (request in row.fullname) or (request in row.address) or (request in row.telephone):
                return row

    def edit(self, fullname, address, telephone):
        for row in self.db:
            if telephone in row.telephone:
                row.fullname = fullname
                row.address = address

    def remove(self, request):
        for row in self.db:
            if (request in row.fullname) or (request in row.address) or (request in row.telephone):
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
    a_person = Person('Иванов Иван Иванович', 'Ленина, 45, 23', '+70000000001')
    b_person = Person('Прекрасная Елена Павловна', 'Кутузова, 6, 123', '+70000000002')
    c_person = Person('Вольная Ольга Александровна', 'Парковая, 50, 82', '+70000000003')
    d_person = Person('Гордый Михаил Львович', 'Центральный, 142, 73', '+70000000004')
    e_person = Person('', '', '')
    f_person = Person('Гордый Михаил Львович', 'Центральный, 142, 73', '+70000000004')
    # print(a_person)
    # print(b_person)
    # print(c_person)
    # print(d_person)
    db = TelephoneDB()
    db.append(a_person)
    db.append(b_person)
    db.append(c_person)
    db.append(d_person)
    db.append(e_person)
    # db.append(f_person)
    print(len(db.db), db.db)
    print(db.find('Ольга'))
    print(db.find('Иванович'))
    print(db.find('Центральный'))
    print(db.find('+70000000002'))
    db.remove('+70000000001')
    print(len(db.db), db.db)
    db.edit('Невольная Мария Викторовна', 'Лесная, 12, 5', '+70000000003')
    print(len(db.db), db.db)
