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
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
        "G": 16,
        "H": 17,
        "I": 18,
        "J": 19,
        "K": 20,
        "L": 21,
        "M": 22,
        "N": 23,
        "O": 24,
        "P": 25,
        "Q": 26,
        "R": 27,
        "S": 28,
        "T": 29,
        "U": 30,
        "V": 31,
        "W": 32,
        "X": 33,
        "Y": 34,
        "Z": 35,
        " ": 36,
        "$": 37,
        "%": 38,
        "*": 39,
        "+": 40,
        "-": 41,
        ".": 42,
        "/": 43,
        ":": 44
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
        encodedKeys = "0" * (groupLength - len(binaryKeysSum)) + binaryKeysSum

    elif len(binaryKeysSum) == groupLength:
        encodedKeys = binaryKeysSum

    else:
        raise ValueError("Data too long for specified length")

print(encodeAlphanumeric("multiple", 11, "HE"))