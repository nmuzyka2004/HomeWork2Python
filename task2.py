# Задача 12: Петя и Катя – брат и сестра. Петя – студент, 
# а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

# x+y=s =>  y=s-x
# x*y=p  =>  x*(s-x)=p  => s*x-x^2=p => x^2-s*x+p=0  => 
# Дискриминант D = (-s)^2 - 4*1*p
# x1 = (s+D^0,5)/2*1   x2 = (s-D^0,5)/2*1 

s = int(input("Введите значение суммы чисел: "))
p = int(input("Введите значение произведения чисел: "))
d = (-1 * s) ** 2 - 4 * p
x1 = (s + d ** 0.5) / 2
x2 = (s - d ** 0.5) / 2
y1 = s - x1
y2 = s - x2
print(f"Это числа: {round(x1)} и {round(y1)} либо {round(x2)} и {round(y2)}")