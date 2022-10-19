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