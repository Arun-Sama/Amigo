"""
def multiplication(num1,num2):
    product = num1*num2
    if product <= 1000:
        return product

    else:
        return num1+num2


result = multiplication(20,30)
print("The result is ", result)

result = multiplication(50,30)
print("The result is ", result)
"""

'''previous_num = 0

for i in range(1,11):
    current_num = i
    print(previous_num+current_num)
    previous_num = i'''

'''data = input()

x = list(data)

for i in x[1::3]:
    print(i)'''

'''data = input()

x = len(data)
print(x-1)

for i in range(0,x,2):
    print(data[i])'''
'''
x = int(input())
y = int(input())
print(x*y)'''
'''
print("My ", " Name ", " Is ", " James ", sep='1234')
num = 15
print('%o' % num)
'''

'''num = 23.1235657757
print('%.3f' % num)'''

'''numbers = []
for i in range(0,5):
    item = float(input())
    numbers.append(item)

print(numbers)'''

'''str1,str2,str3 = input().split()
print(str1)
print(str2)
print(str3)'''

'''totalmoney = 3000
quantity = 3
price = 450
print(format(f"I have {totalmoney} dollars so i can buy {quantity} football for {price:.2f} dollars"))
'''

'''name1, name2, name3 = input().split()
print(f'Result is: {name1} {name2} {name3}')
'''

'''numbers = int(input())
item = []
for i in range(numbers):
    result = input()
    item.append(result)
print(item)
'''

"""previous_num = 0
for i in range(1,10):
    current_num = i
    result = previous_num+current_num
    previous_num = i
    print(result)"""

'''name = input()
for i in name[0::2]:
    print(i)'''

'''for num in reversed(range(4)):
    for i in range(num):
        print(num,end=" ")
    print()'''

'''row = "*"
numbers = int(input())
for i in range(numbers):
    for num in range(i+1):
        print(row,end=" ")
    print()'''

'''def char_range(char1,char2):
    for i in range(ord(char1),ord(char2)+1):
        yield (i)

for letter in char_range('a','z'):
    print(chr(letter),end=' , ')
'''

'''def first_and_last_same(number_list):
    ("The give list: ",number_list)

    frist_number=number_list[0]
    last_number=number_list[-1]

    if frist_number == last_number:
        return True
    else:
        return False

number_x=[1,2,3,4,5,6,2,10]
print(first_and_last_same(number_x))'''

'''given_list = [5,10,12,15,23,24,25,34,35]
num =[]
for i in given_list:
    if i % 5 ==0:
        num.append(i)
print(num)'''

'''sampleList = [10, 20, 30, 40, 50]
print(sampleList[-2])
print(sampleList[-5:-1])'''

'''list1 = [100, 200, 300, 400, 500]
list1.reverse()
print(list1)'''

'''list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
result = [x+y for x ,y in zip(list1,list2)]
print(result)'''

'''numbers = [1, 2, 3, 4, 5, 6, 7]
my_list = []
for i in numbers:
    result = i**2
    my_list.append(result)
print(my_list)'''

'''list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
result = [i+j for i in list1 for j in list2]
print(result)'''

'''list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for i,j in zip(list1,list2[::-1]):
    print(i,j)'''

'''list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
res = list(filter(None, list1))
print(res)'''

'''num = int(input())
for i in range(1,num):
    for j in range(i):
        print(i,end=" ")
    print()'''

'''
#palindrome
numbers = int(input())
result = int(str(numbers)[::-1])
if numbers == result:
    print("Yes. given number is palindrome number")
else:
    print("No. given number is not palindrome number")'''

'''
def palindrome(number):
    orginal_number = number
    reverse_number = 0
    while number>0:
        remainder = number %10
        reverse_number = (reverse_number*10)+remainder
        number = number//10

    if orginal_number == reverse_number:
        print("Palindrome")
    else:
        print("Not palindrome")

        
palindrome(121)
palindrome(125)'''

'''
# leap year
num = int(input())
if (num %400 ==0) or (num % 4 == 0 and num % 100 != 0):
    print("yes")

else:
    print("No")'''

'''list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

empty_result = []

for i in list1:
    if i % 2 != 0:
        empty_result.append(i)
for j in list2:
    if j % 2 == 0:
        empty_result.append(j)

print(empty_result)'''

'''number = 7356
while number>0:
    digit=number %10
    number = number//10
    print(digit,end=" ")'''

'''numbers = int(input())
tax_payable = 0

if numbers <= 10000:
    tax_payable = 0'''

'''num = int(input())
for i in range(1,num):
    for j in range(1,num):
        print(i*j,end=" ")
    print()'''

'''row = "*"
#num = int(input())
for i in range(6,0, -1):
    for j in range(0, i -1):
        print('*', end=' ')
    print(" ")'''

'''def exponent(base, exp):
    num = exp

    result = 1
    while num > 0:
        result = result * base
        num = num - 1
    print(result)


exponent(5, 4)
exponent(2, 5)'''

'''for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()'''

'''num = int(input())
s= 0
for i in range(1,num):
    s = i+s
    print(s)'''

'''num = int(input())
s = 0
for i in range(1,11):
    s = num*i
    print(s)'''

'''
numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    if i >= 500:
        break
    if i % 5 == 0 and i <= 150:
        print(i)
        '''
'''for i in range(1,6):
    for j in range(6-i,0,-1):
        print(j,end=" ")
    print()
'''

'''list1 = [10, 20, 30, 40, 50]

for i in list1[::-1]:
    print(i)'''

'''for i in range(-10,0,1):
    print(i)'''

'''for i in range(5):
    print(i)
else:
    print("Done!")'''

'''for num in range(25, 50 + 1):
    # if num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0:
     #   print(num)
    for j in range(2,10):
        if num %j==0:
            break
    else:
        print(num)'''

'''num = 0
num1 = 1
for i in range(6):
    print(num, end=" ")
    result = num + num1
    num = num1
    num1 = result'''

'''num = 1
for i in range(1,6):
    num= num*i
    print(num)'''

'''num = '76542'
for i in num[::-1]:
    print(i,end="")'''

'''numbers = 76542
reverse_number = 0
while numbers > 0:
    remainder = numbers % 10
    #print(remainder)
    reverse_number = (reverse_number*10)+remainder
    #print(reverse_number)
    numbers=numbers//10
    print(reverse_number)'''

'''my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in my_list[1::2]:
    #if i %20==0:
        print(i,end=" ")'''

'''for i in range(1,6):
    #c= i*i*i
    print("Current Number is :" ,i, " and the cube is ", {i*i*i})'''

'''start = 2
seq=0
for i in range(0,5):
    seq += start
    print(seq, end="+")
    start = start*10+2
print("\nSum of above series is:", seq)
'''

'''for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()
for k in range(1,5)[::-1]:
    for l in range(k):
        print("*",end="")
    print()'''

'''def person( name, age):
    print(name, age)


person("Arun", 15)'''

'''def func1(*args):
    for i in args:
        print(i)


func1("no",1.234,45)'''

'''def calculation(a, b):
    add = a + b
    sub = a - b
    return add, sub


print(calculation(40, 10))'''

'''def employee(name, salary=9000):
    print(name, salary)

employee("Ben",12000)
employee("Arun")'''

'''def outer_fun(a, b):
    # square = a ** 2

    def calculate(a, b):
        return a + b

    cal = calculate(a, b)
    return cal + 5


result = outer_fun(5, 10)
print(result)'''

'''def addition(num):
    if num:
        return num + addition(num - 1)
    else:
        return 0


add = addition(10)
print(add)'''

'''def emp_name(name, age, likes):
    print(f"i like {likes[0]},and {likes[1]}")
    print(name, age)


emp_name("arun", 24, ["Music", "Dancing"])'''

'''def addThree(num1, num2, num3):
    return num1 + num2 + num3


add = addThree(1, 2, 3)
print(add)'''

'''def addAll(**kwargs):
    result = 0
    for x in kwargs:
        result = result + kwargs[x]
    print(result)


addAll(key1=1, key2=2, key3=3)'''


'''def addAll(*args):
    result = 0
    for i in args:
        result += i
    print(result)


addAll(1, 2, 3, 4, 5)'''


numbers = (10, 20, 30, 40, 50)
numbers = numbers[-3:-2]
numbers = numbers[-1]
print(numbers)
