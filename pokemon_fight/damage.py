def deal_damage(attacker, target):
    # compute attack side of the damage formula
    move = attacker.next_move
    if move.kind.capitalize() == "Physical":
        attack_power = move.base_power * attacker.attack
    if move.kind.capitalize() == "Special":
        attack_power = move.base_power * attacker.special_attack
    # apply STAB (same type attack bonus)
    if move.type == attacker.type:
        attack_power = attack_power * 1.5

    # Compute defense side
    if move.kind.capitalize() == "Physical":
        defense_power = target.defense
    if move.kind.capitalize() == "Special":
        defense_power = target.special_defense

    # damage formula
    damage = attack_power * (1 - defense_power / 200)
    # deal the damage
    target.current_hp -= damage
    # print some feedback for the user
    print(f"{target.name} took {'{:.0%}'.format(damage/target.max_hp)} of its total HP as damage.")
