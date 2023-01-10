from guizero import App, PushButton, Text, Box, TextBox
from data import cc_list

def candidate():
    global num
    app = App(title="Voting")
    num = 0

    #try and except to put however many things i need.

    input_box_1 = cc_list[0]
    print(input_box_1)
    input_box_2 = cc_list[1]
    print(input_box_2)
    input_box_3 = cc_list[2]
    print(input_box_3)
    input_box_4 = cc_list[3]
    print(input_box_4)

    message1 = str(input_box_1) + " has " + str(num) + " votes"
    print(message1)
    message2 = str(input_box_2) + " has " + str(num) + " votes"
    print(message2)
    message3 = str(input_box_3) + " has " + str(num) + " votes"
    print(message3)
    message4 = str(input_box_4) + " has " + str(num) + " votes"
    print(message4)

    vote_box_1 = Text(candidate, text=input_box_1, align="left")
    vote_box_2 = Text(candidate, text=input_box_2, align="left")
    vote_box_3 = Text(candidate, text=input_box_3, align="left")
    vote_box_4 = Text(candidate, text=input_box_4, align="left")

    captain_box = Box(app, width="fill")
    Text(captain_box, text="Captain 1: ")

    button = PushButton(app, text="Vote for class captain", command=candidate)
    message = Text(app, text=" ")


