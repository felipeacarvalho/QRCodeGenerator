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
    }
}

def sepparateGroups(specifications:dict, data:list[str]) -> list[list[str]]:
    selectedVersion = specifications[selectedVersion]
    errorCorrectionLevel = specifications[errorCorrectionLevel]
    
    group1Blocks = errorCorrectionLevel[selectedVersion][errorCorrectionLevel]["group1"]["blocks"]
    group1Codewords = errorCorrectionLevel[selectedVersion][errorCorrectionLevel]["group1"]["codewordsPerBlock"]
    
    group2Blocks = errorCorrectionLevel[selectedVersion][errorCorrectionLevel]["group2"]["blocks"]
    group2Codewords = errorCorrectionLevel[selectedVersion][errorCorrectionLevel]["group2"]["codewordsPerBlock"]


    for seg in data:
