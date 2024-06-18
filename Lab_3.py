import csv
from datetime import date, datetime

class Person:
    def __init__(self, surname, first_name, birth_date, nickname=''):
        self.surname = surname
        self.first_name = first_name
        self.nickname = nickname
        self.birth_date = self._parse_birth_date(birth_date)

    def _parse_birth_date(self, birth_date_str):
        year, month, day = map(int, birth_date_str.split('-'))
        return date(year, month, day)

    def get_age(self):
        today = date.today()
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return str(age)

    def get_fullname(self):
        return f"{self.surname} {self.first_name}"

p = Person('Murphy', 'Nicolas', '2000-12-31')
print(p.get_fullname())
print(p.get_age())


def modifier(filename):
    persons = []
    
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            person = Person(
                surname=row['surname'],
                first_name=row['first_name'],
                birth_date=row['birth_date'],
                nickname=row.get('nickname', '')
            )
            persons.append(person)
    
    modified_data = []
    for person in persons:
        data = {
            'surname': person.surname,
            'first_name': person.first_name,
            'nickname': person.nickname,
            'birth_date': person.birth_date.isoformat(),
            'fullname': person.get_fullname(),
            'age': person.get_age()
        }
        modified_data.append(data)

    fieldnames = ['surname', 'first_name', 'nickname', 'birth_date', 'fullname', 'age']
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(modified_data)
