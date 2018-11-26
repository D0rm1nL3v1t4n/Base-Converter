def Decode(base, message):
    message = list(message)
    decimalCharacters = GetASCII(message)
    newBaseCharacters = GetNewBaseCharacters(base, decimalCharacters)

def GetASCII(message):
    decimals = []
    for i in range(0, len(message)):
        decimals.insert(i, ord(message[i]))
    return decimals

def GetNewBaseCharacters(base, decimalCharacters):
    return ChangeToAsciiChar(base, GetListBaseValues(base, decimalCharacters))


def GetListBaseValues(base, decimalCharacters):
    baseValues = []
    for asciiValue in decimalCharacters:
        newValue = ""
        for bit in GetNewBaseValue(asciiValue, base, 1, []):
            newValue += bit
        newValue = int(newValue)
        baseValues.append(newValue)
    return baseValues  

def GetNewBaseValue(asciiVal,base,counter,bits):
    remainder = asciiVal % base^counter
    if (asciiVal >= base^counter):
        bits[counter-1] = remainder
        GetNewBaseValue(asciiVal,base,counter + 1,bits)
    else:
        return bits

def ChangeToAsciiChar(baseValues):
    charValList = []
    for element in charValList:
        if (charValList[i][0] == baseValues)