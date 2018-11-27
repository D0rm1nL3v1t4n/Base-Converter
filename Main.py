from DecodeFunc import Decode
from EncodeFunc import Encode

def GetBase():
    base = int(input(">>> Base: "))
    return base

def GetOperation():
    operationsList = ListOperations()
    while True:
        operation = input(">>> Select an operation: ")
        for i in operationsList:
            if operation.lower() == i[0].lower():
                return i[0]

def ListOperations():
    operations = [["A","Encode"],["B","Decode"]]
    for i in operations:
        print(i[0] + ": " + i[1])
    return operations

def GetMessage():
    message = input(">>> Enter message: ")
    return message

def CallOperation(base, operation, message):
    if operation == "A":
        return Encode(base, message)
    elif operation == "B":
        return Decode(base, message)

def OutputNewMessage(returnVal, base):
    newMessage = ""
    for characterList in returnVal:
        i = 0
        for character in characterList:
            if (i != 0):
                newMessage += str(character)
            i += 1
        newMessage += " "
    print("\n\nYour message in base " + str(base) + ":\n" + str(newMessage))

def Main():
    base = GetBase()
    OutputNewMessage(CallOperation(base, GetOperation(), GetMessage()), base)

def RunTest():
    OutputNewMessage(CallOperation(16, "A", "Nimrod"), 16)

#RunTest()
Main()