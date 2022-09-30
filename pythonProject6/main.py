"""with open("user_input.txt", "a") as file:
    user_input = input("please give some text to store: ")
    while user_input != "stop":
        file.write(user_input + "\n")
        user_input = input("Please give some text to store: ")
    file.seek(0)
    print("file name: " + file.name)
    print(file.read())"""

'''x = [1, 2, 3]
y = ["arun","sama"]
x.append(y)
print(x)'''

'''myLIst = [2, 4, 5, 6, 1]
i = 0
for i in myLIst:
    print("Level Started")
    for y in range(i):
        print(f"star {y} collected")
    print("level completed")'''

'''num = int(input("Enter the number: "))
for i in range(1, num + 1):
    row = ""
    for y in range(i):
        row += str(i)
    print(row)'''

with open("user_input.txt", "w") as file:
    num = (input("Enter the number: "))
    while num != 'Stop':
        file.write(num + "\n")
        num = input("Enter the number: ")
    file.seek(0)
    print(file.read())
