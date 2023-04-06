import random
def f1():
    n = []
    for i in range(5):
        n.append(random.randint(1, 10))
    c = int(input("введите число 1-10 : "))
    if c in n:
        print("вы угадали число!!!")
    else:
        print("неправильно.попробуй еще раз")
    print("список чисел : " + str(n))

def f2():
    n = []
    for i in range(10):
        n.append(random.randint(1, 10))
    print(*filter(lambda x: n.count(x) > 1, n))

def f3():
    w = ("пн", "вт", "ср", "чт", "пт", "сб", "вс")
    n = int(input("сколько дней выходных? "))
    if n == 0:
        print("вы работяга, у вас нет выходных")
        print("работать : ", *w)
    else:
        print("вы отдыхаете: ", *w[-n:])
        print("вы работаете: ", *w[:-n])

def f4():
    s = ""
    s1 = ["бан", "со", "ли", "хан", 'хван']
    s2 = ['юн', 'пак', 'о', 'шрэк', 'чо']
    s = tuple(s1[:5] + s2[:5])
    print("первый список: ", *s1)
    print("второй список: ", *s2)
    print("новый кортеж: ", *sorted(s))
    print("длина кортежа: ", len(s))
    print(s.count('бан'))
f4()