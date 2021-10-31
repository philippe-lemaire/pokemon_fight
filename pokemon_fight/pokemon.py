from models import Pokemon
import moves

pikachu = Pokemon(
    "Pikachu",
    100,
    50,
    60,
    90,
    80,
    120,
    "Electric",
    [moves.tackle, moves.thunderbolt, moves.irontail],
)

mudkip = Pokemon(
    "Mudkip", 90, 60, 60, 70, 100, 120, "Water", [moves.tackle, moves.watergun]
)

chimchar = Pokemon(
    "Chimchar",
    70,
    70,
    55,
    90,
    100,
    120,
    "Fire",
    [moves.ember, moves.tackle, moves.irontail],
)

rattata = Pokemon(
    "Rattata",
    40,
    90,
    90,
    40,
    50,
    130,
    "Normal",
    [moves.bodyslam, moves.tackle, moves.watergun],
)
roster = [pikachu, mudkip, chimchar, rattata]
