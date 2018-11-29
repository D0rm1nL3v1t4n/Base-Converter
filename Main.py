from EncodeFunc import Encode
from DecodeFunc import Decode

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
        OutNewBaseMessage(Encode(base, message), base) 
    elif operation == "B":
        OutputDecimalMessage(Decode(base, message))

def OutNewBaseMessage(newMessage, base):
    print("\n\nYour message in base " + str(base) + ":\n" + str(newMessage))

def OutputDecimalMessage(newMessage):
    print("\n\nYour message in base 10:\n" + str(newMessage))

def Main():
    CallOperation(GetBase(), GetOperation(), GetMessage())

def RunTest():
    CallOperation(2, "A", "Nimrod!")
    CallOperation(2, "B", "1001110 1101001 1101101 1110010 1101111 1100100 0100001")

#RunTest()
Main()
