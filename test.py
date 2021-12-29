nmsp_var = {'global':{'a'}, 'foo':{'b'}} #создаём словарь 'пространство-переменная'
prnt_nmsp = {'None':{'global'}, 'global':{'foo'}} #создаём словарь 'родитель-пространство'
var = 'a'
namespace = 'foo'
if var in nmsp_var[namespace]: #проверяем есть ли в пространстве namespace var
    print(namespace) 
else:            
    def get_key(namespace): #функция позволяет узнать ключ по значению 
        no = 0
        for key, value in prnt_nmsp.items(): #перебираем ключи и их значения
            if namespace in value: #если namespace совпадает с значением какого-либо ключа
                if var in nmsp_var[key]: #проверяем есть ли значение var в протсранстве key
                    print(value) #если есть, то возвращаем пространство key
                    no = 1
                    break
                else:
                    k = key #в противном случае вызываем функцию внутри самой себя с аргументом k = key
                    get_key(k)
        if no != 1:
            print('None')
get_key(namespace)