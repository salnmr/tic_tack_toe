# tic tack toe
import pprint, random, sys, math

board = {"a1": " ", "a2": " ", "a3": " ", "b1": " ", "b2": " ", "b3": " ", "c1": " ", "c2": " ", "c3": " "}

winning = {"win1": {"a1": True, "a2": True, "a3": True}, "win2": {"b1": True, "b2": True, "b3": True},
           "win3": {"c1": True, "c2": True, "c3": True}, "win4": {"a1": True, "b1": True, "c1": True},
           "win5": {"a2": True, "b2": True, "c2": True}, "win6": {"a3": True, "b3": True, "c3": True},
           "win7": {"a1": True, "b2": True, "c3": True}, "win8": {"c1": True, "b2": True, "a3": True}}

state = {"first_round": True, "quit": False, "rounds": 0, "rounds_played": 0, "both_answered": False, "winner": False}
players = {"player_one": {"name": "", "score": 0, "won_round": False, "answered": 0, "order": 0},
           "player_two": {"name": "", "score": 0, "won_round": False, "answered": 0, "order": 0}}

def intro():
    print("tbd \n")

def player():
    while state["both_answered"] != True:
        while players["player_one"]["answered"] != 1:
            player = input(f"What is the name for player one?: ").strip()
            if bool(player) is True:
                player_check_num = player.isdigit()
                player_check_letter = player.isalpha()
                if player_check_num is not True and player_check_letter is True:
                    players["player_one"]["name"] = player
                    players["player_one"]["answered"] = 1
                else:
                    print("WARNING: Please make sure you dont have any numbers or special characters within your name. Try again.\n")
            else:
                print("WARNING: You need to enter something!\n")

        while players["player_two"]["answered"] != 1:
            player = input(f"What is the name for player two?: ").strip()
            if bool(player) is True:
                player_check_num = player.isdigit()
                player_check_letter = player.isalpha()
                if player_check_num is not True and player_check_letter is True:
                    players["player_two"]["name"] = player
                    players["player_two"]["answered"] = 1
                else:
                    print("WARNING: Please make sure you dont have any numbers or special characters within your name. Try again.\n")
            else:
                print("WARNING: You need to enter something!\n")
        state["both_answered"] = False
        return None

def order():
    # who will go first? or randomise?
    print(f"""Who will go first? 
    1). Player One ({players['player_one']['name']}) 
    2). Player Two({players['player_two']['name']}) """)

    while state["both_answered"] != True:
        try:
            player_order = input("Choose type either 1 or 2: ").strip()
            player_order = int(player_order)
            if player_order == 1 or player_order == 2:
                if player_order == 1:
                    players["player_one"]["order"] = 1
                    state["both_answered"] = True
                else:
                    players["player_two"]["order"] = 1
                    state["both_answered"] = True
            else:
                print("WARNING: Thats not a 1 or a 2!\n")
        except ValueError:
            print("WARNING: Cant be blank. No special characters. And it has to be a 1 or 2! Try again.\n")


def define_game():
    # while not players["player_one"]["name"] and not players["player_two"]["name"]:
    player()
    print()
    order()
    print()

    state["first_round"] = False
    return

def game():
    print("game")

# main loop
while state["winner"] != True:
    if state["first_round"] == True:
        define_game()
    else:
        # if you would like to quit please
        game()
        print("in loop")
        sys.exit()