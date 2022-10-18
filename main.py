# tic tack toe
import pprint, random, sys

board = {"a1": " ", "a2": " ", "a3": " ", "b1": " ", "b2": " ", "b3": " ", "c1": " ", "c2": " ", "c3": " "}

winning = {"win1": {"a1": True, "a2": True, "a3": True}, "win2": {"b1": True, "b2": True, "b3": True},
           "win3": {"c1": True, "c2": True, "c3": True}, "win4": {"a1": True, "b1": True, "c1": True},
           "win5": {"a2": True, "b2": True, "c2": True}, "win6": {"a3": True, "b3": True, "c3": True},
           "win7": {"a1": True, "b2": True, "c3": True}, "win8": {"c1": True, "b2": True, "a3": True}}

state = {"first_round": True, "quit": False, "rounds": 0, "rounds_played": 0}
player_one = {"name": "", "score": 0, "won_round": False, "char": ""}
player_two = {"name": "", "score": 0, "won_round": False, "char": ""}

def intro():
    print("tbd \n")

def define_game():
# error handle try/expect
    # get names
    player = input("What is the name for player one?: ")
    player_one["name"] = player
    player = input("What is the name for player two?: ")
    player_two["name"] = player

    # best of how many?
    rounds = input("How many rounds would you like to play?: ")
    state["rounds"] = rounds

    # who will go first? or randomise?

    # pick special char. x or o. or z and y. Etc.


# main loop
while True:
    if state["first_round"] == True:
        pass
    else:
        state["first_round"] = False


