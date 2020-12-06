import collections

file = open("data.txt", "r")
answers = file.read().split('\n\n')

# First Task of Day 6
numberOfAnswersInGroups = 0
for group in answers:
    groupAnswers = set()
    for personInGroup in group.split():
        groupAnswers.update(set(personInGroup))
    numberOfAnswersInGroups += len(groupAnswers)
print(numberOfAnswersInGroups)

# Second Task of Day 6
numberOfAnswersInGroups = 0
for group in answers:
    groupAnswers = list()
    numberOfGroupMembers = 0
    for personInGroup in group.split():
        groupAnswers.extend(list(personInGroup))
        numberOfGroupMembers += 1
    for amountOfOneQuestion in collections.Counter(groupAnswers).most_common():
        if amountOfOneQuestion[1] == numberOfGroupMembers:
            numberOfAnswersInGroups += 1
        else:
            break
print(numberOfAnswersInGroups)
