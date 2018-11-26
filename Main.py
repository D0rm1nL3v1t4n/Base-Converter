from DecodeMessage import Decode
from EncodeMessage import Encode

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
    operations = [["A","Decode"],["B","Encode"]]
    for i in operations:
        print(i[0] + ": " + i[1])
    return operations

def GetMessage():
    message = input(">>> Enter message: ")
    return message

def CallOperation(base, operation, message):
    if operation == "A":
        Decode(base, message)
    elif operation == "B":
        Encode(base, message)

def Main():
    CallOperation(GetBase(), GetOperation(), GetMessage())
        

def RunTest():
    CallOperation(2, "A", "Nimrod")


def DoListStuff():
    arrayOne = ("1","2","3","4","5","6")
    print(arrayOne)
    for integer in arrayOne:
        print(str(integer))

#Main()
#DoListStuff()
RunTest()