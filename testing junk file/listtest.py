import random

randomList = []
removeList = []
for i in range(0,20):
    n = random.randint(1,15)
    randomList.append(n)
    print(n, end="\n")

removeList = set(randomList)

print("The size is: ", len(removeList), end="\n")
for i in range(len(removeList)):
    print(randomList[i], end="\n")

