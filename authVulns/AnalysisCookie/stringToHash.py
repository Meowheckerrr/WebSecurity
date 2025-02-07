import hashlib
import base64

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
                list.append(line.rstrip()) # Remove "/n"    

            #print("List:", list)
            wordlist.close()
        
        return list
    except FileNotFoundError:
        print("File not found:", filePath)
    except Exception as e:
        print("Error", e)

def readWordlistToHashList(wordlist):
    hashList = []

    for string in wordlist:
        hashString = hashlib.md5(string.encode()).hexdigest()    # md5 input must be Binary String(b"string" - 0~255)
        hashList.append(hashString)
    print(hashList)
    return hashList

def writeHashListToFile(hashList,hashFilePath):

    with open(hashFilePath, 'w') as hashFile:
        for hash in hashList:

            hashFile.write(hash + '\n')
        
        print(hashList)
        hashFile.close()


def addingPrifixBase64Encode(hashList):
    finalPayloadList = []
    for hash in hashList:
        prifixAndPass = 'carlos:'+hash
        Encode = base64.b64encode(prifixAndPass.encode()).decode()
        finalPayloadList.append(Encode) 
    return finalPayloadList

def writeFinalPayloadToFile(finalPayloadList,finalPayloadPath):
    with open(finalPayloadPath, 'w') as hashFile:
        for hash in finalPayloadList:

            hashFile.write(hash + '\n')
        
        hashFile.close()

banner=Banner()

filePath="./wordlist.txt"
hashFilePath="./hashList.txt"
finalPayloadPath ="./finalPayload.txt"
wordlist=readWordlistToList(filePath)
hashList = readWordlistToHashList(wordlist)
writeHashListToFile(hashList,hashFilePath)

finalPayloadList = addingPrifixBase64Encode(hashList)
print(">>>>>>>>>>>",finalPayloadList)
writeFinalPayloadToFile(finalPayloadList,finalPayloadPath)