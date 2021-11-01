def wake_up_check(pkmn):
    if pkmn.status == "Sleep":
        pkmn.sleep_count -= (
            1  # remove one from the sleep counter, so that it lasts 1 to 5 turns
        )
        if pkmn.sleep_count == 0:
            pkmn.status = ""
            print(f"{pkmn.name} woke up!")
            return True
        else:
            print(f"{pkmn.name} is fast asleep…")
            return False
    else:  # pokemon wasn't even asleep
        return True
