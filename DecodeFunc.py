def Decode(base, message):
    return ConcatenateMessage(GetDecimalValues(GetListMessage(message), base))

def GetListMessage(message):
    listMessage = message.split(" ")
    #listMessage.pop()
    return listMessage

def GetDecimalValues(message, base):
    asciiCharList = []
    for character in message:
        listChar = list(reversed(character))
        asciiCharacters = []
        for character in listChar:
            asciiCharacters.append(ChangeToAscii(character))
        decimalValue = ChangeToDecimal(asciiCharacters, base, GetIterationCount(base) , 0)
        asciiCharList.append(chr(decimalValue))
    return asciiCharList

def ChangeToDecimal(listChar, base, counter, value):
    if counter < 0:
        return value
    else:
        value += int(listChar[counter]) * (base**counter)
        return ChangeToDecimal(listChar, base, counter - 1, value)

def ChangeToAscii(character):
    characterValues = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","+","/"]
    return characterValues.index(character)

def GetIterationCount(base):
    if (base == 2):
        return 6
    elif (base == 3):
        return 4
    elif (base < 6):
        return 3
    elif (base < 12):
        return 2
    else:
        return 1

def ConcatenateMessage(returnVal):
    newMessage = ""
    for character in returnVal:
        newMessage += character
    return newMessage