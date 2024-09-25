def print_params(a = 1, b = 'строка', c = True):
    print (a,b,c)
print('1. Функция с параметром по умолчанию')
print_params ()
print_params(b=25)
print_params(c=[1, 2, 3])
print('')

print('2. Рапаковка параметров')
values_list = [1, True, 'Текст']
value_dict = {'a': 5, 'b': True, 'c': 'Словарь'}
print_params(*values_list)
print_params(**value_dict)
print('')

print('3. Распаковка + отдельные параметры')
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)