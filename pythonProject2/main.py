"""num = 0
word = "Arun"
while num < len(word):
    if word[num] == "r" or word[num] == "u":
        num += 1
        continue
    print(word[num])
    num += 1"""
# adding sum of numbers
'''myList = (1, 2, 3, 4, 5, 6)
i = 0
add = 0
while i < len(myList):
    add += myList[i]
    i += 1
print(add)'''
# square of numbers
'''num = 1
while num < 5:
    squareNum = num ** 2
    print(num,squareNum)
    num += 1'''
# Multiplication numbers
'''num = int(input())
i = 0
mul = 1
while i <= 10:
    mul = i * num
    print(mul)
    i += 1'''
# sum of even numbers
'''num = int(input())
i = 0
add = 0
while i <= num:
    if i % 2 == 0:
        add += i
    i += 1
print(add)'''
# factorial of numbers
'''num = int(input())
i = 1
mul = 1
while i <= num:
    mul = i * mul
    i += 1
    print(mul)'''
# finding duplicate words in sentence
sentence = "So yes, Kotlin is a great language. It is robust"
words = sentence.split()
count = {}
duplicate_words = {}
for word in words:
    count[word] = count.get(word, 0) + 1
    print(count)
    if count[word] > 1:
        duplicate_words.add(word)
print(duplicate_words)
