import datetime
from config import Config
from flight import Flight

class DataSheet:
    __flights = []
    __dateCreated = datetime.datetime.now()

    def __init__(self):
        self.__flights = []
        self.__dateCreated = datetime.datetime.now()

    def size(self):
        return len(self.__flights)

    def add(self, f):
        if isinstance(f, Flight):
            self.__flights.append(f)

    def remove(self, i):
        if i in range(0, len(self.__flights)):
            self.__flights.remove(i)
        else:
            raise IndexError(Config._EXCEPTION_0)

    def get(self, i):
        if i in range(0, len(self.__flights)):
            return self.__flights[i]
        else:
            raise IndexError(Config._EXCEPTION_0)

    def tab(self, field):
        length = len(field + Config._DATASHEET_FORMAT[field]) + 1
        tabs = ""
        for i in range(0, 20 - length, 4):
            tabs += "\t"
        return tabs

    def printSheet(self, fileName):
        with open(fileName, 'w') as sheet:
            sheet.write("Date:\t" + self.__dateCreated.strftime("%m/%d/%y")
            + "\n\n");

            for i in range(0, len(self.__flights)):
                flight = self.__flights[i]

                sheet.write("Flight No.\t" + str(i + 1) + "\n")

                sheet.write(Config._IND_0 + "Weather:\n")
                for field in Config._WEATHER:
                    sheet.write(Config._IND_1 + field
                    + Config._DATASHEET_FORMAT[field] + ":"
                    + self.tab(field) + "%.1f" % flight.get(field) + "\n");

                sheet.write(Config._IND_0 + "Specifications:\n")
                for field in Config._SPECIFICATIONS:
                    if field == "Motor Delay":
                        sheet.write(Config._IND_1 + field
                        + Config._DATASHEET_FORMAT[field] + ":"
                        + self.tab(field) + "%d" % flight.get(field) + "\n");
                    else:
                        sheet.write(Config._IND_1 + field
                        + Config._DATASHEET_FORMAT[field] + ":"
                        + self.tab(field) + flight.get(field) + "\n");

                sheet.write(Config._IND_0 + "Mass Components:\n")
                for field in Config._MASS_COMPONENTS:
                    if field == "Eggs":
                        sheet.write(Config._IND_1 + field
                        + Config._DATASHEET_FORMAT[field] + ":"
                        + self.tab(field));
                        for egg in flight.get(field):
                            sheet.write("%.1f" % egg + " ")
                        sheet.write("\n")
                    else:
                        sheet.write(Config._IND_1 + field
                        + Config._DATASHEET_FORMAT[field] + ":"
                        + self.tab(field) + "%.1f" % flight.get(field) + "\n");
                sheet.write(Config._IND_1 + "Total (g):\t\t\t"
                + str(flight.totalMass()) + "\n");

                sheet.write(Config._IND_0 + "Flight Results:\n")
                for field in Config._RESULTS:
                    if field == "Altitude":
                        sheet.write(Config._IND_1 + field
                        + Config._DATASHEET_FORMAT[field]
                        + ":\t\t%d" % flight.get(field) + "\n");
                    else:
                        sheet.write(Config._IND_1 + field
                        + Config._DATASHEET_FORMAT[field]
                        + ":\t\t\t%.2f" % flight.get(field) + "\n");
                sheet.write(Config._IND_1 + "Flight Score:\t\t"
                + str(flight.score()) + "\n");

                sheet.write(Config._IND_0 + "Observations:\n")
                for field in Config._OBSERVATIONS:
                    sheet.write(Config._IND_1 + field + ":\n")
                    for j in range(0, flight.observationSize(field)):
                        sheet.write(Config._IND_1 + "-\t"
                        + flight.getObservation(field, j) + "\n");
                sheet.write("\n")

"""
testsheet = DataSheet()
testsheet.add(Flight())
testsheet.printSheet("test.txt")
"""
