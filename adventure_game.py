import time
import random
players1 = (["Lebron James", "Anthony Davis", "Dwight Howard"])
players2 = (["Steph Curry", "Kyrie Irving", "Damian Lillard"])


def print_pause(x):
    print(x)
    time.sleep(2)


def intro():
    print_pause("Welcome to first day of NBA camp")
    print_pause("You've made it really far, however you have one last step"
                " to make it into the NBA")
    print_pause("You have to prove yourself by "
                "defeating one of the best 1v1 !")


def first_door():
    print_pause(random.choice(players1) + " has appeared!")
    action1 = input("Shoot a three or go for a layup?\n"
                    "(1) for three or (2) for layup\n")
    if action1 == "1":
        print_pause("Congratulations! You made the three!\n"
                    "Welcome to the NBA!!")

    elif action1 == "2":
        print_pause("When you went for the layup you got blocked!\n"
                    "You lose!")

    else:
        print_pause("I don't understand your reponse")
        first_door()


def second_door():
    print_pause(random.choice(players2) + " has appeared!")
    action2 = input("Safe jumpshot or go for the dunk?\n"
                    "(1) for jumpshot or (2) for dunk\n")
    if action2 == "1":
        print_pause("Oh no! You missed!\n"
                    "You lose!")

    elif action2 == "2":
        print_pause("Congratulations, you made the dunk and scored!\n"
                    "Welcome to the NBA!!")

    else:
        print_pause("Sorry I don't understand your response.")
        second_door()


def beginning():
    print_pause("You find two doors with "
                "legend NBA players behind each.")
    print_pause("Knock on the first door or the second one?")
    door = input("Press '1' for the first door"
                 "or '2' to go the second door.\n")
    if door == "1":
        first_door()
    elif door == "2":
        second_door()
    else:
        print_pause("Sorry I don't understand your response")
        beginning()


def play_again():
    print_pause("Would you like to play again?")
    last_response = input("(y/n)\n").lower()
    if last_response == "y":
        play_game()
    elif last_response == "n":
        print_pause("Game over!")
        print_pause("Thanks for playing.")
    else:
        print_pause("I don't understand your response")
        play_again()


def play_game():
    intro()
    beginning()
    play_again()


play_game()
