from guizero import App, PushButton, Text, Box, TextBox
from classCaptains import class_captains
cc_list = []

app = App(title="Voting")
num = 0

def candidate():
    global num
    num += 1
    message.value = str(input_box_1) + " has " + str(num) + " votes"

captain_box = Box(app, width="fill")
Text(captain_box, text="Captain 1: ")
input_box_1 = TextBox(app, text=" ")

button = PushButton(app, text="Vote for class captain", command=candidate)
message = Text(app, text=" ")

app.display()


