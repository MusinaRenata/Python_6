# Задача 1. Дано натуральное число N. Найдите значение выражения: N + NN + NNN. N 
# может быть любой длины.
# N = 132: 132 + 132132 + 132132132 = 132264396


number = int(input("Введите число N:  "))
temp = str(number)
t1 = temp + temp
t2 = temp + temp + temp
comp = number + int(t1) + int(t2)
print(t1, t2, comp)