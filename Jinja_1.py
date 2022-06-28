from jinja2 import Template

# name = "Федор"
# age = 24
# tm = Template("Привет мне {{ a }}, меня зовут {{ n }}.")
# msg = tm.render(n=name, a=age)
#
# msg2 = f'Привет {name}'
#
#
# print(msg, msg2, sep='\n')


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# per = Person("Федор", 33)
#
# tm = Template("Привет мне {{ p.name }}, меня зовут {{ p.age }}.")
# msg = tm.render(p=per)
#
# print(msg)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def getName(self):
#         return self.name
#
#     def getAge(self):
#         return self.age
#
#
# per = Person("Федор", 33)
#
# tm = Template("Привет мне {{ p.getAge() }}, меня зовут {{ p.getName() }}.")
# msg = tm.render(p=per)
#
# print(msg)

#
# per = {'name': 'Федор', 'age': 34}
#
# tm = Template("Привет мне {{ p['age'] }}, меня зовут {{ p['name'] }}.")
# msg = tm.render(p = per)
#
# print(msg)


# cities = [{'id': 1, 'city': 'Москва'},
#     {'id': 1, 'city': 'Москва'},
#     {'id': 1, 'city': 'Москва'},
#     {'id': 1, 'city': 'Москва'},
#     {'id': 1, 'city': 'Москва'}]
