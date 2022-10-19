fresh_board = {
"a3": {"space": "___|", "taken": False}, "b3": {"space": "___", "taken": False}, "c3": {"space": "|___", "taken": False},
"a2": {"space": "___|", "taken": False}, "b2": {"space": "___", "taken": False}, "c2": {"space": "|___", "taken": False},
"a1": {"space": "   |", "taken": False}, "b1": {"space": "   ", "taken": False}, "c1": {"space": "|   ", "taken": False}}

working_board = {
"a3": {"space": "___|", "taken": False}, "b3": {"space": "___", "taken": False}, "c3": {"space": "|___", "taken": False},
"a2": {"space": "___|", "taken": False}, "b2": {"space": "___", "taken": False}, "c2": {"space": "|___", "taken": False},
"a1": {"space": "   |", "taken": False}, "b1": {"space": "   ", "taken": False}, "c1": {"space": "|   ", "taken": False}}

holding = ""
count = 0
for space in working_board:
    holding += working_board[space]["space"]
    count += 1
    if count == 3:
        print(holding)
        count = 0
        holding = ""





# def check_player_answer():
#     player = input(f"Answer: ").strip().lower()
#     player_num_check = player.isdigit()
#     player_letter_check = player.isalpha()
#     if player_letter_check == True and player_num_check == False:
#         if player == "quit" or player == "q":
#             state["quit"] = True
#         elif player == "x" or player == "o":
#             square = input(f"Square: ").strip().lower()
#             if square in working_board.keys():
#                 print("checking... \n")
#                 # check to see if the square is empty
#                 if working_board[square]['taken'] == False:
#                     players_turn_to_answer(player, square)
#                 else:
#                     print("WARNING: Not Empty!")
#             else:
#                 # not a vaild square. could be full but not vaild. IE x1 or g3.
#
#         # pass player answer here
#         else:
#             print("WARNING: Thats not X or O... \n")
#     else:
#         print("WARNING:Jesus Christ.... we've done this for like 3 times now. I need the correct Character! X or O \n")


#    ****************************** CHECK THEM SEPTRRATELY******************************
#  Check selction and also square
# then passit through