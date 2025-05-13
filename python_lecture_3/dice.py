##my_list = [1, 2, 3, 4, 5]
##for item in my_list:
##    print(item)
import random

while True:
    type_of_die = int(input("choose a die (6,12,20) "))

    while type_of_die not in [6, 12, 20]:
            print("Must be 6, 12 or 20")
            type_of_die = int(input("choose a die (6, 12, 20) "))
    while True:
        match type_of_die:
            case 6:
                roll = random.randint(1,6)
                print(f"you chose 6 and rolled {roll}")
            case 12:
                roll = random.randint(1,12)
                print(f"you chose 12 and rolled {roll}")
            case 20:
                roll = random.randint(1,20)
                print(f"you chose 20 and rolled {roll}")
        
        roll_again = input("roll again with the same die y/n? ")
        if roll_again != "y":
            break
    change_die = input("Change die y/n? " )
    if change_die != "y":
        break

print("thanks for playing")