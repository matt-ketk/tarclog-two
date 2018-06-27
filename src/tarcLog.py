import os
import pickle

from config import Config
from flight import Flight
from datasheet import DataSheet

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
                hasQuitDataInput = False
                dataSheet = DataSheet()
                date = dataSheet.date().strftime(Config._DATE_FORMAT_FILE)
                saveName = Config._SAVES_DIR + "save_" + date + ".pkl"

                while not hasQuitDataInput:
                    dataSheet.add(Flight())
                    editFlight(dataSheet, saveName, dataSheet.size() - 1, False)
                    # DRY this later...
                    hasChosen = False
                    while not hasChosen:
                        userInput = input(
                            "Do you want to add another flight? (yes, y/no, n): "
                        ).lower();
                        hasChosen = True
                        if userInput == "yes" or userInput == "y":
                            print("Adding Flight No. "
                            + str(dataSheet.size() + 1));
                        elif userInput == "no" or userInput == "n":
                            print("Returning to menu...\n")
                            hasQuitDataInput = True
                        else:
                            hasChosen = False
                if dataSheet.size() < 1:
                    try:
                        os.remove(saveName)
                    except OSError:
                        print("Did not find file. Exiting...")
            elif num == 1:
                pass
            elif num == 2:
                pass
            elif num == 3:
                pass
            elif num == 4:
                pass
            elif num == 5:
                # DRY this later...
                hasChosen = False
                while not hasChosen:
                    userInput = input(
                        "Are you sure you want to exit? (yes, y/no, n): "
                    ).lower();
                    hasChosen = True
                    if userInput == "yes" or userInput == "y":
                        hasQuit = True
                        print("Exiting...")
                    elif userInput == "no" or userInput == "n":
                        print("Returning to menu...\n")
                    else:
                        hasChosen = False
            else:
                print(Config.Config._ERROR_0)
        else:
            print(Config.Config._ERROR_0)


def intCheck(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def floatCheck(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

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

def editFlight(sheet, saveName, flightNum, showField):
    hasSaved = False
    isDone = False
    phase = 0
    flight = sheet.get(flightNum)
    fieldSequence = []
    fieldSequence += Config._WEATHER
    fieldSequence += Config._SPECIFICATIONS
    fieldSequence += Config._MASS_COMPONENTS
    fieldSequence += Config._RESULTS + Config._OBSERVATIONS
    """
    groupingSequence = {
        0 : "Weather",
        len(Config._SPECIFICATIONS) - 1 : "Specifications",
        len(Config._MASS_COMPONENTS) - 1 : "Mass Components",
        len(Config._RESULTS) - 1 : "Results",
        len(Config._OBSERVATIONS) - 1 : "Observations"
    }
    """
    while phase in range(0, len(fieldSequence)):
        field = fieldSequence[phase]

        if phase in range(0, len(fieldSequence) - len(Config._OBSERVATIONS)):
            userInput = input(field
            + Config._DATASHEET_FORMAT[field] + ": ");

            if evalInput(userInput) == 0:
                if evalKeyword(userInput) == 0:
                    if phase < len(fieldSequence):
                        phase += 1
                    else:
                        print(Config._ERROR_1)
                elif evalKeyword(userInput) == 1: 
                    if phase > 0:
                        phase -= 1
                    else:
                        print(Config._ERROR_1)
                elif evalKeyword(userInput) == 2:
                    hasSaved = True
                    with open(saveName, 'wb') as save:
                        pickle.dump(sheet, save)
                elif evalKeyword(userInput) == 3:
                    phase = -1
                elif evalKeyword(userInput) == 4:
                    ind = "\t"
                    print("\nKeywords:")
                    print(ind + "/pass, /p:\tSkips the current field to the next one.")
                    print(ind + "/back, /b:\tGoes back to the previous field.")
                    print(ind + "/save, /s:\tSaves the flight onto the data sheet.")
                    print(ind + "/finish, /f:\tSkips the whole flight input and asks to save or not.")
                    print(ind + "/help, /h:\tBrings up this dialog.")
            elif isinstance(flight.get(field), int) or isinstance(flight.get(field), float):
                if evalInput(userInput) == 1 or evalInput(userInput) == 2:
                    flight.set(field, float(userInput))
                    phase += 1
                else:
                    print(Config._ERROR_0)
            elif isinstance(flight.get(field), str):
                if evalInput(userInput) == 3:
                    flight.set(field, userInput)
                    phase += 1
                else:
                    print(Config._ERROR_0)
            elif isinstance(flight.get(field), list):
                isValid = True
                values = userInput.split(" ")

                for index in range(0, len(values)):
                    if values[index].strip() == "":
                        values.remove(index)

                for v in values:
                    if not floatCheck(v):
                        isValid = False

                if isValid:
                    checkedValues = []
                    for v in values:
                        checkedValues.append(float(v))
                    flight.set(field, checkedValues)
                    phase += 1
                else:
                    print(Config._ERROR_0)
        else:
            isDone = False
            print(field + Config._DATASHEET_FORMAT[field] + ":")
            print("NOTE: enter /view, /v to view past comments; enter /del "
            + "<index> or /d <index> to remove a comment; enter /end, "
            + "/e to stop adding messages");
            while not isDone:
                userInput = input()
                if evalInput(userInput) == 0:
                    if evalKeyword(userInput) == 0:
                        if phase < len(fieldSequence):
                            isDone = True
                            phase += 1
                        else:
                            print(Config._ERROR_1)
                    elif evalKeyword(userInput) == 1:
                        if phase > 0:
                            isDone = True
                            phase -= 1
                        else:
                            print(Config._ERROR_1)
                    elif evalKeyword(userInput) == 2:
                        hasSaved = True
                        with open(saveName, 'wb') as save:
                            pickle.dump(sheet, save)
                    elif evalKeyword(userInput) == 3:
                        isDone = True
                        phase = -1
                    elif evalKeyword(userInput) == 4:
                        ind = "\t"
                        print("\nKeywords:")
                        print(ind + "/pass, /p:\tSkips the current field to the next one.")
                        print(ind + "/back, /b:\tGoes back to the previous field.")
                        print(ind + "/save, /s:\tSaves the flight onto the data sheet.")
                        print(ind + "/finish, /f:\tSkips the whole flight input and asks to save or not.")
                        print(ind + "/help, /h:\tBrings up this dialog.")
                elif userInput.lower() == "/view" or userInput.lower() == "/v":
                    for index in range(0, flight.observationSize(field)):
                        print(index + ": " + field.getObservation(index))
                elif "/del" in userInput or "/d" in userInput:
                    split = userInput.split(" ")

                    for index in range(0, len(split)):
                        if split[index].strip() == "":
                            split.remove(index)
                    if len(split) > 1:
                        if intCheck(split[1]):
                            flight.removeObservation(field, int(split[1]))
                        else:
                            print(Config._ERROR_0)
                    else:
                        print(Config._ERROR_0)
                elif userInput.lower() == "/end" or userInput.lower() == "/e":
                    isDone = True
                    phase += 1
                else:
                    flight.addObservation(field, userInput)
    isDone = False
    while not isDone:
        userInput = input("Do you want to save (yes, y/no, n): ")
        userInput = userInput.lower()
        if userInput == "yes" or userInput == "y":
            isDone = True
            with open(saveName, 'wb') as save:
                pickle.dump(sheet, save)
        elif userInput == "no" or userInput == "n":
            isDone = True
            if not hasSaved:
                sheet.remove(flightNum)
        print("Exiting...\n")

main()
