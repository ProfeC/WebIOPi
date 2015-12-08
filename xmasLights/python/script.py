import webiopi
import datetime

def setup():
        pfd = webiopi.deviceInstance("pfd") # retrieve the device named "pfd" in the configuration


    # retrieve current datetime
    now = datetime.datetime.now()

def loop():

