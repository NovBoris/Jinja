from jinja2 import Template

# cars = [{'models': 'Ауди', 'price': 23000},
#     {'model': 'Шкода', 'price': 17300},
#     {'model': 'Вольво', 'price': 44300},
#     {'model': 'Фольксваген', 'price': 21300}
# ]

# tpl = "Суммарная цена автомобилей {{ cs | sum(attribute='price') }}"
# tm = Template(tpl)
# msg = tm.render(cs=cars)
#
# print(msg)

# tpl = "Суммарная цена автомобилей {{ cs | max(attribute='price') }}"
# tm = Template(tpl)
# msg = tm.render(cs=cars)
#
# print(msg)

# tpl = "Суммарная цена автомобилей {{ (cs | max(attribute='price')).model }}"
# tm = Template(tpl)
# msg = tm.render(cs=cars)
#
# print(msg)

# tpl = "Случайны авто {{ cs | random }}"
# tm = Template(tpl)
# msg = tm.render(cs=cars)
#
# print(msg)
#
# tpl = 'Замена {{ cs | replace("o", "O") }}'
# tm = Template(tpl)
# msg = tm.render(cs=cars)
#
# print(msg)

# persons = [{'name': 'Алексей', 'old': 18, 'weight': 78.5},
#     {'name': 'Николай', 'old': 27, 'weight': 82.3},
#     {'name': 'Иван', 'old': 33, 'weight': 94.0},
# ]
#
# tpl = '''
# {%- for u in user %}
# {%- filter lower %}{{u.name}}{% endfilter %}
# {% endfor -%}
# '''
#
# tm = Template(tpl)
# msg = tm.render(user=persons)
#
# print(msg)


# html = '''
# {% macro input (name, value='', type='text', size=20) -%}
#     <input type="{{ type }} name="{{ name }}" value="{{ value|e }}" size={{ size }}">
# {%- endmacro %}
#
# <p>{{ input('username') }}
# <p>{{ input('email') }}
# <p>{{ input('password') }}
# '''
#
# tm = Template(html)
# msg = tm.render()
#
# print(msg)

# html = '''
# {% macro list_users(list_of_user) -%}
# <ul>
# {% for u in list_of_user -%}
#     <li>{{u.name}} {{caller(u)}}
# {%- endfor %}
# </ul>
# {%- endmacro %}
#
# {% call(user) list_users(users) %}
#     <ul>
#     <li>age: {{user.old}}
#     <li>weight: {{user.weight}}
#     </ul>
# {% endcall -%}
#
#
# '''
#
# tm = Template(html)
# msg = tm.render(users=persons)
#
# print(msg)

# {% call(user) list_users(user) %}
#     <ul>
#     <li>age: {{u.name}} {{caller(u)}}
#     <li>weight: {{user.weight}}
#     </ul>
# {% endcall -%}
