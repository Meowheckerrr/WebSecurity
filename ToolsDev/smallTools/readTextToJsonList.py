import json

filePath = "./wordlist.txt"

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

            #print("List:", list)
            wordlist.close()
        
        return list
    except FileNotFoundError:
        print("File not found:", filePath)
    except Exception as e:
        print("Error", e)

def converListToJson(pythonList):

    if pythonList:
        jsonList = json.dumps(pythonList)
        return jsonList
    else:
        print("No python list")
        return None 
    

# Main function

moewBanner()
wordlist = readWordlistToList(filePath)
jsonList = converListToJson(wordlist)
print("JSON list:", jsonList)