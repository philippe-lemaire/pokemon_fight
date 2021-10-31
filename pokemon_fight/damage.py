def deal_damage(attacker, target):
    # compute attack side of the damage formula
    move = attacker.next_move
    if move.kind.capitalize() == "Physical":
        # Let's use int to get a whole number
        attack_power = move.base_power * attacker.attack / 100
    if move.kind.capitalize() == "Special":
        attack_power = move.base_power * attacker.special_attack / 100
    # apply STAB (same type attack bonus)
    if move.type == attacker.type:
        attack_power = attack_power * 1.5

    # Compute defense side
    if move.kind.capitalize() == "Physical":
        defense_power = target.defense
    if move.kind.capitalize() == "Special":
        defense_power = target.special_defense

    # damage formula
    damage = int(attack_power * (1 - defense_power / 200))
    # deal the damage
    target.current_hp -= damage
    # print some feedback for the user
    print(
        f"{target.name} took damage: {'{:.0%}'.format(damage/target.max_hp)} of its total HP."
    )