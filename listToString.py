def listToString(listToChange):
    """
    Takes a list of strings, returns a comma-separated string
    :param listToChange: the list to stringify
    :return: returns a string
    """
    if len(listToChange) == 0:
        return ""
    elif len(listToChange) == 1:
        return listToChange[0]
    else:
        stringedList = ""
        for i in range(len(listToChange)):
            if i == len(listToChange) - 1:
                stringedList += " and "
                stringedList += listToChange[-1]
            else:
                stringedList += listToChange[i]
                stringedList += ", "
        return stringedList

test1 = ["a","b","c","d"]
test2 = ["a", "b","c"]
test3 = ["a","b"]
test4 = ["a"]
test5 = []


print(listToString(test1))
print(listToString(test2))
print(listToString(test3))
print(listToString(test4))
print(listToString(test5))
