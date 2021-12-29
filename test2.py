nmsp_var = {'global':{'a'}, 'foo':{'b'}} #создаём словарь 'пространство-переменная'
prnt_nmsp = {'None':{'global'}, 'global':{'foo'}} #создаём словарь 'родитель-пространство'
var = 'a'
namespace = 'foo'
def get_key(namespace): #функция позволяет узнать ключ по значению 
    for value in prnt_nmsp.values(): #перебираем ключи и их значения
        print(value)
        if namespace in value: #если namespace совпадает с значением какого-либо ключа
            print('True')
        else:
            print('False')
get_key('foo')