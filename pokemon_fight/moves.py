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

bodyslam = Move("Body Slam", 80, None, 1, 100, "Physical", "Normal")

poisonpowder = Move("Poison Powder", 0, "Poison", 5, 70, "Status", "Poison")

willowisp = Move("Will'o Wisp", 0, "Burn", 5, 80, "Status", "Fire")

sleeppowder = Move("Sleep Powder", 0, "Sleep", 5, 70, "Status", "Grass")
thunderwave = Move("Thunder Wave", 0, "Paralysis", 5, 100, "Status", "Electric")
