versions = {
    1: {
        "L": {
            "numeric": 41, 
            "alphanumeric": 25,
            "binary": 17, 
            "kanji": 10
        }, 
        "M": {
            "numeric": 34, 
            "alphanumeric": 20,
            "binary": 14, 
            "kanji": 8
        },
        "Q": {
            "numeric": 27, 
            "alphanumeric": 16,
            "binary": 11, 
            "kanji": 7
        }, 
        "H": {
            "numeric": 17, 
            "alphanumeric": 10,
            "binary": 7, 
            "kanji": 4
        }
    }, 
    2: {
        "L": {
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