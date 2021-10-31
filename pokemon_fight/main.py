import random
from time import sleep
import pokemon as pkmn
from damage import deal_damage

# Create the roster of Pokemon to choose from
roster = pkmn.roster

# Create a nice separator
separator = "--------"

# set sleep time (in seconds) between attacks resolution (it's too fast without it)
sleep_time = 1

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
sleep(sleep_time)
cpu = random.choice(roster)
print(f"The CPU selected {cpu.name}.")

# main game loop
while True:
    print(separator)
    # print the current status
    game_state = f"{player.name}: HP {player.current_hp}/{player.max_hp} {player.status}~~ {cpu.name}: HP {'{:.0%}'.format(cpu.current_hp/cpu.max_hp)}. {cpu.status}"
    print(game_state)
    # let the player select a move
    print(separator)
    sleep(sleep_time)
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
        mons = [player, cpu]
        random.shuffle(mons)
        first, last = mons
    print(f"{first.name} moves first.")
    sleep(sleep_time)
    # first attack
    print(f"{first.name} uses {first.next_move.name}.")
    # deal damage here
    deal_damage(first, last)
    sleep(sleep_time)
    # check if last is ko, if yes, exit the loop
    if last.current_hp <= 0:
        print(f"{last.name} is KO. {first.name} won.")
        break

    # slower pokemon's attack
    print(f"{last.name} uses {last.next_move.name}.")
    # deal damage here
    deal_damage(last, first)
    sleep(sleep_time)
    # check if first is ko, if yes, exit the loop
    if first.current_hp <= 0:
        print(f"{first.name} is KO. {last.name} won.")
        break
    print("Thank you for playing. Good bye.")
