file = open("data.txt", "r")
forest = file.read().split('\n')


def checkIfThereIsATree(indexOfLine, element, treeCount):
    if element[indexOfLine] == '#':
        treeCount += 1
    return treeCount

# First Task of Day 3
trees = 0
index = 0
for element in forest:
    # Check For Trees
    trees = checkIfThereIsATree(index, element, trees)
    index = (index + 3) % len(element)

print(trees)

# Second Task of Day 3
trees1 = 0
trees2 = 0
trees3 = 0
trees4 = 0
trees5 = 0
index1 = 0
index2 = 0
index3 = 0
index4 = 0
index5 = 0
for i, element in enumerate(forest):

    # Check For Trees
    trees1 = checkIfThereIsATree(index1, element, trees1)
    trees2 = checkIfThereIsATree(index2, element, trees2)
    trees3 = checkIfThereIsATree(index3, element, trees3)
    trees4 = checkIfThereIsATree(index4, element, trees4)

    # Check for Index Out Of Range
    index1 = (index1 + 1) % len(element)
    index2 = (index2 + 3) % len(element)
    index3 = (index3 + 5) % len(element)
    index4 = (index4 + 7) % len(element)
    if not i % 2:
        # Check For Trees
        trees5 = checkIfThereIsATree(index5, element, trees5)

        # Check for Index Out Of Range
        index5 = (index5 + 1) % len(element)

print(trees1 * trees2 * trees3 * trees4 * trees5)
