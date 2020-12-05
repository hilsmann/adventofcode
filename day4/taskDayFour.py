import re

file = open("data.txt", "r")
passports = file.read().split('\n\n')


def validatePassports(listOfregexes):
    validPassorts = 0
    for element in passports:
        passport = element.split()
        if len(passport) >= 7:
            joinpass = ''.join(passport)
            count = 0
            for regex in listOfregexes:
                if re.search(regex, joinpass):
                    count += 1
            if count >= 7:
                validPassorts += 1
    return validPassorts

# First Task of Day 4
regexes = [
    '.*byr',
    '.*iyr',
    '.*eyr',
    '.*hgt',
    '.*hcl',
    '.*ecl',
    '.*pid'
]

print(validatePassports(regexes))

# Second Task of Day 4
regexes = [
    '.*byr:[1][9][2-9][0-9]|.*byr:[2][0][0][0-2]',
    '.*iyr:[2][0][1][0-9]|.*iyr:[2][0][2][0]',
    '.*eyr:[2][0][2][0-9]|.*eyr:[2][0][3][0]',
    '.*hgt:[1][5-8][0-9]cm|.*hgt:[1][9][0-3]cm|.*hgt:[5][9]in|.*hgt:[6][0-9]in|.*hgt:[7][0-6]in',
    '.*hcl:#[0-9a-f]{6}|.*hcl:#[0-9a-f]{6}$',
    '.*ecl:amb|.*ecl:blu|.*ecl:brn|.*ecl:gry|.*ecl:grn|.*ecl:hzl|.*ecl:oth',
    '.*pid:[0-9]{9}[a-zA-Z]|.*pid:[0-9]{9}$'
]

print(validatePassports(regexes))
