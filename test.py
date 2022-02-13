import os
import os.path
from pathlib import Path

# print(os.path.relpath('qxbwf.txt'))
# path = os.path.relpath('main/ddiqo/qxbwf.txt')
# def slash_change(path):
#     a = path.replace('\\','/')
#     print(a)

# slash_change(path)

# file = Path('main', 'ddiqo', 'qxbwf.txt')
# wave = file.relative_to(Path('main'))
# print(wave)
print(os.chdir('main')) 
print(os.getcwd())