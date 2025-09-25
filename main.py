from specs import *
import errorCorrection as ec
from lib import *

message = "Hello World"
messageLength = len(message)
messageType = "alphanumeric"

errorCorrectionLevel = "Q"

currentBits = 0

for versionIdx in versions:
    if versions[versionIdx][errorCorrectionLevel][messageType] >= messageLength:
        selectedVersion = versionIdx
        totalVersionCodewordBits = getTotalDataCodewordBits(ec.errorCorrections, selectedVersion, errorCorrectionLevel)
        break

messageSpecs = {
    "messageLength": messageLength,
    "messageType": messageType, 
    "selectedVersion": selectedVersion, 
    "errorCorrectionLevel": errorCorrectionLevel
}

binSelectedMode = [modes[messageType]]
currentBits += len(binSelectedMode[0]) - 2

modeEncodingLength = modeEncodingLengths[messageType][0 if selectedVersion < 10 else 1 if selectedVersion < 27 else 2 if selectedVersion < 41 else -1]
if modeEncodingLength == -1:
    raise ValueError("Version not supported")

binMessageLength = [getBinaryFromInteger(messageLength, modeEncodingLength)]
currentBits += len(binMessageLength[0]) - 2

encodeGroups = []
if messageLength % modeStorage[messageType]["multiple"]["charactersNumber"] == 0:

    messageLengthIsMultiple = True
    charactersNumber = modeStorage[messageType]["multiple"]["charactersNumber"]

    for idx in range(0, messageLength, charactersNumber):
        groupToEncode = ""
        if idx % charactersNumber == 0:
            for i in range(charactersNumber):
                groupToEncode += message[idx + i]
            encodeGroups.append(groupToEncode)
else:
    messageLengthIsMultiple = False

    charactersNumber = modeStorage[messageType]["multiple"]["charactersNumber"]
    remainingCharactersNumber = modeStorage[messageType]["remaining"]["charactersNumber"]

    remainingCharacters = message[-remainingCharactersNumber:]
    newMessage = message[:-remainingCharactersNumber]
    newMessageLength = len(newMessage)

    for idx in range(0, newMessageLength, charactersNumber):
        groupToEncode = ""
        if idx % charactersNumber == 0:
            for i in range(charactersNumber):
                groupToEncode += newMessage[idx + i]
            encodeGroups.append(groupToEncode)

    encodeGroups.append(remainingCharacters)

multipleBitGroupLength = int(modeStorage[messageType]["multiple"]["charactersNumber"] * modeStorage[messageType]["multiple"]["bitsPerCharacter"])
remainingBitGroupLength = int(modeStorage[messageType]["remaining"]["charactersNumber"] * modeStorage[messageType]["remaining"]["bitsPerCharacter"])

binMessage = ""
for group in encodeGroups:
    if len(group) == 2:
        match messageType:
            case "numeric":
                #groupEncodedMessage = encodeNumeric("multiple", multipleBitGroupLength, group)
                ...
            case "alphanumeric":
                groupEncodedMessage = encodeAlphanumeric("multiple", multipleBitGroupLength, group)
            case "binary":
                #groupEncodedMessage = encodeBinary("multiple", multipleBitGroupLength, group)
                ...
            case "kanji":
                #groupEncodedMessage = encodeKanji("multiple", multipleBitGroupLength, group)
                ...

    elif len(group) == 1:
        match messageType:
            case "numeric":
                #groupEncodedMessage = encodeNumeric("remaining", remainingBitGroupLength, group)
                ...
            case "alphanumeric":
                groupEncodedMessage = encodeAlphanumeric("remaining", remainingBitGroupLength, group)
            case "binary":
                #groupEncodedMessage = encodeBinary("remaining", remainingBitGroupLength, group)
                ...
            case "kanji":
                #groupEncodedMessage = encodeKanji("remaining", remainingBitGroupLength, group)
                ...

    binMessage += groupEncodedMessage + " "

binMessage = [binMessage[:-1]]
currentBits += len(binMessage[0].replace("0b", "").replace(" ", ""))

binTerminator = [getTerminatorBits(totalVersionCodewordBits, currentBits)]
currentBits += len(binTerminator[0]) - 2

bitStream = [binSelectedMode, binMessageLength, binMessage, binTerminator]

bitString = ""
for segment in bitStream:
    bitString += segment[0].replace("0b", "").replace(" ", "")

if len(bitString) % 8 != 0:
    additionalBits = 8 - (len(bitString) % 8)
    bitString += "0" * additionalBits
    currentBits += additionalBits

if len(bitString) < totalVersionCodewordBits:
    padBytes1 = "11101100"
    padBytes2 = "00010001"

    repetitions = (totalVersionCodewordBits - len(bitString)) // 8
    for i in range(repetitions):
        if i % 2 == 0:
            bitString += padBytes1
        else:
            bitString += padBytes2

    currentBits += repetitions * 8

bitStream = []
for i in range(0, len(bitString), 8):
    print(i)
    bitStream.append("0b" + bitString[i:i+8])

print(messageSpecs)
print(bitString)
print(bitStream)
print(len(bitStream))