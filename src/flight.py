from config import Config

class Flight:
    __flightData = {}

    def __init__(self):
        self.__flightData = {
            "Temperature" : 0.0,
            "Wind Speed" : 0.0,
            "Humidity" : 0.0,
            "Payload Name" : "",
            "Booster Name" : "",
            "Motor Name" : "",
            "Parachute Name" : "",
            "Motor Delay" : 0.0,
            "Payload" : 0.0,
            "Booster" : 0.0,
            "Eggs" : [],
            "Parachute" : 0.0,
            "Nomex" : 0.0,
            "Insulation" : 0.0,
            "Ballast" : 0.0,
            "Casing" : 0.0,
            "Motor" : 0.0,
            "Time" : 0.0,
            "Altitude" : 0.0,
            "Modifications" : [],
            "Damages" : [],
            "Characteristics" : [],
            "Considerations" : []
        }

    # for "Eggs" field, input the list directly
    def set(self, field, value):
        if field in self.__flightData and not (field in Config._OBSERVATIONS):
            if type(self.__flightData[field]) is type(value):
                self.__flightData[field] = value
            else:
                raise ValueError(Config._EXCEPTION_1)
        else:
            raise ValueError(Config._EXCEPTION_0)

    # for "Eggs" field, returns the list directly
    def get(self, field):
        if field in self.__flightData and not (field in Config._OBSERVATIONS):
            return self.__flightData[field]
        else:
            raise ValueError(Config._EXCEPTION_0)

    def score(self):
        score = 0.0
        time = self.__flightData["Time"]
        altitude = self.__flightData["Altitude"]
        if time < Config._MIN_TIME:
            score += 4 * (Config._MIN_TIME - time)
        elif time > Config._MAX_TIME:
            score += 4 * (time - Config._MAX_TIME)
        return (score + abs(altitude - Config._ALTITUDE))

    def totalMass(self):
        total = 0.0
        for mass in Config._MASS_COMPONENTS:
            if mass == "Eggs":
                for eggMass in self.__flightData[mass]:
                    total += eggMass
            else:
                total += self.__flightData[mass]

        return total

    def addObservation(self, field, message):
        if field in Config._OBSERVATIONS:
            if type(message) is types.StringTypes:
                self.__flightData[field].append(message)
            else:
                raise ValueError(Config._EXCEPTION_1)
        else:
            raise ValueError(Config._EXCEPTION_0)

    def removeObservation(self, field, i):
        if field in Config._OBSERVATIONS:
            if i in range(0, len(self.__flightData[field])):
                return self.__flightData[field].pop(i)
            else:
                raise IndexError(Config._EXCEPTION_2)
        else:
            raise ValueError(Config._EXCEPTION_0)

    def getObservation(self, field, i):
        if field in Config._OBSERVATIONS:
            if i in range(0, len(self.__flightData[field])):
                return self.__flightData[field][i]
            else:
                raise IndexError(Config._EXCEPTION_2)
        else:
            raise ValueError(Config._EXCEPTION_0)

    def observationSize(self, field):
        if field in Config._OBSERVATIONS:
            return len(self.__flightData[field])
        else:
            raise ValueError(Config._EXCEPTION_0)

    def isComplete(self):
        for i in Config._WEATHER:
            if self.__flightData[i] <= 0.0:
                 return False
        for i in Config._SPECIFICATIONS:
            if self.flightData[i].strip() == "":
                return False
        for i in Config._MASS_COMPONENTS:
            if i == "Eggs":
                if len(self.__flightData[i]) < 1:
                    return False
                else:
                    for j in self.__flightData[i]:
                        if j <= 0.0:
                            return False
            elif self.flightData[i] <= 0.0:
                return False
        for i in Config._RESULTS:
            if self.__flightData[i] <= 0.0:
                return False
        for i in Config._OBSERVATIONS:
            if len(self.__flightData[i]) < 1:
                return False
        return True
