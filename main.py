# tic tack toe
import pprint, random, sys, math

fresh_board = {
    "a3": {"space": "___|", "taken": False}, "b3": {"space": "___", "taken": False},
    "c3": {"space": "|___", "taken": False},
    "a2": {"space": "___|", "taken": False}, "b2": {"space": "___", "taken": False},
    "c2": {"space": "|___", "taken": False},
    "a1": {"space": "   |", "taken": False}, "b1": {"space": "   ", "taken": False},
    "c1": {"space": "|   ", "taken": False}}

working_board = {
    "a3": {"space": "___|", "taken": False}, "b3": {"space": "___", "taken": False},
    "c3": {"space": "|___", "taken": False},
    "a2": {"space": "___|", "taken": False}, "b2": {"space": "___", "taken": False},
    "c2": {"space": "|___", "taken": False},
    "a1": {"space": "   |", "taken": False}, "b1": {"space": "   ", "taken": False},
    "c1": {"space": "|   ", "taken": False}}

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
            print(f"2). We will being with Player One")
        else:
            print(f"2). We will being with Player Two")
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
            player_order = input("Please choose either 1 or 2: ").strip()
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
            print("How many rounds would you like to play? Remember it has to be an odd number and greater then 3 (or equal to)!")
            rounds_amount = int(input("Amount of Rounds: ").strip())

            if rounds_amount >= 3 and (rounds_amount % 2) == 1:
                state["rounds"] = rounds_amount
            else:
                print("WARNING: Thats not correct! \n")
        except ValueError:
            print("WARNING: Cant be blank. No special characters. And it has to be a Number! Try again. \n")

    print()
    return None

def draw_board():
    if players["player_one"]["order"] == 1:
        print("Turn: Player One - x")
    else:
        print("Turn: Player Two - o")

    holding = ""
    count = 0
    for space in working_board:
        holding += working_board[space]["space"]
        count += 1
        if count == 3:
            print(holding)
            count = 0
            holding = ""


def check_player_answer():
    player = input(f"Answer: ").strip().lower()
    player_num_check = player.isdigit()
    player_letter_check = player.isalpha()
    if player_letter_check == True and player_num_check == False:
        if player == "quit" or player == "q":
            state["quit"] = True
        elif player == "x" or player == "o":
            players_turn_to_answer(player)
        # pass player answer here
        else:
            print("WARNING: Thats not X or O... \n")
    else:
        print("WARNING:Jesus Christ.... we've done this for like 3 times now. I need the correct Character! X or O \n")

def players_turn_to_answer(player_input):
# this will check which players turn it is
    # player one goes
    if players['player_one']['order'] == 1:
        # player one = x
        if player_input == "x":
            players["player_two"]["order"] = 1
            players["player_one"]["order"] = 0
            write_to_board(player_input, "player_one", square="")
        else:
            print(f"Wrong! You are not {player_input}! You are X \n")
    else:
        # player 2 goes
        if player_input == "o":
            # draw
            players["player_two"]["order"] = 0
            players["player_one"]["order"] = 1
            write_to_board(player_input, "player_two")
        else:
            print(f"Wrong! You are not {player_input}! You are O \n")

def write_to_board(player_input, player, square=""):
    if player == "player_one":
        pass
    # player two
    else:
        pass



# Error check and make sure its a vaild answer
# FOR THE SPECIDIFC PLAYER ALSO!

# change baord

def check_win():
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
        for count in range(state["rounds"]):
            while players["player_one"]["won_round"] != True or players["player_two"]["won_round"] != True:
                while state["quit"] != True:
                    draw_board()
                    check_player_answer()
                    check_win()
                sys.exit()
