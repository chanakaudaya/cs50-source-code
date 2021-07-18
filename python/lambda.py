people = [
    {"name":"harry", "home":"slyhterine"},
    {"name":"chanaka", "home":"sw19"},
    {"name":"saneli", "home":"seeduwa"}
]

def f(person):
    return person["home"]

people.sort(key=f)
print(people)