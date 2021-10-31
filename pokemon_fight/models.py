# This file contains the classes used to model the Pokémon and their moves
import random


class Pokemon:
    """Class used to model a Pokemon"""

    def __init__(
        self,
        name,
        hp,
        attack,
        defense,
        special_attack,
        special_defense,
        speed,
        type,
        moves,
    ):
        self.name = name.capitalize()
        self.max_hp = hp
        self.current_hp = hp
        self.attack = attack
        self.defense = defense
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.speed = speed
        self.type = type.capitalize()
        self.status = ""
        self.attack_mod = 1
        self.defense_mod = 1
        self.special_attack_mod = 1
        self.special_defense_mod = 1
        self.speed_mod = 1
        self.moves = moves
        self.next_move = None

    def __str__(self):
        return f"{self.name}: {self.current_hp}/{self.max_hp} {self.status}"

    def __repr__(self):
        return f"Pokemon({self.name}, {self.max_hp}, {self.attack}, {self.defense}, {self.special_attack}, {self.special_defense}, {self.speed}, {self.type})"

    def select_move(self):
        print("Select your move:")
        for num, move in enumerate(self.moves, 1):
            print(f"{num}: {move}")

        selected_move = None
        while selected_move not in range(0, len(self.moves)):
            selected_move = input(
                "Please type the number of the move you want to do this turn:\n"
            )
            try:
                selected_move = int(selected_move)
                selected_move -= 1
            except ValueError:
                print("Invalid input")
                selected_move = None
        self.next_move = self.moves[selected_move]
        print(f"You selected {self.moves[selected_move].name}.")

    def cpu_select_move(self):
        """this method will be used by the CPU only"""
        self.next_move = random.choice(self.moves)


class Move:
    """Class used to model a move, such as Thunderbolt or Poison Powder"""

    def __init__(self, name, base_power, pp, kind, type, desc):
        self.name = name.capitalize()
        self.base_power = base_power
        self.max_pp = pp
        self.current_pp = pp
        self.kind = kind.capitalize()
        self.type = type.capitalize()
        self.desc = desc.capitalize()

    def __str__(self):
        return f"{self.name}. Base Power: {self.base_power}. PP: {self.max_pp}. Kind: {self.kind}. Type: {self.type}. {self.desc}."

    def __repr__(self):
        return f"{self.name}. PP: {self.current_pp}/{self.max_pp}"
