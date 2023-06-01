# TODO: Imports
import config
import time

# Variables
cameraCentre = config.CAMERA_START_CENTRE_LINE
boostTime = 0
throttleVal = config.NORMAL_THROTTLE

def getLineLocation():
    # TODO
    return (0.0, 0.0)

def getMushroomLocation():
    # TODO
    return (0.0, 0.0)

def mushroomPresent():
    # TODO
    return False

def mushroomOnDifferentLane():
    return abs(config.cameraCentre + config.CENTRE_ERROR - getMushroomLocation()) > 0

def getMushroomDistance():
    # TODO
    return 1

# Return 0 if left lane, 1 if right lane
def getCurrentLane():
    # TODO
    return 0

# @param nextLane: 0 if left lane, 1 if right lane
def switchLanes(nextLane):
    if (nextLane == 0):
        cameraCentre = config.CAMERA_CENTRE_LEFT_LANE
    else:
        cameraCentre = config.CAMERA_CENTRE_RIGHT_LANE
    return

def stayOnLane(boosted):
    throttleVal = config.NORMAL_THROTTLE
    if (boosted):
        throttleVal = throttleVal * config.BOOST_VALUE
    # TODO: Some pyvesc code
    return

while(True):
    if (mushroomPresent):
        if (mushroomOnDifferentLane()):
            switchLanes()

        if (getMushroomDistance() < config.MUSHROOM_BOOST_DISTANCE):
            boostTime = time.time() + config.BOOST_DURATION
            stayOnLane(True)
            continue

    if (time.time() <= boostTime):
        stayOnLane(True)
    else:
        stayOnLane(False)