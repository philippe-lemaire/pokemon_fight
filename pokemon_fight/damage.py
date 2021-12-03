from random import randint
from type_effectiveness import double_effective, resists


def deal_damage(attacker, target):
    # compute attack side of the damage formula
    move = attacker.next_move
    # remove 1 pp
    move.current_pp -= 1
    # check physical / special for damage calc
    if move.kind.capitalize() == "Physical":
        attack_power = move.base_power * attacker.attack / 100
    if move.kind.capitalize() == "Special":
        attack_power = move.base_power * attacker.special_attack / 100

    if move.kind.capitalize() == "Status":
        attack_power = 0
        defense_power = 0
    # apply STAB (same type attack bonus)
    if move.type == attacker.type and move.kind in ["Physical", "Special"]:
        attack_power = attack_power * 1.5

    # Compute defense side
    if move.kind.capitalize() == "Physical":
        defense_power = target.defense
    if move.kind.capitalize() == "Special":
        defense_power = target.special_defense

    # damage formula. I use int on the result to get a whole number
    damage = int(attack_power * (1 - defense_power / 200))

    # check for accuracy if the attack missed, we return something here to skip the rest of the function.
    # We have no real value to return, so we can just return None
    roll = randint(1, 100)
    if roll > move.accuracy:
        print(f"{attacker.name}’s attack {move.name} missed.")
        return None

    # check for 25% chance of not attacking if paralysis. Return None in this case to skip the rest of the function.
    if attacker.status == "Paralysis":
        if randint(1, 100) <= 25:
            print(f"{attacker.name} is fully paralyzed. It could not attack.")
            return None

    # check for random chance of crit. It's a 5% chance, so like rolling a 20 on a 20 sided dice
    # but only if there is damage above 0. if damage allows us to check if damage is above 0
    # we will apply type effectiveness here as well, stored in 2 dictionaries objects in another file we imported above
    if damage:
        if randint(1, 20) == 20:
            print("\nA critical hit!\n")
            damage = damage * 2
        # check for type effectiveness
        if target.type in double_effective.get(move.type, []):
            damage = damage * 2
            print("It's super effective!")
        if move.type in resists.get(target.type, []):
            damage = damage // 2
            print("It's not very effective…")

    # deal the damage
    target.current_hp -= damage

    # apply status but only if there isn't one already
    if not target.status and move.status_affliction:
        target.status = move.status_affliction
        print(f"{attacker.name} inflicted {move.status_affliction} to {target.name}.")
        if target.status == "Paralysis":
            target.speed = target.speed // 2
        if target.status == "Burn":
            target.attack = target.attack // 2
        if target.status == "Sleep":
            target.sleep_count = randint(1, 5)
    # print some feedback for the user
    if damage:
        print(
            f"{target.name} took damage: {'{:.0%}'.format(damage/target.max_hp)} of its total HP."
        )


def apply_status_damage(pkmn):
    if pkmn.status in ["Poison", "Burn"]:
        damage = pkmn.max_hp // 8
        pkmn.current_hp -= damage
        message = f"{pkmn.name} took {pkmn.status} damage: {damage} HP."
        print(message)
