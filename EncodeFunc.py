def Encode(base, message):
    return GetListBaseValues(base, GetASCII(list(message)))

def GetASCII(message):
    decimals = []
    for i in range(0, len(message)):
        decimals.insert(i, ord(message[i]))
    return decimals

def GetListBaseValues(base, decimalCharacters):
    baseValues = []
    for asciiValue in decimalCharacters:
        newValue = ""
        for bit in (GetNewBaseValue(asciiValue, base, GetIterationCount(base),[])):
            newValue += ChangeToAsciiCharVal(base, bit)
        baseValues.append(newValue)
    return baseValues

def GetNewBaseValue(asciiVal,base,counter,bits):
    if counter < 0:
        return bits
    else:
        quotient = asciiVal // base**counter
        remainder = asciiVal % base**counter
        bits.insert(len(bits),str(quotient))
        return GetNewBaseValue(remainder,base,counter - 1,bits)

def ChangeToAsciiCharVal(base, num):
    characters = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","+","/"]
    return characters[int(num)]

def GetIterationCount(base):
    if (base == 2):
        return 7
    elif (base == 3):
        return 5
    elif (base < 6):
        return 4
    elif (base < 12):
        return 3
    else:
        return 2