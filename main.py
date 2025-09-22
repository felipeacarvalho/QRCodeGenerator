from specs import *
from lib import *

message = "Hello, World!"
messageLength = len(message)
messageType = "alphanumeric"

errorCorrectionLevel = "L"

for versionIdx in versions:
    if versions[versionIdx][errorCorrectionLevel][messageType] >= messageLength:
        selectedVersion = versionIdx
        break

binSelectedMode = [modes[messageType]]

modeEncodingLength = modeEncodingLengths[messageType][0 if selectedVersion < 10 else 1 if selectedVersion < 27 else 2 if selectedVersion < 41 else -1]
if modeEncodingLength == -1:
    raise ValueError("Version not supported")

binMessageLength = [getBinaryFromInteger(messageLength, modeEncodingLength)]

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

print(encodeGroups)

multipleBitGroupLength = modeStorage[messageType]["multiple"]["charactersNumber"] * modeStorage[messageType]["multiple"]["bitsPerCharacter"]
remainingBitGroupLength = modeStorage[messageType]["remaining"]["charactersNumber"] * modeStorage[messageType]["remaining"]["bitsPerCharacter"]

for group in encodeGroups:
    if len(group) == 2:

binMessage = []

bitStream = [binSelectedMode, binMessageLength, binMessage]

print(bitStream)