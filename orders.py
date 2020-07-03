import uuid

def vulture_1_1():
    item = {
    "id": "Vulture_" + str(uuid.uuid4()),
    "username": "Amber Vulture",
    "turn": 1.1,
    "ep": {
        "linguistics": 0,
        "arithmetics": 0,
        "rhetoric": 1,
        "archives": 0,
        "sympathy": 0,
        "physicking": 3,
        "alchemy": 0,
        "artificery": 0,
        "naming": 1
    },
    "complaints": ["Amethyst Scorpion", "Coral Swan"],
    "attend_imre": True
    }
    return item

def vulture_1_2():
    item = {
    "id": "Vulture_" + str(uuid.uuid4()),
    "username": "Amber Vulture",
    "turn": 1.2,
    "ep": {
        "linguistics": 0,
        "arithmetics": 0,
        "rhetoric": 0,
        "archives": 0,
        "sympathy": 0,
        "physicking": 0,
        "alchemy": 0,
        "artificery": 0,
        "naming": 0
    },
    "complaints": ["Amethyst Scorpion", "Amethyst Scorpion"],
    "attend_imre": False,
    "lodging": "Windy Tower"
    }
    return item

def scorpion_1_1():
    item = {
    "id": "Scorpion_" + str(uuid.uuid4()),
    "username": "Amethyst Scorpion",
    "turn": 1.1,
    "ep": {
        "linguistics": 5,
        "arithmetics": 0,
        "rhetoric": 0,
        "archives": 0,
        "sympathy": 0,
        "physicking": 0,
        "alchemy": 0,
        "artificery": 0,
        "naming": 0
    },
    "complaints": ["Amber Vulture", "Coral Swan"],
    "attend_imre": False
    }
    return item

def scorpion_1_2():
    item = {
    "id": "Scorpion_" + str(uuid.uuid4()),
    "username": "Amethyst Scorpion",
    "turn": 1.2,
    "ep": {
        "linguistics": 5,
        "arithmetics": 0,
        "rhetoric": 0,
        "archives": 0,
        "sympathy": 0,
        "physicking": 0,
        "alchemy": 0,
        "artificery": 0,
        "naming": 0
    },
    "complaints": ["Coral Swan", "Coral Swan"],
    "attend_imre": False,
    "lodging": "Windy Tower"
    }
    return item

def swan_1_1():
    item = {
    "id": "Swan_" + str(uuid.uuid4()),
    "username": "Coral Swan",
    "turn": 1.1,
    "ep": {
        "linguistics": 5,
        "arithmetics": 0,
        "rhetoric": 0,
        "archives": 0,
        "sympathy": 0,
        "physicking": 0,
        "alchemy": 0,
        "artificery": 0,
        "naming": 5
    },
    "complaints": ["Amber Vulture", "Amethyst Scorpion"],
    "attend_imre": False
    }
    return item

def swan_1_2():
    item = {
    "id": "Swan_" + str(uuid.uuid4()),
    "username": "Coral Swan",
    "turn": 1.2,
    "ep": {
        "linguistics": 0,
        "arithmetics": 0,
        "rhetoric": 0,
        "archives": 0,
        "sympathy": 0,
        "physicking": 0,
        "alchemy": 2,
        "artificery": 3,
        "naming": 0
    },
    "complaints": ["Amethyst Scorpion", "Amethyst Scorpion"],
    "attend_imre": False,
    "lodging": "Windy Tower"
    }
    return item