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
        level,
    ):
        self.name = name.capitalize()
        self.max_hp = hp
        self.current_hp = hp
        self.attack = attack
        self.defense = defense
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.speed = speed
        self.type = type
        self.status = ""
        self.attack_mod = 1
        self.defense_mod = 1
        self.special_attack_mod = 1
        self.special_defense_mod = 1
        self.speed_mod = 1
        self.moves = moves
        self.level = level
        self.next_move = None

    def __str__(self):
        return f"{self.name}: LV {self.level} - {self.current_hp}/{self.max_hp} {self.status}"

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
            if self.moves[selected_move].current_pp < 1:
                print("This move has no Power Points left.")
                selected_move = None
        self.next_move = self.moves[selected_move]

    def cpu_select_move(self):
        """this method will be used by the CPU only"""
        self.next_move = random.choice(self.moves)


class Move:
    """Class used to model a move, such as Thunderbolt or Poison Powder"""

    def __init__(self, name, base_power, status_affliction, pp, accuracy, kind, type):
        self.name = name.capitalize()
        self.base_power = base_power
        self.max_pp = pp  # optional at first
        self.accuracy = accuracy  # optional at first
        self.current_pp = pp
        self.kind = kind.capitalize()
        self.type = type.capitalize()
        self.status_affliction = status_affliction  # for status inflicting moves

    def __repr__(self):
        return f"{self.name}. Base Power: {self.base_power}. Accuracy: {self.accuracy}%. PP: {self.max_pp}. Kind: {self.kind}. Type: {self.type}."

    def __str__(self):
        return f"{self.name}. PP: {self.current_pp}/{self.max_pp}"
