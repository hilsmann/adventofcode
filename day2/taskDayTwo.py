import re

file = open("data.txt", "r")
arrayOfNumbers = file.read().split('\n')

# First Task of Day 2
correctPasswords = 0
for element in arrayOfNumbers:
    arrayOfOneLine = element.split(' ')
    minMax = arrayOfOneLine[0].split('-')
    letter = arrayOfOneLine[1].replace(':', '')
    word = arrayOfOneLine[2]
    letterCount = len(re.findall(r'['+letter+']', word))
    if int(minMax[0]) <= int(letterCount) <= int(minMax[1]):
        correctPasswords += 1

print(correctPasswords)

# Second Task of Day 2
correctPasswordsTwo = 0
for element in arrayOfNumbers:
    arrayOfOneLine = element.split(' ')
    minMax = arrayOfOneLine[0].split('-')
    letter = arrayOfOneLine[1].replace(':', '')
    word = arrayOfOneLine[2]
    if (word[int(minMax[0])-1].__eq__(letter) or word[int(minMax[1])-1].__eq__(letter)) and\
            not(word[int(minMax[0])-1].__eq__(letter) and word[int(minMax[1])-1].__eq__(letter)):
        correctPasswordsTwo += 1

print(correctPasswordsTwo)
