#!/usr/local/bin/python3

import sys

def isLeapYear(myYear):
    if ( myYear % 4 ) == 0:
        if ( myYear % 100 ) != 0:
            return "true"
    else:
        return "false"



if len(sys.argv) < 2:
    print("Please provide a year as an argument")
else:
    value = int(sys.argv[1])

    if (isinstance(value,(int)) == True):
        print(isLeapYear(value))
    else:
        print ("Please provide an interger value")
