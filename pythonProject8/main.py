# import turtle

"""class Human:
    @staticmethod
    def walk():
        print("Walking")

    @staticmethod
    def stand():
        print("Standing")


class Woman(Human):
    @staticmethod
    def ramp_walk():
        print("Ramp Walking")

    @staticmethod
    def walk():
        print("I am unable to walk")


human1 = Human
# human1.walk()
human1.name = "Arun"
# print(human1.name)
human1.name = 'Sama'
# print(human1.name)
woman1 = Woman
woman1.walk()
woman1.ramp_walk()"""
# import sys

'''try:
    t = turtle.Turtle()

    s = int(input("Enter the number: "))

    t.forward(s)
    t.right(90)

    t.forward(s)
    t.right(90)

    t.forward(s)
    t.right(90)

    t.forward(s)
    t.right(90)

except ModuleNotFoundError:
    print("Hello World")'''

'''def human(a, b):
    return a + b


num = human(2, 3)
print(num)'''

'''def return_greeting():
    return "Arun Sama"


return_greeting()'''

'''def palindrome(s):
    return s == s[::-1]


s = input("Please Enter the Word to check it is a Palindrome: ")
ans = palindrome(s)

if ans:
    print("yes")
else:
    print("No")'''

'''n = int(input("Enter the number: "))
a = 0
b = 1
if n == 1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(c)'''

'''num = 5
i = 0
while i <= num:

    i += 1
    if i == 3:
        break

    print(i)'''

'''def addsub(x, y):
    c = x + y
    d = x - y
    return c, d


result = addsub(5, 4)
result1 = addsub(10, 5)
print(result)
print(result1)'''

'''lst = []
for i in range(10):
    name = input("Enter the name : ")
    lst.append(name)
print(lst)
for j in lst:
    if len(j) < 5:
        continue
    else:
        print(j)'''

'''def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even += 1
            print([i])
        else:
            odd += 1
            print([i])
    return even, odd


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(count(lst))'''

'''num = int(input("Enter the number: "))
a = 0
b = 1
if num == 1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(2, num):
        c = a + b
        a = b
        b = c
        print(c)'''

'''def fact(n):
    mul = 1
    for i in range(1, n + 1):
        mul = mul * i
        return mul


n = int(input("Enter the number: "))
fact(n)'''

# recursion factorial
"""def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


n = int(input("Enter the number : "))
print(fact(n))"""

'''def fact(n):
    if n <= 1:
        return n
    else:
        return fact(n - 1) + fact(n - 2)


n_terms = int(input("Enter the number: "))
if n_terms <= 0:
    print("Invalid Input")
else:
    print("Fibonacci Series :")
    for i in range(n_terms):
        print(fact(i))'''

'''sys.setrecursionlimit(1500)

print(sys.getrecursionlimit())

def fun():
    print(f"Helo World")
    fun()


#fun()'''

'''num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

fun = list(map(lambda a: a % 2 == 0, num))

print(fun)'''

'''my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list = list(map(lambda a: a %2 == 0, my_list))
print(new_list)'''

'''a = 100


def method():
    global a
    a = 60
    print(a)


a = 120
print(a)
method()'''

'''def fun(n):
    """this i the world
    and we take """
    return n ** 2


print(fun.__doc__)
print(fun(3))'''


class Arun:
    def age(self):
        print("Hello World")


arun = Arun()

arun.age()
Arun.age(arun)
