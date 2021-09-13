import random


def randomNum():
    newList = []
    myList = [19, 16, 26, 33, 11, 22, 37, 3, 7, 17]  # 10 NUMBERS!!!!!!!!
    for i in range(6):
        ranNum = random.choice(myList)
        myList.remove(ranNum)
        newList.append(ranNum)
        newList.sort()
    return newList


def randomList():
    listOfList = []
    for i in range(10):
        oneSet = randomNum()
        if oneSet in listOfList:
            oneSet
        listOfList.append(oneSet)
        listOfList.sort()
    for i in range(len(listOfList)):
        print(listOfList[i])


randomList()
