nmsp_var = {'global':{'a'}, 'foo':{'b'}} #создаём словарь 'пространство-переменная'
prnt_nmsp = {'None':{'global'}, 'global':{'foo'}} #создаём словарь 'родитель-пространство'
var = 'a'
namespace = 'foo'
def get_key(namespace): #функция позволяет узнать ключ по значению 
    for key, value in prnt_nmsp.items(): #перебираем ключи и их значения
        if value == namespace: #если namespace совпадает с значением какого-либо ключа
            if var in nmsp_var[key]: #проверяем есть ли значение var в протсранстве key
                print(key) #если есть, то возвращаем пространство key
            else:
                k = key #в противном случае вызываем функцию внутри самой себя с аргументом k = key
                get_key(k)
        elif value == 'None':
            print('None')
get_key(namespace)