import os

WEATHER = "WEATHER"


def setenv(key, value):
    with open(os.path.join(os.path.dirname(__file__), ".env"), "a+") as f:
        f.write(f"{key.upper()}={value}")


def getenv(key):
    with open(os.path.join(os.path.dirname(__file__), ".env"), "r") as f:
        for line in f:
            var = line.split("=")
            if var[0] == key.upper():
                return var[1]
    
    return None