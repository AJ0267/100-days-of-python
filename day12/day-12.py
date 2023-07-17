#namespcaes: Local vs Global Scope

enemies = 1 

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside of function: {enemies}")

# >>>> enemies inside function: 2
# >>>> enemies outside of function: 1



#Local Scope: Local scope exists within a function.

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
print(potion_strength)

# >>>> NameError: name 'potion_strength' is not defined



#Global Scope

player_health = 10
def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)
    drink_potion()
print(player_health)

# >>>> 10



#example

game_level = 3
def create_enemy():
    enemies = ["skeleton", "zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]
   print(new_enemy)



#modifying global scope:

enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")