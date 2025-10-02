errorCorrections: dict = {
    1: {
        "L": {
            "group1": {
                "blocks": 1,
                "codewordsPerBlock": 19,
            }, 
            "group2": {
                "blocks": 0,
                "codewordsPerBlock": 0,
            },
            "ecCodewordsPerBlock": 7,
        },
        "M": {
            "group1": {
                "blocks": 1,
                "codewordsPerBlock": 16,
            }, 
            "group2": {
                "blocks": 0,
                "codewordsPerBlock": 0,
            },
            "ecCodewordsPerBlock": 10,
        },
        "Q": {
            "group1": {
                "blocks": 1,
                "codewordsPerBlock": 13,
            }, 
            "group2": {
                "blocks": 0,
                "codewordsPerBlock": 0,
            },
            "ecCodewordsPerBlock": 13,
        },
        "H": {
            "group1": {
                "blocks": 1,
                "codewordsPerBlock": 9,
            }, 
            "group2": {
                "blocks": 0,
                "codewordsPerBlock": 0,
            },
            "ecCodewordsPerBlock": 17,
        }
    }, 
    2: {
        "L": {
            "group1": {
                "blocks": 1,
                "codewordsPerBlock": 34,
            }, 
            "group2": {
                "blocks": 0,
                "codewordsPerBlock": 0,
            },
            "ecCodewordsPerBlock": 10,
        },
        "M": {
            "group1": {
                "blocks": 1,
                "codewordsPerBlock": 28,
            }, 
            "group2": {
                "blocks": 0,
                "codewordsPerBlock": 0,
            },
            "ecCodewordsPerBlock": 16,
        },
        "Q": {
            "group1": {
                "blocks": 1,
                "codewordsPerBlock": 2,
            }, 
            "group2": {
                "blocks": 0,
                "codewordsPerBlock": 0,
            },
            "ecCodewordsPerBlock": 22,
        },
        "H": {
            "group1": {
                "blocks": 1,
                "codewordsPerBlock": 16,
            }, 
            "group2": {
                "blocks": 0,
                "codewordsPerBlock": 0,
            },
            "ecCodewordsPerBlock": 28,
        }
    }, 
    5: {
        "Q": {
            "group1": {
                "blocks": 2,
                "codewordsPerBlock": 15,
            }, 
            "group2": {
                "blocks": 2,
                "codewordsPerBlock": 16,
            },
            "ecCodewordsPerBlock": 18,
        }
    }
}

def separateGroups(data:list[str], specifications:dict) -> list[list[str]]:
    selectedVersion = specifications["selectedVersion"]
    errorCorrectionLevel = specifications["errorCorrectionLevel"]
    
    groupBlocks = [0]

    group1Blocks = errorCorrections[selectedVersion][errorCorrectionLevel]["group1"]["blocks"]
    group1Codewords = errorCorrections[selectedVersion][errorCorrectionLevel]["group1"]["codewordsPerBlock"]
    
    indexSum = 0
    for i in range(group1Blocks):
        indexSum += group1Codewords
        groupBlocks.append(indexSum)

    group2Blocks = errorCorrections[selectedVersion][errorCorrectionLevel]["group2"]["blocks"]
    group2Codewords = errorCorrections[selectedVersion][errorCorrectionLevel]["group2"]["codewordsPerBlock"]

    for i in range(group2Blocks):
        indexSum += group2Codewords
        groupBlocks.append(indexSum)

    blocks = []
    for idx in range(len(groupBlocks)):
        if idx + 1 == len(groupBlocks):
            break
        codewordBlocks = data[groupBlocks[idx]:groupBlocks[idx+1]]
        blocks.append(codewordBlocks)
    
    groups = []

    group1 = []
    if group1Blocks > 0:
        for i in range(group1Blocks):
            group1.append(blocks[i])
    else:
        group1.append([])

    group2 = []
    if group2Blocks > 0:
        for i in range(group2Blocks):
            i += group1Blocks
            group2.append(blocks[i])
    else:
        group2.append([])

    groups.append(group1)
    groups.append(group2)

    return groups

def convertDecimal(data:list) -> list:
    dataGroup1 = data[0]

    group1Blocks = []
    for block in dataGroup1:
        bytesList = []

        for byte in block:
            bytesList.append(int(byte, 2))

        group1Blocks.append(bytesList)
    

    dataGroup2 = data[1]

    group2Blocks = []
    for block in dataGroup2:
        bytesList = []

        for byte in block:
            bytesList.append(int(byte, 2))

        group2Blocks.append(bytesList)

    return [group1Blocks, group2Blocks]

'''groupTest = separateGroups({'messageLength': 11, 'messageType': 'alphanumeric', 'selectedVersion': 5, 'errorCorrectionLevel': 'Q'}, ["0b01000011",
"0b01010101",
"0b01000110",
"0b10000110",
"0b01010111",
"0b00100110",
"0b01010101",
"0b11000010",
"0b01110111",
"0b00110010",
"0b00000110",
"0b00010010",
"0b00000110",
"0b01100111",
"0b00100110",
"0b11110110",
"0b11110110",
"0b01000010",
"0b00000111",
"0b01110110",
"0b10000110",
"0b11110010",
"0b00000111",
"0b00100110",
"0b01010110",
"0b00010110",
"0b11000110",
"0b11000111",
"0b10010010",
"0b00000110",
"0b10110110",
"0b11100110",
"0b11110111",
"0b01110111",
"0b00110010",
"0b00000111",
"0b01110110",
"0b10000110",
"0b01010111",
"0b00100110",
"0b01010010",
"0b00000110",
"0b10000110",
"0b10010111",
"0b00110010",
"0b00000111",
"0b01000110",
"0b11110111",
"0b01110110",
"0b01010110",
"0b11000010",
"0b00000110",
"0b10010111",
"0b00110010",
"0b11100000",
"0b11101100",
"0b00010001",
"0b11101100",
"0b00010001",
"0b11101100",
"0b00010001",
"0b11101100"])'''

def appendErrorCorrection(data:list, specifications:dict) -> list:
    groups = separateGroups(data, specifications)

    coefficients = convertDecimal(groups)

    print(coefficients)
