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
    [moves.tackle, moves.thunderbolt, moves.irontail, moves.thunderwave],
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
    [moves.ember, moves.tackle, moves.irontail, moves.willowisp],
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

bulbasaur = Pokemon(
    "Bulbasaur",
    120,
    70,
    90,
    90,
    80,
    70,
    "Grass",
    [moves.vinewhip, moves.sleeppowder, moves.bodyslam, moves.poisonpowder],
)

geodude = Pokemon(
    "Geodude",
    100,
    120,
    80,
    20,
    60,
    70,
    "Rock",
    [moves.earthquake, moves.rocktomb, moves.tackle],
)
roster = [
    pikachu,
    mudkip,
    chimchar,
    bulbasaur,
    rattata,
    geodude,
]
