"""myList = ["Apple","kiwi","Mango","Melon","Cherry"]
myList.insert(2,"Orange")
print(myList)
print(myList[2])
dictionary = {"A":"Apple","A":"Ant"}
dictionary1 = {"A":"Apple","B":"Ball","C":"Cat"}
x = dictionary1.get("B")
print(x)
print(dictionary.get("A"))
tuple = (1,2,3,4,5)
x=5
y=2
x,y = y,x
print(x)
print(y)"""
'''for i in "1000":
    print(i)
def test(a,b=5,c=10):
    print(a)
    print(b)
    print(c)

test()
test(1)
test(1,2)
test(1,2,3)'''
'''l1 = [1,2,3]
l2 = [3,4,5]
#l1.extend(l2)
print(l1)'''

'''def myList(**a):
    print("Hello ", a)


myList(a=1,b= 2,c= 3)  # Hello (1,2,3)
myList(a=12)  # Hello 12
myList()  # Error'''

'''def add(a, b):
    c = a + b
    print(c)


add(2, 3)


def sub(c, d):
    print(c + d)


sub(3, 5)


def mul(e, f):
    return e + f


print(mul(5, 6))'''

'''def bill_amount_after_discount(bill_amount, discount_percentage):
    discount_amount = bill_amount * (discount_percentage / 100)
    final_bill_amount = bill_amount - discount_amount

    return discount_amount


print(bill_amount_after_discount(int(input("Enter the number :")),int(input("Enter the discount :"))))'''

# Calculator

'''def add(first_number, second_number):
    return first_number + second_number


def sub(first_number, second_number):
    return first_number - second_number


def mul(first_number, second_number):
    return first_number * second_number


def div(first_number, second_number):
    return first_number / second_number


def modulus(first_number, second_number):
    return first_number % second_number


def invalid():
    return "Invalid Operator"


def calculate(first_number, operator, second_number):
    if operator == "+":
        result = add(first_number, second_number)
    elif operator == "-":
        result = sub(first_number, second_number)
    elif operator == "*":
        result = mul(first_number, second_number)
    elif operator == "/":
        result = div(first_number, second_number)
    elif operator == "%":
        result = modulus(first_number, second_number)
    else:
        result = "Invalid operator"

    print(result)


print(calculate(first_number=int(input("Number1: ")), operator=input("operator: "), second_number=int(input("Number2: "))))'''

'''def welcome_message(customer_name):
    print("hi", customer_name)
    print("Welcome to the hotel")
    print("We are offering good food")


def thank_you_message(title, customer_name):
    print("Please visit again")
    return "Thank you for choosing us " + title + customer_name


welcome_message("Arun Sama")
welcome_message("Sam")
print(thank_you_message("Mr. ", "Arun Sama"))'''

x = 5
y = 7
# print(x,y)
if x == y:
    print("Hello World")

else:
    print("It is wrong")


