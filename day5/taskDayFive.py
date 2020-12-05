file = open("data.txt", "r")
passports = file.read().split('\n')

# First Task of Day 5
allSeatIds = []
for passport in passports:
    seatRowUpper = 127
    seatRowLower = 0
    seatColumnUpper = 7
    seatColumnLower = 0
    for char in passport:
        if char == 'F':
            seatRowUpper = seatRowLower + int((seatRowUpper - seatRowLower) / 2)
        if char == 'B':
            seatRowLower = seatRowUpper - int((seatRowUpper - seatRowLower) / 2)
        if char == 'L':
            seatColumnUpper = seatColumnLower + int((seatColumnUpper - seatColumnLower) / 2)
        if char == 'R':
            seatColumnLower = seatColumnUpper - int((seatColumnUpper - seatColumnLower) / 2)

    if passport[9] == 'R':
        seatColumnLower = seatColumnUpper
    if passport[6] == 'B':
        seatRowLower = seatRowUpper
    allSeatIds.append((seatRowLower * 8) + seatColumnLower)
print(max(allSeatIds))

# Second Task of Day 5
allSeatIds = []
for passport in passports:
    seatRowUpper = 127
    seatRowLower = 0
    seatColumnUpper = 7
    seatColumnLower = 0
    for char in passport:
        if char == 'F':
            seatRowUpper = seatRowLower + int((seatRowUpper - seatRowLower) / 2)
        if char == 'B':
            seatRowLower = seatRowUpper - int((seatRowUpper - seatRowLower) / 2)
        if char == 'L':
            seatColumnUpper = seatColumnLower + int((seatColumnUpper - seatColumnLower) / 2)
        if char == 'R':
            seatColumnLower = seatColumnUpper - int((seatColumnUpper - seatColumnLower) / 2)

    if passport[9] == 'R':
        seatColumnLower = seatColumnUpper
    if passport[6] == 'B':
        seatRowLower = seatRowUpper
    allSeatIds.append((seatRowLower * 8) + seatColumnLower)
print(sorted(set(range(min(allSeatIds), max(allSeatIds))).difference(allSeatIds)))
