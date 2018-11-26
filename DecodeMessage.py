def Decode(base, message):
    return ChangeToAsciiChar(base, GetListBaseValues(base, GetASCII(list(message))))

def GetASCII(message):
    decimals = []
    for i in range(0, len(message)):
        decimals.insert(i, ord(message[i]))
    return decimals

def GetListBaseValues(base, decimalCharacters):
    baseValues = []
    for asciiValue in decimalCharacters:
        newValue = ""
        bits = str(GetNewBaseValue(asciiValue, base, 7,[]))
        print(bits)
        for bit in bits:
            newValue += bit
        newValue = int(newValue)
        baseValues.append(newValue)
    return baseValues

def GetNewBaseValue(asciiVal,base,counter,bits):
    if counter < 0:
        return bits
    else:
        quotient = asciiVal // base**counter
        remainder = asciiVal % base**counter
        bits.insert(len(bits),str(quotient))
        GetNewBaseValue(remainder,base,counter - 1,bits)

def ChangeToAsciiChar(base, baseValues):
    characters = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","+","/"]
    allNewChar = []
    for value in baseValues:
        newChar = []
        for num in value:
            newChar.append(characters[characters.index(num)])
        allNewChar.append(newChar)
    return allNewChar