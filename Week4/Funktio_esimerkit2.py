

def displayMenu() -> None:
    print("Menu:")
    print("1 - View balance")
    print("2- Deposit balance")
    print("3- Withdraw money")
    print("0 - Exit")
    return None

def getUserChoice() -> int:
    userInput = input("Enter your choise: ")
    return int(userInput)

def main() -> None:
    print("Welcome to the bank app!")
    choise = -1
    while choise != 0:
        displayMenu()
        choise = getUserChoice()
    return None

main()
