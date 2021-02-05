def collatzFunction(number):
    if number % 2 == 0:
        print("NUmber // 2")
        return number // 2
    else:
        return 3 * number + 1


numberEntered = ""
while not numberEntered:
    try:
        print("Please enter a number:")
        numberEntered = int(input())
    except ValueError:
        print("I said a number, dico!")
while numberEntered != 1:
    numberEntered = collatzFunction(numberEntered)
    print(numberEntered)