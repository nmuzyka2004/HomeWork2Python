# Задача 10: На столе лежат n монеток. Некоторые из них лежат 
# вверх решкой, а некоторые – гербом. Определите минимальное число 
# монеток, которые нужно перевернуть, чтобы все монетки были 
# повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, 
# которые нужно перевернуть
from random import randint
n = int(input("Введите количество монет: "))
coins = []
count0 = 0
count1 = 0
for i in range(n):
    coins.append(randint(0,1))
print(coins)
for i in range(n):
    if coins[i] == 0:
        count0 +=1
    else: count1 +=1
if count0 < count1:
    min = count0
else: min = count1
print(f"Требуется перевернуть как минимум {min} монет")  