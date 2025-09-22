versions = {
    1: {
        "L": {
            "dataBits": 152, 
            "numeric": 41, 
            "alphanumeric": 25,
            "binary": 17, 
            "kanji": 10
        }, 
        "M": {
            "dataBits": 128, 
            "numeric": 34, 
            "alphanumeric": 20,
            "binary": 14, 
            "kanji": 8
        }
    }, 
    2: {
        "L": {
            "dataBits": 272, 
            "numeric": 77, 
            "alphanumeric": 47,
            "binary": 32, 
            "kanji": 20
        }
    }
}

modes: dict[str, str] = {
    "numeric": "0b0001", 
    "alphanumeric": "0b0010",
    "binary": "0b0100", 
    "kanji": "0b1000"
}

modeEncodingLengths: dict[str, list[int]] = {
    "numeric": [10, 12, 14],
    "alphanumeric": [9, 11, 13],
    "binary": [8, 16, 16],
    "kanji": [8, 10, 12]
}

modeStorage: dict = {
    "numeric": {
        "charactersNumber": 3, 
        "bitsPerCharacter": 3 + 1/3
    }, 
    "alphanumeric": {
        "multiple": {
            "charactersNumber": 2,
            "bitsPerCharacter": 5 + 1/2
        }, 
        "remaining": {
            "charactersNumber": 1,
            "bitsPerCharacter": 6
        }
    },
    "binary": {
        "charactersNumber": 1,
        "bitsPerCharacter": 8
    },
    "kanji": {
        "charactersNumber": 1,
        "bitsPerCharacter": 10
    }
}