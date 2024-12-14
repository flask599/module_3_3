print('Задача "Распаковка')
print('----------------------')

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c )
values_list = [5, True, 'Bug']
values_dict = {'a':False, 'b': 85, 'c': 'Debug'}
values_list_2 = [25.1, 'string']
values_dict_2 = {'c': [1, 2, 3]}
print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
#print_params(*values_list, **values_dict) # в этом случае выходит ошибка
# print_params() got multiple values for argument 'a'/
# #как понимаю из-за большего количества параметров чем ожидает функция
print_params(56,*values_list_2)
print_params(*values_list_2, **values_dict_2)