import random

done = False

player = input("What is your name ? ")
game = input("Would you like to play a game? \n(YES) OR (NO)\nAnswer: ")

# Introduction to game
if game.lower() == "yes" or game.lower() == "y":
    print("Welcome", player, " to the school run game")
    print("\nYou are running late to school because you overslept and missed the bus. Your parents already left"
          "for work,and you do not have a valid drivers’ licence.\nYour teacher Mr. Birrell threatened to exclude you"
          " from an upcoming field trip to Sky Park if you are late one more time.\nYou urgently hop on"
          "your bike and make your way to school without eating breakfast.\n")

    print("School starts at 8:45 AM the time is 8:10 AM\nDr. Martin LeBoldus High School is 8 km away from "
          "your house.\nEnergy – 100\nTime – 30")

else:
    done = True
    print(" Oh no goodbye", player, ".")

energy = 100
distance = 8
time = 30

while done == False:
    # Choices for user is given
    print("\nA. Drink Water\nB. Pedal faster \nC. Pedal normal pace \nD. Slow Pedal"
          "\nQ. Hop off the bike and accept defeat (Loser)")
    user_input = input("\n Answer: ")
    # Quit option
    if user_input.lower() == "q":
        done = True
        print('Game over loser :(')

    # Drink variation/ thirst

    elif user_input.lower() == "a":
        time -= 5
        energy += 5
        print(" Energy level is at", energy)
        print("You have ", distance, " km left ")
        print("You have", time, "minutes left")

    # Option B Pedal faster option

    elif user_input.lower() == "b":
        pedal_faster = float("{:.1f}".format(random.random() * 0.8 + 1.5))
        distance = distance - pedal_faster
        energy -= 35
        time -= 6
        print("You have ", distance, " left km ")
        print("energy level ", energy)
        print("You have", time, "minutes left")

        # Option C normal pace option

    elif user_input.lower() == "c":
        pedal_normal = float("{:.1f}".format(random.random() * 0.4 + 0.7))
        distance = distance - pedal_normal
        energy -= 25
        time -= 7
        print("You have", distance, "km left")
        print("You have", time, "minutes left")
        print("energy level ", energy)

        # option D slow pace option

    elif user_input.lower() == "d":
        pedal_slow = float("{:.1f}".format(random.random() * 0.1 + 0.3))
        distance = distance - pedal_slow
        energy -= 20
        time -= 8
        print("You have", distance, "km left")
        print("You have", time, "minutes left")
        print("energy level ", energy)

        # Random Section 2 - Shortcut option-, random is the distance of km that is randomized subtracted by normal
        # distance

    if distance <= 4:
        game = input("\n[You found a shortcut would you like to take it ?]\nA-Take shortcut "
                     "\nB-Not take shortcut\nAnswer: ")
        if game.upper() == "A":
            print("You found a shortcut")
            time -= 3
            distance -= random.randrange(1, 5)
            print(" distance left is", distance, "km")
            print("You have", time, "minutes left")
            print("energy level ", energy)
        elif game.upper() == "B":
            print(" you have", distance, "left")
            print("You have", time, "minutes left")
            print("energy level ", energy)

    # Warning display

    elif time <= 8:
        print(" [ Time is running out !!! ] ")

    elif energy <= 20:
        print("[ Energy level is low !! ]")

    elif energy >= 115:
        print("[ Time is running out !!] ")

    # If players energy and time surpasses the given  number they either loose or win

    if time <= 1:
        done = True
        print(" oh no, You did not make it to school time ran out :( ")

    elif distance <= 0.9:
        done = True
        print("Congratulation", player, " made it to school")

    elif energy <= 0:
        done = True
        print("You passed out, Game over")

        # signs of reducing pace
