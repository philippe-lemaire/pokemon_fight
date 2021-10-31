from models import Pokemon
import moves

pikachu = Pokemon(
    "Pikachu", 100, 50, 60, 90, 80, 120, "Electric", [moves.tackle, moves.thunderbolt]
)

mudkip = Pokemon(
    "Mudkip", 90, 60, 60, 70, 100, 90, "Water", [moves.tackle, moves.watergun]
)
