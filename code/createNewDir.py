
import argparse
import os

def createNewDir(path):
    print "createNewDir"
    if(not os.path.exists(path)):
        print "Dir " + path + " created!\n"
        os.makedirs(path)
    else:
        print "Dir " + path + " already exists!\n"
    return


if __name__ == '__main__':
    createNewDir("spaceShip")

