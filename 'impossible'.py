"""
str.find('') - индекс первого вхождения или -1
    .rfind() - справа
    .lfind() - слева

str.index('') - индекс первого вхождения или ValueError

str.startswith('') - проверяет начинается ли строка с другой строки. Возвращает True или False

str.endswith('') - проверяет заканчивается ли строка с другой строки. Возвращает True или False

str.count('') - количество вхождений в строку 

str.lower() - преобразует в нижний регистр

str.upper() - преобразует в верхний региср

str.replace('1', '2') - заменяет один элемент на другой

str.split(sep=None, maxsplit=-1) - возвращает список элементов разделенных сепарэйтом
                                   максимальное количество делений поумолчанию неограничено 
    .rsplit() - справа
    .lsplit() - слева
    
'sep'.join() - объединяет элементы строки в строку разделённую sep
"""

s = str(input())
a = str(input())
b = str(input())
count = 0

while True:
    if s.find(a) != -1 and count != 1000:
        count += 1
        s = s.replace(a, b)
    elif count == 1000:
        print('Impossible')
        break
    else:
        print(count)
        break
       