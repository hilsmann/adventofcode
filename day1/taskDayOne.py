file = open("data.txt", "r")
arrayOfNumbers = file.read().split('\n')
lastLine = 0
result = 0
for line in arrayOfNumbers:
    for nextLines in arrayOfNumbers:
        for nextLines2 in arrayOfNumbers:
            if line != '\n':
                if int(line) + int(nextLines) + int(nextLines2) == 2020:
                    result = int(line) * int(nextLines) * int(nextLines2)
                    print(line)
                    print(nextLines)
                    print(nextLines2)
                    break

print(result)