
filePath = "./wordlist.txt"

class Banner:

    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def __init__(self):
        self.meow_banner()

    def meow_banner(self):
        print(self.HEADER + "##################################################")
        print("#                                                #")
        print("#          " + self.GREEN + "MeowHecker is a cat. ^O^" + self.HEADER + "              #")
        print("#                                                #")
        print("##################################################" + self.ENDC)

        print(self.WARNING + "-> Author: Meowhecker\n" + self.ENDC)

def readWordlistToList(filePath):
    
    list = []
    try:
        with open(filePath, "r") as wordlist:

            for line in wordlist:
                line = line.replace("\n", "")
                line = line.replace(" ", "")
                list.append(line) # Remove "/n"    

            #print("List:", list)
            wordlist.close()
        
        return list
    except FileNotFoundError:
        print("File not found:", filePath)
    except Exception as e:
        print("Error", e)


def httpHeaderToDirectory(headerList):
    headerDic = {}
    for header in headerList:
        key,value = header.split(':',1)
        headerDic[key] = value
        print(f"Header: {key}:Header:{value}")
    return headerDic


banner = Banner()
headerList = readWordlistToList(filePath)
headerDic = httpHeaderToDirectory(headerList)
print(headerDic)