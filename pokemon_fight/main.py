import random
import pokemon as pkmn
from damage import deal_damage

# Create the roster of Pokemon to choose from
roster = [pkmn.pikachu, pkmn.mudkip]

# Create a nice separator
separator = "--------"


# let the player select one Pokémon out of the roster
selected_pkmn = None

while selected_pkmn is None:
    print("Please select your Pokémon")
    for num, mon in enumerate(roster, 1):
        print(num, mon.name)
    selected_pkmn = input()
    try:
        selected_pkmn = int(selected_pkmn) - 1
        print(f"You selected {roster[selected_pkmn].name}.")
        # let's use pop to assign the selected pokemon to the player, and remove it from the roster
        # this avoids mirror matches
        player = roster.pop(selected_pkmn)
    except (ValueError, IndexError):
        print("Incorrect input")
        selected_pkmn = None


# the cpu will pick randomly one pokemon

cpu = random.choice(roster)

print(f"The CPU selected {cpu.name}.")

# main game loop

while player.current_hp > 0 and cpu.current_hp > 0:
    # let the player select a move
    player.select_move()
    # the cpu picks its move
    cpu.cpu_select_move()
    # check which one is faster. If it's a tie, pick randomly.
    if player.speed > cpu.speed:
        first = player
        last = cpu
    elif cpu.speed > player.speed:
        first = cpu
        last = player
    else:
        mons = random.shuffle([player, cpu])
        first, last = mons
    print(f"{first.name} uses {first.next_move.name}.")
    # deal damage here
    deal_damage(first, last)
    # check if last is ko, if yes, exit the loop
    if last.current_hp <= 0:
        break
    print(f"{last.name} uses {last.next_move.name}.")
    # deal damage here
    deal_damage(last, first)
    # check if first is ko, if yes, exit the loop
    if first.current_hp <= 0:
        break
    print(separator)
