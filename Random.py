from random import randint

def randomlist():
    t = [randint(a, b) for i in range(c)]
    print(t)



a = int(input("Начало диапазона:"))
b = int(input("Конец диапазона:"))
c = int(input("Количество элементов:"))

randomlist()