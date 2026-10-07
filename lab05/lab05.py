matrix = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

players = ["X","O"]

winner = ""

current_player = ""

number_of_turns = 0

enter = "Press [Enter] to continue"

while(number_of_turns <= 8) and (winner == ""):
    
    if (current_player == "") or (current_player == "O"):
        current_player = players[0]

    elif (current_player == "X"):
        current_player = players[1]
    
    print(f"TIC-TAC-TOE,\n{matrix[0]}\n{matrix[1]}\n{matrix[2]}\nIt is {current_player}'s turn")
    
    row_answer = input("Enter Row (1-3):")
    column_answer = input("Enter Column (1-3):")

    if (row_answer != "1") and (row_answer != "2") and (row_answer != "3"):
        print("Input a number 1-3 for your row next time...\nTry Again")
        input(enter)
        if (current_player == "") or (current_player == "O"):
            current_player = players[0]

        elif (current_player == "X"):
            current_player = players[1]
        continue

    if (column_answer != "1") and (column_answer != "2") and (column_answer != "3"):
        print("Input a number 1-3 for your column next time...\nTry Again")
        input(enter)
        if (current_player == "") or (current_player == "O"):
            current_player = players[0]

        elif (current_player == "X"):
            current_player = players[1]
        continue

    if ((matrix[int(row_answer) - 1])[int(column_answer) - 1] != "-"):
        print("You input a move that already happened\nTry again")
        input(enter)
        if (current_player == "") or (current_player == "O"):
            current_player = players[0]

        elif (current_player == "X"):
            current_player = players[1]
        
    (matrix[int(row_answer) - 1])[int(column_answer) - 1] = (current_player)

    for column_answer in range(3):
        if current_player == (matrix[0])[column_answer] == (matrix[1])[column_answer] == (matrix[2])[column_answer]:
            winner = current_player
            break

    for row_answer in range(3):
        if current_player == (matrix[row_answer])[0] == (matrix[row_answer])[1] == (matrix[row_answer])[2]:
            winner = current_player
            break
    
    if current_player == (matrix[0])[0] == (matrix[1])[1] == (matrix[2])[2]:
        winner = current_player
        break

    if current_player == (matrix[2])[0] == (matrix[1])[1] == (matrix[0])[2]:
        winner = current_player
        break

    number_of_turns += 1
    continue

print(f"TIC-TAC-TOE,\n{matrix[0]}\n{matrix[1]}\n{matrix[2]}")
if winner == "":
        print("It's a TIE!")
elif winner != "":
    print(f"Game Over!\n{winner} Won!\nThanks for Playing!")