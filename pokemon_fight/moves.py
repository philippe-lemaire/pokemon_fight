from models import Move

thunderbolt = Move("Thunderbolt", 95, None, 15, 100, "Special", "Electric")
tackle = Move(
    "Tackle",
    50,
    None,
    30,
    95,
    "Physical",
    "Normal",
)
watergun = Move("Water Gun", 40, None, 20, 100, "Special", "Water")
ember = Move("Ember", 40, None, 20, 100, "Special", "Fire")
irontail = Move(
    "Iron Tail",
    70,
    None,
    20,
    70,
    "Physical",
    "Steel",
)

bodyslam = Move("Body Slam", 80, None, 12, 100, "Physical", "Normal")

poisonpowder = Move("Poison Powder", 0, "Poison", 5, 70, "Status", "Poison")

willowisp = Move("Will'o Wisp", 0, "Burn", 5, 100, "Status", "Fire")

sleeppowder = Move("Sleep Powder", 0, "Sleep", 5, 70, "Status", "Grass")

thunderwave = Move("Thunder Wave", 0, "Paralysis", 5, 100, "Status", "Electric")

vinewhip = Move("Vine Whip", 40, None, 20, 100, "Physical", "Grass")

hyperfang = Move("Hyper Fang", 90, None, 10, 70, "Physical", "Normal")

rocktomb = Move("Rock Tomb", 80, None, 10, 90, "Physical", "Rock")

earthquake = Move("Earthquake", 100, None, 10, 100, "Physical", "Ground")
