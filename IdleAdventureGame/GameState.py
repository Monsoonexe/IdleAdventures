#GameState.py
from enum import Enum
GameState = Enum("GameState", "IDLE, WALKING, TOWN, INNREST, CAMPREST," +
    "SHOP, BATTLE")
