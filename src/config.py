class Config:
    # modify them if you know what you're doing
    _DATASHEETS_DIR = "cache/datasheets/"
    _SAVES_DIR = "cache/saves/"
    _DATE_FORMAT = "%m/%d/%y"

    _ERROR_0 = "Incorrect input. Please try again."
    _ERROR_1 = "Incorrect keyword. Please try again."

    _EXCEPTION_0 = "Incorrect field"
    _EXCEPTION_1 = "Incorrect value type"
    _EXCEPTION_2 = "Index out of bounds"

    # field groupings; again modify if you know what you're doing
    _WEATHER = [
        "Temperature",
        "Wind Speed",
        "Humidity"
    ]

    _SPECIFICATIONS = [
        "Payload Name",
        "Booster Name",
        "Motor Name",
        "Parachute Name",
        "Motor Delay"
    ]

    _MASS_COMPONENTS = [
        "Payload",
        "Booster",
        "Eggs",
        "Parachute",
        "Nomex",
        "Insulation",
        "Ballast",
        "Casing",
        "Motor"
    ]

    _RESULTS = [
        "Time",
        "Altitude"
    ]

    _OBSERVATIONS = [
        "Modifications",
        "Damages",
        "Characteristics",
        "Considerations"
    ]

    # datasheet formattings; (as said above)
    _DATASHEET_FORMAT = {
        "Temperature" : " (F)",
        "Wind Speed" : " (MPH)",
        "Humidity" : " (%)",
        "Payload Name" : "",
        "Booster Name" : "",
        "Motor Name" : "",
        "Parachute Name" : "",
        "Motor Delay" : " (s)",
        "Payload" : " (g)",
        "Booster" : " (g)",
        "Eggs" : " (g)",
        "Parachute" : " (g)",
        "Nomex" : " (g)",
        "Insulation" : " (g)",
        "Ballast" : " (g)",
        "Casing" : " (g)",
        "Motor" : " (g)",
        "Time" : " (s)",
        "Altitude" : " (ft)",
        "Modifications" : "",
        "Damages" : "",
        "Characteristics" : "",
        "Considerations" : ""
    }

    _IND_0 = "\t"
    _IND_1 = "\t\t"

    # modify according to tarc season rules
    _MIN_TIME = 43 # seconds
    _MAX_TIME = 46 # seconds
    _ALTITUDE = 856 # feet
