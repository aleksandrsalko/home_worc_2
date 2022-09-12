# Реализуйте выдачу случайного числа
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time или datetime 
# (миллисекунды или наносекунды) - для задания случайности
# Учтите, что есть диапазон: от(минимальное) и до (максимальное)

from time import time

def time_random():
    return time() - float(str(time()).split('.')[0])

def gen_random_range(min, max):
    return int(time_random() * (max - min) + min)

print(gen_random_range(20,60))