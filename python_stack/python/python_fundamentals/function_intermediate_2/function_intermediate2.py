x = [[5, 2, 3], [10, 8, 9]]

students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
]

sport_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Ronney'],
}

print(sport_directory['basketball'][2])

z = [{'x': 10, 'y': 20}]

x[1][0] = 15
students[0]['first_name'] = 'Bryant'
sport_directory['soccer'][0] = 'Andres'
z[0]['y'] = 30

print(x)
print(students)
print(sport_directory)
print(z)


students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'},
]


def iterateDictionary(some_list):
    for d in some_list:
        for k, value in d.items():
            print (f"{k} - {value}")

iterateDictionary(students)

def iterateDictionary2(key_name, some_list):
    for i in some_list:
        print(i[key_name])

iterateDictionary2('last_name', students)


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dalles', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Micheal', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon'],
}

def printInfo(some_dict):
    for k in some_dict:
        print(f"{len(some_dict[k])} {k.upper()}")
        for i in some_dict[k]:
            print(i)

printInfo(dojo)