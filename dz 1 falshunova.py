
a = "Фальшунова Анастасия"
print(a)

b = "18"
print("Меня зовут Фальшунова Анастасия, мне ", b," лет")

n= "Фальшунова Анастасия "
n = n * 5
print(n)

a="Впишите ваше имя"
print (a)
b = str(input())
c = "Укажите свой возраст"
print (c)
d = int(input())
print ("Здравствуйте,",b ,"вы слишком стар для использования PyCharm")

c = "Укажите свой возраст"
print (c)
k= int(input())
if k<= 20:
    print ("Тем кому меньше 20 вход в данную программу запрещен")
else:
    print ("Вы слишком молодо выглядите для своих лет")

c = "Введите имя"
print (c)
k= str(input())
print(k[1:-1])

c = "Введите имя"
print (c)
k= str(input())
print(k[::-1])

c = "Введите имя"
print (c)
k= str(input())
print(k[-3:])

a="Впишите ваше имя"
print (a)
b = str(input())
c = "Укажите свой возраст"
print (c)
d = str(input())
h= sum(map(int,str(d)))
d=int(d)
p=1
while (d != 0):
    p = p * (d % 10)
    d = d // 10
print (len(b),h,p)

a="Впишите ваше имя"
print (a)
b = str(input())
b = b.upper()
print (b)

a="Впишите ваше имя"
print (a)
b = str(input())
b = b.lower()
print (b)
