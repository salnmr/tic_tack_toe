# tic tack toe
import pprint, random, sys, math

board = {"a1": False, "a2": False, "a3": False, "b1": False, "b2": False,
         "b3": False, "c1": False, "c2": False, "c3": False}

winning = {"win1": {"a1": True, "a2": True, "a3": True}, "win2": {"b1": True, "b2": True, "b3": True},
           "win3": {"c1": True, "c2": True, "c3": True}, "win4": {"a1": True, "b1": True, "c1": True},
           "win5": {"a2": True, "b2": True, "c2": True}, "win6": {"a3": True, "b3": True, "c3": True},
           "win7": {"a1": True, "b2": True, "c3": True}, "win8": {"c1": True, "b2": True, "a3": True}}

state = {"first_round": True, "quit": False, "rounds": 0, "rounds_played": 0, "both_answered": False, "winner": False}
players = {"player_one": {"name": "", "score": 0, "won_round": False, "answered": 0, "order": 0},
           "player_two": {"name": "", "score": 0, "won_round": False, "answered": 0, "order": 0}}

def text_block(text):
    if text == "intro":
        print("""
                █████   ███   █████          ████                                                    █████                                                 
                ░░███   ░███  ░░███          ░░███                                                   ░░███                                                  
                 ░███   ░███   ░███   ██████  ░███  █████ █████  ██████  █████████████    ██████     ███████    ██████                                      
                 ░███   ░███   ░███  ███░░███ ░███ ░░███ ░░███  ███░░███░░███░░███░░███  ███░░███   ░░░███░    ███░░███                                     
                 ░░███  █████  ███  ░███████  ░███  ░░░█████░  ░███ ░███ ░███ ░███ ░███ ░███████      ░███    ░███ ░███                                     
                  ░░░█████░█████░   ░███░░░   ░███   ███░░░███ ░███ ░███ ░███ ░███ ░███ ░███░░░       ░███ ███░███ ░███                                     
                    ░░███ ░░███     ░░██████  █████ █████ █████░░██████  █████░███ █████░░██████      ░░█████ ░░██████                                      
                     ░░░   ░░░       ░░░░░░  ░░░░░ ░░░░░ ░░░░░  ░░░░░░  ░░░░░ ░░░ ░░░░░  ░░░░░░        ░░░░░   ░░░░░░                                       
                                                                                                                                            
                                                                                                                                            
                                                                                                                                            
 ███████████ █████   █████████  █████   ████    ███████████   █████████   █████   ████                  ███████████    ███████    ██████████
░█░░░███░░░█░░███   ███░░░░░███░░███   ███░    ░█░░░███░░░█  ███░░░░░███ ░░███   ███░                  ░█░░░███░░░█  ███░░░░░███ ░░███░░░░░█
░   ░███  ░  ░███  ███     ░░░  ░███  ███      ░   ░███  ░  ░███    ░███  ░███  ███                    ░   ░███  ░  ███     ░░███ ░███  █ ░ 
    ░███     ░███ ░███          ░███████           ░███     ░███████████  ░███████        ██████████       ░███    ░███      ░███ ░██████   
    ░███     ░███ ░███          ░███░░███          ░███     ░███░░░░░███  ░███░░███      ░░░░░░░░░░        ░███    ░███      ░███ ░███░░█   
    ░███     ░███ ░░███     ███ ░███ ░░███         ░███     ░███    ░███  ░███ ░░███                       ░███    ░░███     ███  ░███ ░   █
    █████    █████ ░░█████████  █████ ░░████       █████    █████   █████ █████ ░░████                     █████    ░░░███████░   ██████████
            """)
        print()
        return None

    elif text == "rules":
        print("""
                                        ███████████   █████  █████ █████       ██████████  █████████ 
                                        ░░███░░░░░███ ░░███  ░░███ ░░███       ░░███░░░░░█ ███░░░░░███
                                         ░███    ░███  ░███   ░███  ░███        ░███  █ ░ ░███    ░░░ 
                                         ░██████████   ░███   ░███  ░███        ░██████   ░░█████████ 
                                         ░███░░░░░███  ░███   ░███  ░███        ░███░░█    ░░░░░░░░███
                                         ░███    ░███  ░███   ░███  ░███      █ ░███ ░   █ ███    ░███
                                         █████   █████ ░░████████   ███████████ ██████████░░█████████ 
                                        ░░░░░   ░░░░░   ░░░░░░░░   ░░░░░░░░░░░ ░░░░░░░░░░  ░░░░░░░░░ 
            """)
        print("1). If you would like to quit type, (Q)uit")
        if players["player_one"]["order"] == 1:
            print(f"2). we will being with Player One")
        else:
            print(f"2). we will being with Player Two")
        print()
        return None

def create_players():
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
        print()
        return None

def player_order():
    # pick who to go first
    print(f"""Who will go first? 
    1). Player One ({players['player_one']['name']}) 
    2). Player Two ({players['player_two']['name']}) """)

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

    state["both_answered"] = False
    print()
    return None

def get_turn_amount():
    # ask how many rounds.
    while state["rounds"] == 0:
        try:
            print("How many rounds would you have to play? Remember it has to be an odd number!")
            rounds_amount = int(input("Amount of Rounds: ").strip())

            if rounds_amount >= 3 and (rounds_amount % 2) == 1:
                    state["rounds"] = rounds_amount
            else:
                print("WARNING: Thats not correct!\n")
        except ValueError:
            print("WARNING: Cant be blank. No special characters. And it has to be a Number! Try again.\n")

    print()
    return None

def draw_board():
    pass

# main loop
while state["winner"] != True:
    if state["first_round"] == True:
        text_block("intro")
        create_players()
        player_order()
        get_turn_amount()
        text_block("rules")
        state["first_round"] = False
    else:
        while state["quit"] != True:
            draw_board()
            # start here. all checking of user data is done. Next I have to create the check each imput and then
            # draw the board
            #
            # I might want to add the character check used within each square
            sys.exit()
