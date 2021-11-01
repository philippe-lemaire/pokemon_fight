# Pokemon Fight
A simple text based Pokémon fighting games, for EM Lyon students.

## Steps I took to make it

1. Create 2 classes to model Pokemon and Moves. Think about the attributes they need to function. Moves need at least a base power, but to model the game more closely, they also need a type, power points (PP) that are spent when the move is used, a kind (Physical, Special, or Status) and an accuracy value (some strong moves don't land 100% of the time). 
1. Add a `__str__` method to the Move class showing what a player should see about the move when it's printed on screen.
1. Inside your Pokemon class, create a method to let the player pick a move. Store the move picked in an attribute of the pokemon class such as next_move, we'll use it later
1. Still in teh Pokemon class, create a separate method for the cpu to pick a move, with no player input. the CPU can pick its move randomly (most real cpu trainers do in the real games) or you can make a smarter CPU that picks the most damaging move. But before you can do that you need to work on the damage function, see later
2. Create some instances of moves, and some instances of pokemon. Store at least 2 pokemon in a list that you can call roster. It's from this list the player and CPU will pick their pokemon for the fight
1. In the main script, start with allowing the user to pick a pokemon from the roster, and have the CPU pick randomly from the pokemon not picked by the player
3. Create your main game loop. It can be an infinite while True loop, but it needs break points if a pokemon reaches HP below 1.
1. In the game loop, have the player pick his move with the method you wrote earlier inside the pokemon class. Have the CPU pick his move
1. Determine who attacks first and last, by comparing pokemon speeds
1. Resolve the attacks. You'll need some damage formula. Write a separate function that takes 2 pokemon as argument (atacker, target), reads the move stored in the attacker's next_move attribute, computes the damage based on a formula of your choosing, and changes the HP of the target. In the damage formula itself, the kind of move (Physical, Special) determines if the formula uses attack and defense or special attack and special defense. These stats combined with the move's base power should determine the damage dealt. Once damage is calculated, substract it from the target's hp. Try to not have all attacks KO in one hit. Defense should reduce the damage, but not to the point of damage being negative, that would heal the target.
Bonus points: check for accuracy. A move with 70 accuracy should have a 30% chance of missing. Apply the "Same Type Attack Bonus": if the attacker and its move have the same type, multipy the damage by 1.5. Add a crit chance. If the move connects, 5% of the time it should be a critical hit, and deal double damage. Print some message when that happens, ie : "A critical hit!"
1. In your main loop, use the attack resolution function with the fastest pokemon as the attacker and the slowest as the target first, check if there's a ko, then use the attack resolution function again with the slowest pokemon as the attacker, check again for a ko. If there's no ko, the loop continues and you pick your next move.

## General Tips :

1. Do all this step by step and have fun with it. This is absolutely doable with the basic notions we've seen in class. It can take you a while, don't try to do it all in one session. If you are stuck, go do something else and think about it during the day, you'll probably think of a solution yourself, while away from the computer. This means you should start the project as early as possible, to give you time.
1. This is fully a text based interface, so add usefull prints to show the user (and yourself) what's going on: attacks used, damage dealt, hp left, status, and so on.
1. As text will print very fast, it can be hard to read when playing. You can use the function time.sleep(1) (import time first) to make the game pause for a second at some points during the main loop.

## Extra stuff you can do when the basic loop is working:

1. Implement status moves, that don't deal damage directly
    - paralysis reduces target's speed by half, and add a 25% chance to not being able to use a move
    - burn cuts target's attack by half, and deals 1/8 of target's max hp at the end of the turn
    - poison deals 1/8 of target's max hp at the end of the turn
    - sleep : targets falls asleep for a random number of turns, between 1 and 5. User still picks moves but unless the pokemon wakes up, they're not used (no pp spent).


    A pokemon can only have one status at a time, sleep is the only one that heals itself after a while.
1. Implement type effectiveness on moves versus target. Fire moves deal double damage on Grass targets, half damage on fire and water targets, and so on. Keep the pokemon simple by having a unique type. You can do this with 2 dictionaries, one for double effective move type versus target, the second with resisting target type versus move type. Do the checks in your damage function. You don't need to implement all the 18 types, Fire, Grass and Water is already great.
1. Make sure the user inputs are robust: if the user inputs something invalid, the code should not break, but repeat the prompt until the input is valid (use a while {answer is not valid} loop to have robust inputs)
