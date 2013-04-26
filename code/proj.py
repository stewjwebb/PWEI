#this is the start point.
#first thing will be something to generate default directory structure.

import argparse

def createNewDirStruc():
    print "CreateNewDirStruc"
    return

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='command and params')
    #parser.add_argument('integers', metavar='N', type=int, nargs='+',help='an integer')
    parser.add_argument('-c', type=str, help='command')
    args = parser.parse_args()
    
    if args.c == 'new':
        print "new detected"
        print args.c
        createNewDirStruc()
    else:
        print args.c

