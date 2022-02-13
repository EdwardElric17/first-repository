import os
import os.path
import shutil
import pathlib 

#1
# def search_dir(main):   #Функция проверяет является ли указанный файл папкой
#     for i in os.listdir(main):
#         if os.path.isdir(path_of_folder(i)) == True:
#             print(i)
#             check_folder(i)
#             search_dir(i)

# #2
# def path_of_folder(fold):
#     return os.path.abspath(fold)[46::]

#3
# def check_folder(folder):   #Функция проверяет есть ли в папке файл с расшерением '.py'
#     for i in os.listdir(folder):    
#         if i[-3::] == '.py':
#             a = (os.path.abspath(folder))[46::]
#             massive_dir_1.append(a)   #Если есть, добавляет папку в массив с другими такими же папками
#             return massive_dir_1

massive_dir_1 = []
massive_dir_2 = []

def slash_change(path):    #Функция меняет в названии пути '\' на '/'
    a = path.replace('\\','/')
    massive_dir_2.append(a)

a = os.walk('main')
for i in a:
    for j in i[2]:
        if j[-3::] == '.py':
            massive_dir_1.append(i[0])
            break

for i in massive_dir_1:
    slash_change(i)

with open('test.txt', 'w') as ouf:
    for i in massive_dir_2:
        ouf.write(i +'\n')

# os.chdir('sample/a')
# print(path_of_folder('a'))

# print(os.getcwd())    #текущий путь
# print(os.listdir())   #вывод всех файлов в пути
# print(os.path.exists())   #проверяет есть ли файл в пути
# print(os.path.isdir())    #проверяет является ли директорией 
# print(os.path.isfile())   #проверяет является ли файлом
# print(os.path.abspath())  #абсолютный путь до файла
# print(os.chdir())    #переход в нужную директорию
# print(os.walk())    #показывает все файлы в директории

# os.chdir('sample/a/c')
# print(check_folder('a'))

# print(check_folder(''))

# print(os.listdir('sample'))
# print((os.getcwd())[46::])]

# print(os.path.isdir('sample/a'))

#print(os.path.abspath('sample'))