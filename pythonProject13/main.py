"""import threading
import time

exitFlag = 0


class MyThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadId = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        print_time(self.name, 5, self.counter)
        print("Exiting " + self.name)


def print_time(threadName, counter, delay):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)

thread1.start()
thread2.start()

print("Exit Main Thread")"""


# Parent class : User
# child class :Bank
# store details about the bank
# Allow for withdraw and view balance

# Parent class
class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal details")
        print("")
        print("Name ", self.name)
        print("Age ", self.age)
        print("Gender ", self.gender)


# Child class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.amount = None
        self.balance = 0

    def deposit(self):
        self.amount = int(input("Enter the amount to deposit: "))
        self.balance = self.amount + self.balance
        print("Account Balance is updated ", self.balance)

    def withdraw(self):
        self.amount = int(input("Enter the Amount to withdraw: "))
        if self.amount > self.balance:
            print("Enter the Valid amount")
        else:
            self.balance = self.balance - self.amount
            print("Account balance is updated ", self.balance)


print("Insert user Card ")

login_attempts = 0
correct_pin = 1234
while login_attempts <= 3:
    pin = int(input("Please enter a pin: "))
    login_attempts += 1
    if pin == correct_pin:
        print("Login Successful")
        break
    else:
        print("Wrong pin try again later")

Arun = Bank("Sama", 20, "M")
while True:
    if login_attempts > 3:
        print("Your Account is Blocked")
        break
    else:
        print("\n1. Deposit \n2. Withdraw")
        user_Choice = int(input("Please choose the options for Deposit or Withdraw "))
        while user_Choice > 2 or user_Choice < 1:
            user_Choice = int(input("Enter the valid input : "))

        Arun.show_details()

        if user_Choice == 1:
            Arun.deposit()

        elif user_Choice == 2:
            Arun.withdraw()

        print("Continue to the transaction? (Y/N)")
        ans = input()

        if ans == "N" or ans == "n":
            break

print("Thank you for choosing Arun Bank")
