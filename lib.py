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
