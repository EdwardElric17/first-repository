nmsp_var = {'global':[]} #создаём словарь 'пространство-переменная'
prnt_nmsp = {'None':['global']} #создаём словарь 'родитель-пространство'
for i in range(int(input())):
    cmd, namespace, var = (str(j) for j in input().split()) #вводим значения для переменных cmd, namespace и var 
    if cmd == 'create': #если cmd равно 'create', то создаём пространство namespace внутри протсранства var
        if var not in prnt_nmsp: #проверяем есть ли пространство var в словаре 'родитель-пространство'
            prnt_nmsp[var] = [] #если нет, то создаем его
            nmsp_var[namespace] = []
        if namespace not in nmsp_var:
            nmsp_var[namespace] = []
        prnt_nmsp[var].append(namespace) #добавляем в него пространтсво namespace
    if cmd == 'add': #если cmd равно 'add', то добавляем в пространство namespace переменную var
        if namespace not in nmsp_var:  #проверяем есть ли пространство namespace в словаре 'пространство-переменная'
            nmsp_var[namespace] = [] #если нет, то создаём пространство namespace в словарь 'пространство-переменная'
        nmsp_var[namespace].append(var) #добавляем в неё переменную var
    if cmd == 'get': #если cmd равно 'get', то возвращаем пространство в котором находится var. Если такого пространства нет, возвращаем None
        if var in nmsp_var[namespace]: #проверяем есть ли в пространстве namespace var
            print(namespace) 
            continue
        elif namespace == 'global':
            print('None')
            continue
        else:            
            def get_key(namespace): #функция позволяет узнать ключ по значению 
                for key, value in prnt_nmsp.items(): #перебираем ключи и их значения
                    if namespace in value: #если namespace совпадает с значением какого-либо ключа
                        if var in nmsp_var[key]: #проверяем есть ли значение var в протсранстве key
                            print(key) #если есть, то возвращаем пространство key
                            break
                        else:
                            if key == 'global':
                                print('None')
                            else:    
                                k = key #в противном случае вызываем функцию внутри самой себя с аргументом k = key
                                get_key(k)
        get_key(namespace)