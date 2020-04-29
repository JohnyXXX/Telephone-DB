class TelephoneDB:
    pass


class Person:
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
    print(a_person)
    print(b_person)
    print(c_person)
    print(d_person)
