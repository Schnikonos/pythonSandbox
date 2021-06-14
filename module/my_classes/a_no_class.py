
person = {
    'name': 'John',
    'age': 42
}

group = [person, person]

club = {'members': group, 'type_de_club': 'foot'}


if __name__ == '__main__':
    print(person['name'], person['age'])
    print(group[1]['name'])
    print(club['type_de_club'])
    print(club['member'][0]['age'])
