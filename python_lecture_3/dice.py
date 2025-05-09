##my_list = [1, 2, 3, 4, 5]
##for item in my_list:
##    print(item)

type_of_die = int(input("choose a die (6,12,20) "))

while True:
    if type_of_die not in [6, 12, 20]:
        print("Must be 6, 12 or 20")
match type_of_die:
    case 6:
        print("you chose 6")
    case 12:
        print("you chose 12")
    case 20:
        print("you chose 20")
