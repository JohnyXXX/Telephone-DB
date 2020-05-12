import unittest

from module import TelephoneDB, Person


class TestDB(unittest.TestCase):
    def setUp(self):
        self.db = TelephoneDB()
        self.persons = (
            Person('+70000000001', 'Иванов Иван Иванович', 'Ленина, 45, 23'),
            Person('+70000000002', 'Прекрасная Елена Павловна', 'Кутузова, 6, 123'),
            Person('+70000000003', 'Вольная Ольга Александровна', 'Парковая, 50, 82'),
            Person('+70000000004', 'Гордый Михаил Львович', 'Центральный, 142, 73'),
        )
        self.words_for_find = (
            'Ольга',
            'Ивано',
            'Центральный',
            '+70000000002',
            'вна',
        )
        self.edit_persons = (
            Person('+70000000003', 'Невольная Мария Викторовна', 'Лесная, 12, 5'),
            Person('+70000000003', 'ГыГыГыГЫ', 'Луговая, 26, 20'),
        )
        self.remove_persons = (
            '+70000000001',
            'ГыГы',
        )


class TestAddPersons(TestDB):
    def test_add_person(self):
        self.db.add(self.persons[0])
        self.assertIn(self.persons[0].key, self.db.db.keys())
        self.assertIn(self.persons[0].value, self.db.db.values())

    def test_add_persons(self):
        for person in self.persons:
            self.db.add(person)
            self.assertIn(person.key, self.db.db.keys())
            self.assertIn(person.value, self.db.db.values())


class TestExistPersons(TestDB):
    def test_exist_person(self):
        self.db.add(self.persons[1])
        self.assertRaises(self.db.add(self.persons[1]))

    def test_exist_persons(self):
        for person in self.persons:
            self.db.add(person)
            self.assertRaises(self.db.add(person))


class TestFindPersons(TestDB):
    def test_find_persons(self):
        for person in self.persons:
            self.db.add(person)
        for word in self.words_for_find:
            self.assertGreater(len(self.db.find(word)), 0)


class TestEditPerson(TestDB):
    def test_edit_persons(self):
        for person in self.persons:
            self.db.add(person)
        for person in self.edit_persons:
            self.db.edit(person)
            self.assertIn(person.key, self.db.db.keys())
            self.assertIn(person.value, self.db.db.values())


class TestRemovePerson(TestDB):
    def test_remove_persons(self):
        for person in self.persons:
            self.db.add(person)
        for person in self.edit_persons:
            self.db.edit(person)
        for person in self.remove_persons:
            self.db.remove(person)
            self.assertNotIn(person, self.db.db.keys())
            self.assertNotIn(person, self.db.db.values())


if __name__ == '__main__':
    unittest.main()
