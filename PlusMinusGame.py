
prompt_1 = "Please enter the board size\n"
prompt_2 = "Please enter how many squares you want to place\n"
prompt_3 = "Please enter the coordinates of a square you want to place\n"
prompt_4 = "Please enter a target square coordinate, or enter exit to exit\n"
prompt_5 = "Congratulations, you won!"
prompt_6 = "Thanks for playing."
error_message_1 = "Improper board size"
error_message_2 = "Improper amount of squares"
error_message_3 = "Incorrect input format for square coordinates"
error_message_4 = "Improper square coordinates"
error_message_5 = "Sign already placed to square"



def change_sign(x):
    if x == "+":
        return "-"
    if x == "-":
        return "+"
coordinates = dict()
board_size = int(input(prompt_1))
while board_size < 5 or board_size > 9:
    print(error_message_1)
    board_size = int(input(prompt_1))
for row in range(1, board_size+1): #building the board
    for col in range(1, board_size+1):
        coordinates[(row, col)] = "-"
square_amount = int(input(prompt_2))
while square_amount < 1 or square_amount > board_size**2:
    print(error_message_2)
    square_amount = int(input(prompt_2))
#Placement phase
def board_print(dic):
    global board_size
    print(" " * 2, end="")
    for l in range(1, board_size + 1):
        if l != board_size:
            print(l, end=" ")
        else:
            print(l)
    for m in range(1, board_size + 1):
        print(m, end=" ")
        for n in range(1, board_size + 1):
            if n != board_size:
                print(dic[(m, n)], end=" ")
            else:
                print(dic[(m, n)])
counter=0
while counter < square_amount:
    false_coords = False
    placement = input(prompt_3).split()
    if placement == [] or len(placement) < 2:
        print(error_message_3)
        continue
    for coords in placement[0:2]: #since only first 2 elements matter
        try:
            int(coords)
            if int(coords) > board_size or int(coords) < 1: #invalid number case
                print(error_message_4)
                false_coords = True
                break
        except:
            print(error_message_3) #invalid format case
            false_coords = True
            break
    if false_coords:
        continue
    if coordinates[(int(placement[0]), int(placement[1]))] == "+": #already placed
        print(error_message_5)
        continue
    coordinates[(int(placement[0]), int(placement[1]))]="+"
    counter += 1
    board_print(coordinates)
# X phase
while True:
    minuses = 0
    false_coords = False
    target = input(prompt_4)
    if target.lower().strip() == "exit":
        print(prompt_6)
        break
    targlst = target.split()
    if targlst == [] or len(targlst) < 2:
        print(error_message_3)
        continue
    for el in targlst[0:2]:
        try:
            int(el)
            if int(el) > board_size or int(el) < 1:
                print(error_message_4)
                false_coords = True
                break
        except:
            print(error_message_3)
            false_coords = True
            break
    if false_coords:
        continue
    roww = int(targlst[0])
    column = int(targlst[1])
    coordinates[(roww, column)] = change_sign(coordinates[(roww, column)])
    if not coordinates.get((roww+1, column-1)) == None: #south west
        coordinates[(roww+1, column-1)] = change_sign(coordinates[(roww+1, column-1)])
    if not coordinates.get((roww+1, column+1)) == None: #south east
        coordinates[(roww+1,column+1)] = change_sign(coordinates[(roww+1, column+1)])
    if not coordinates.get((roww-1, column+1)) == None: #north east
        coordinates[(roww-1,column+1)] = change_sign(coordinates[(roww-1, column+1)])
    if not coordinates.get((roww-1, column-1)) == None: #north west
        coordinates[(roww-1, column-1)] = change_sign(coordinates[(roww-1, column-1)])
    board_print(coordinates)
    for signs in coordinates.values(): #checking victory
        if signs == "-":
            minuses += 1
        else:
            break
    if minuses == board_size**2:
        print(prompt_5)
        print(prompt_6)
        break
