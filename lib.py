def xor(num1:str, num2:str) -> str:
    bin1, bin2 = num1[2:], num2[2:]
    lenBin1, lenBin2 = len(bin1), len(bin2)

    if lenBin1 != lenBin2:
        maxLen, minLen = max(lenBin1, lenBin2), min(lenBin1, lenBin2)
        digitsToAdd = maxLen - minLen

        if lenBin1 < lenBin2:
            bin1 = "0" * digitsToAdd + bin1
        elif lenBin1 > lenBin2:
            bin2 = "0" * digitsToAdd + bin2

    try:
        desiredLen = maxLen

    except:
        desiredLen = 8

    binResult = ""
    for idx in range(desiredLen):
        d1, d2 = bin1[idx], bin2[idx]

        binResult += str((int(d1) + int(d2)) % 2)

    if len(binResult) > 8:
        binResult = binResult[-8:]

    return "0b" + binResult

def modulo285(num:str):
    binNum = num[2:]

    while True:

        for i in range(1, 255):

        if len(binNum) > 8:
            break

    if num1 >= 512:
        return xor(num1, "0b100011101")
    elif num1 >= 256:

def getTotalDataCodewordBits(table:dict, version: int, errorCorrectionLevel: str) -> int:
    specs: dict = table[version][errorCorrectionLevel]

    group1Blocks, group1CodewordsPerBlock = specs["group1"]["blocks"], specs["group1"]["codewordsPerBlock"]
    group2Blocks, group2CodewordsPerBlock = specs["group2"]["blocks"], specs["group2"]["codewordsPerBlock"]

    return (group1Blocks * group1CodewordsPerBlock + group2Blocks * group2CodewordsPerBlock) * 8

def getTerminatorBits(totalBits: int, currentBits: int) -> str:
    remainingBits = totalBits - currentBits

    if remainingBits >= 4:
        terminatorBits = "0b" + 4 * "0"

    elif 0 < remainingBits < 4:
        terminatorBits = "0b" + remainingBits * "0"
    
    else:
        terminatorBits = "0b"

    return terminatorBits

def getBinaryFromInteger(data: int | str, length: int) -> int:
    if isinstance(data, str):
        data = int(data)

    binData = bin(data)
    lengthBinData = len(str(binData)[2:])

    if  lengthBinData < length:
        binData = "0b" +"0" * (length - lengthBinData) + binData[2:]

    elif lengthBinData > length:
        raise ValueError("Data too long for specified length")

    return binData

def getBinaryFromAscii(data: str) -> str:
    return ''.join(format(ord(i), '08b') for i in data)

def encodeAlphanumeric(mode: str, groupLength: int, data: str) -> str:
    ALPHANUMERIC_TABLE: dict[str, int] = { 
        "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, 
        "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "G": 16, "H": 17, "I": 18, "J": 19, "K": 20, "L": 21, "M": 22, "N": 23, "O": 24, "P": 25, "Q": 26, "R": 27, "S": 28, "T": 29, "U": 30, "V": 31, "W": 32, "X": 33, "Y": 34, "Z": 35, 
        " ": 36, "$": 37, "%": 38, "*": 39, "+": 40, "-": 41, ".": 42, "/": 43, ":": 44
    }

    if mode == "multiple":
        key1, char1 = ALPHANUMERIC_TABLE.get(data.upper()[0]), data.upper()[0]
        key2, char2 = ALPHANUMERIC_TABLE.get(data.upper()[1]), data.upper()[1]

        keysSum = key1 * 45 + key2

    elif mode == "remaining":
        key1, char1 = ALPHANUMERIC_TABLE.get(data.upper()[0]), data.upper()[0]

        keysSum = key1

    binaryKeysSum = bin(keysSum)[2:]

    if len(binaryKeysSum) < groupLength:
        encodedKeys = "0b" + "0" * (groupLength - len(binaryKeysSum)) + binaryKeysSum

    elif len(binaryKeysSum) == groupLength:
        encodedKeys = "0b" + binaryKeysSum

    else:
        raise ValueError("Data too long for specified length")
    
    return encodedKeys

print(xor("0b00101101", "0b01100011"))


