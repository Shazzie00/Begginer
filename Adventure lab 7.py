done = False

player = input("What is your name ? ")
game = input("Would you like to play a game? \n(YES) OR (NO)\nAnswer: ")

# Introduction to game
if game.lower() == "yes" or game.lower() == "y":
    print("welcome war house, your goal of the game is to escape the house safely, but beware of "
          "\npossible dangers that may occur.In each room, there will be a series of challenges. You now have a "
          "\nbackpack with things to help u survive but also escape. There are 8 rooms in this house.You will "
          "\nhave a chance to explore the rooms or to move on but be careful not all the room are safe.")

else:
    done = True
    print(" Oh no goodbye", player, ".")

health = 100
# order is: current Room , north, east, south, or west
room_list = []
homebase = ["Home base.\n There is a room to the east and south.", None, 5, 1, None, "Homebase"]
room_list.append(homebase)
outpost = ["Outpost.\nThere is a room to your north, east and south", 0, 4, 2, None, "Outpost"]
room_list.append(outpost)
arsenal = ["Arsenal.\nThere is a room to the north and east.", 1, 3, None, None, "Arsenal"]
room_list.append(arsenal)
depot = ["Depot. \nThere is a room to the north, east and west.", 4, 8, None, 2, "Depot"]
room_list.append(depot)
barracks = ["Barracks.\n You can go any direction.", 5, 7, 3, 1, "Barracks"]
room_list.append(barracks)
Mineroom = ["Mineroom.Be-careful were you step or it might be your last", None, None, None, 0, "Mine-room"]
room_list.append(Mineroom)
end = ["Remember to explore each room", None, None, None, None, "FinalRoom"]
room_list.append(end)
whitehall = ["WhiteHall.There is a room to the north, east and west", 6, 8, None, 4, "WhiteHall"]
room_list.append(whitehall)
landmineroom = ["Land Mine room (8). Be-careful were you tread or it might be your last", None, None, None, 3, "L.Mine"
                                                                                                               "-room"]
room_list.append(landmineroom)

# Track current room
current_room = 0

next_room = room_list[current_room][1]
# users current position


# list of inventory
backpack_list = ["water", "water", "water", "apple", "bandaid", "bandaid"]

while done == False:
    print('\n\t\t\t'"Location:", (room_list[current_room][5]))
    print("\nA.Check backpack \nB.Explore Room \nC.Move \nD.Quit ")
    print("Health:", health)
    user_input = input("\nChoice: ")

    # Quit option
    if user_input.lower() == "d":
        print('Game over :(')

        done = True

    # Backpack and health status
    if user_input.lower() == "a":
        print("Items in backpack :", backpack_list)
        print("health:", health)
        print("A. Drink Water \n B. Use Bandaid \n C. Ignore")
        player_input = input("\nChoice: ")

        if player_input == "a":
            print("Health increased by 5")
            health += 5
            backpack_list.remove('water')

        elif player_input == "b":
            print("heal")
            health += 5
            backpack_list.remove("bandaid")

    # Room Exploration sector
    if user_input.lower() == "c":
        print("You are in room:", (room_list[current_room][0]))
        print(">>(N)NORTH \n>>(E)EAST \n>>(S)SOUTH \n>>(W)WEST")
        player_input = input("Direction: ")

        if player_input.lower() == "north" or player_input.lower() == "n":
            next_room = room_list[current_room][1]
            health -= 5
            if next_room == None:
                print("You can't go that way")

            else:
                current_room = next_room

        if player_input.lower() == "east" or player_input.lower() == "e":
            next_room = room_list[current_room][2]
            health -= 5
            if next_room == None:
                print("You can't go that way")
            else:
                current_room = next_room

        if player_input.lower() == "south" or player_input.lower() == "s":
            next_room = room_list[current_room][3]
            health -= 5
            if next_room == None:
                print("You can't go that way")
            else:
                current_room = next_room

        if player_input.lower() == "west" or player_input.lower() == "w":
            next_room = room_list[current_room][4]
            health -= 5
            if next_room == None:
                print("You can't go that way")
            else:
                current_room = next_room

    # exploration function

    if user_input.lower() == "b":

        if current_room == 1:
            print("As you were exploring the room you came across a shiny object as you moved closer you accidentally "
                  "scraped your hand on a sharp object nearby.")
            print("A. CheckBackpack for bandaid \nB. Ignore it")
            player_input = input("Decision: ")

            if player_input.lower() == "a":
                backpack_list.remove('bandaid')
                health -= 10
                print("You found the bandaid, your health decreased by 10.")

            elif player_input.lower() == "b":
                print(player, "ignored injury")
                health -= 25
                print("Your health decred by 25")

        if current_room == 0:
            print("Your at home base")
            print("A. Review rules \n B.Check Backpack")

            if user_input.lower() == "a":
                print("welcome war house, your goal of the game is to escape the house safely, but BEWARE "
                      "of possible dangers that may occur. In each room, there will be a series of challenges. "
                      "You now have a backpack with things to help you SURVIVE but also escape. There are 8 rooms in "
                      "this house.You will have a chance to EXPLORE the rooms or to move on but be careful not all the"
                      " room are safe.")

            elif user_input.lower() == "b":
                print("Items in backpack :", backpack_list)
                print("Health:", health)

        if current_room == 5:
            print("You just entered a room full of land mines as you explored the room u stepped on a land mine"
                  " oh sorry u just exploded into small bits")
            print("GAME OVER")
            done = True

        if current_room == 8:
            print("You just entered a room full of land mines as you explored the room u stepped on a land mine"
                  " oh sorry you exploded into small bits")
            print("GAME OVER")
            done = True

        if current_room == 2:
            print("you are now in the arsenal room but there is nothing useful in there")

        if current_room == 4:
            print("You are explored  the barracks you find food and medicine")
            print("A.Put things in backpack \nB. Ignore them")
            player_input = input("Decision: ")

            if player_input.lower() == "a":
                print("Items added in backpack")
                backpack_list.append('apple')
                backpack_list.append('medicine')

            elif player_input.lower() == "b":
                print(player, "ignored resources")

        if current_room == 3:
            print("You just walked into the depot room you see a shine red key you are then suddenly attacked by red "
                  "ants")
            print("A.checkBackpack for medicine \nB. Ignore ")
            player_input = input("Decision: ")

            if player_input.lower() == "a":
                if 'medicine' not in backpack_list:
                    print("\nYou need to explore the room to find a medicine quickly, you dont have much energy left")
                    health -= 10

                if 'medicine' in backpack_list:
                    backpack_list.remove('medicine')
                    print("Phew, you are saved you health decreased by 5")
                    health -= 5

                elif player_input.lower() == "b":
                    health -= 15
                    print(player, "ignored")

        if current_room == 7:
            print("You are now in white hall, there are beds, food, water, and first aid kits in this room")
            print("A. Sleep B. Eat C. Heal D. Ignore")
            player_input = input("Decision: ")

            if player_input.lower() == "a":
                health += 15
                print("Your health increased by 15")
            elif player_input.lower() == "b":
                health += 25
                print("Your health was increased by 25")
            elif player_input.lower() == "c":
                health += 40
                print("Good choice your health is now increased by 40")
            elif player_input.lower() == "d":
                print("It is your choice but be careful")

        if current_room == 6:
            print("As you explored the room you found a window which you could crawl our from."
                  "Congratulation you made it out alive")
            print(player, "goodbye")
            done = True

    # health

    if health <= 50:
        print("Warning, Health is low, Check backpack for something to increase your health")
    if health <= 15:
        print("You died from Exhaustion")
        done = True
