# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
dirnames=['dir_'+str(d) for d in range(1,10)]
def make9dirs(names):
    for dirn in names:
        os.mkdir(os.path.join(os.getcwd(),dirn))

def rm9dirs(names):
    for dirn in names:
        os.rmdir(os.path.join(os.getcwd(),dirn))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

with os.scandir(".") as it:
    for entry in it:
        if entry.is_dir():
            print(entry.name)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import shutil
def copycurrent():
    src = os.path.realpath(__file__)
    dst = src[:-3:]+'_copy.py'
    shutil.copy(src,dst)
copycurrent()