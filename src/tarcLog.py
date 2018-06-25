import config
import flight

def main():
    userInput = ""
    hasQuit = False

    while not hasQuit:
        print("Welcome to TARC Log. Start off with these commands:")
        print("\t0: New Data Sheet")
        print("\t1: Edit Data Sheet")
        print("\t2: Print Data Sheet")
        print("\t3: Delete Data Sheet")
        print("\t4: Analyze Data Sheet")
        print("\t5: Exit")

        userInput = input()
        if evalInput(userInput) == 1:
            num = int(userInput)
            if num == 0:
                pass
            elif num == 1:
                pass
            elif num == 2:
                pass
            elif num == 3:
                pass
            elif num == 4:
                pass
            elif num == 5:
                hasChosen = False
                while not hasChosen:
                    userInput = input("Are you sure you want to exit? (yes, y/no, n): ").lower()
                    hasChosen = True
                    if userInput == "yes" or userInput == "y":
                        hasQuit = True
                        print("Exiting...")
                    elif userInput == "no" or userInput == "n":
                        print("Returning to menu...\n")
                    else:
                        hasChosen = False
            else:
                print(Config._ERROR_0)
        else:
            print(Config._ERROR_0)


def intCheck(s):
    try:
        int(s)
    except ValueError:
        return False
    return True

def floatCheck(s):
    try:
        float(s)
    except ValueError:
        return False
    return True

def evalKeyword(s):
    result = -1
    s = s.lower()
    if s == "/pass" or s == "/p":
        result = 0
    elif s == "/back" or s == "/b":
        result = 1
    elif s == "/save" or s == "/s":
        result = 2
    elif s == "/finish" or s == "/f":
        result = 3
    elif s == "/help" or s == "/h":
        result = 4
    return result

def evalInput(s):
    result = -1
    if evalKeyword(s) != -1:
        result = 0
    elif intCheck(s):
        result = 1
    elif floatCheck(s):
        result = 2
    else:
        result = 3
    return result

def editFlight(sheet, fileName, flightNum):
    pass

main()
