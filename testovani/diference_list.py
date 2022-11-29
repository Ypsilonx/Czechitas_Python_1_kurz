name = 'Guido'


class MyClass:
    name = 'Raymond'
    list_1 = [name] * 3
    list_2 = [name for i in range(3)]


print(MyClass.list_1)
# ---> ['Raymond', 'Raymond', 'Raymond']

print(MyClass.list_2)
# ---> ['Guido', 'Guido', 'Guido']
