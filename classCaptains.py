from guizero import Box, Text, TextBox, PushButton, Window
from data import cc_list

def class_captains(app):

    #Instead of using an app just turned it to a window.
    win_class_captain = Window(app, title="Menu", layout="grid", bg="#034C3C", height="1400", width="1400")

    def save_data(box_no):
        if box_no == 1:
            cc_list.append(input_box_1.value)

        elif box_no == 2:
            cc_list.append(input_box_2.value)

        elif box_no == 3:
            cc_list.append(input_box_3.value)

        elif box_no == 4:
            cc_list.append(input_box_4.value)

        print(cc_list)

    #this is the code for the title box
    spacer = Box(win_class_captain, width=20, height=20, grid=[2,0])
    title_box = Box(win_class_captain, width=200, height=20, grid=[3,0])
    Text(title_box, text="Enter the names of the class captains.", bg="#E2D4B7")
    #-----

    #code for captain 1 box
    spacer = Box(win_class_captain, width=70, height=30, grid=[2,1])
    captain_box1 = Box(win_class_captain, width="fill", grid=[1,1])
    Text(captain_box1, text="Captain 1: ")
    input_box_1 = TextBox(win_class_captain, text=" ", grid=[2,1])
    captain_box1.bg = "#E2D4B7"
    button1 = PushButton(win_class_captain, text="Save Name", command=save_data, grid=[3,1], args=[1])

    #code for captain 2
    spacer = Box(win_class_captain, width=70, height=150, grid=[2,2])
    captain_box2 = Box(win_class_captain, width="fill", grid=[1,2])
    Text(captain_box2, text="Captain 2: ")
    input_box_2 = TextBox(win_class_captain, text=" ", grid=[2,2])
    captain_box2.bg = "#E2D4B7"
    button2 = PushButton(win_class_captain, text="Save Name", command=save_data, grid=[3,2], args=[2])

    #code for captain 3
    captain_box3 = Box(win_class_captain, width="fill", grid=[1,3])
    Text(captain_box3, text="Captain 3: ")
    input_box_3 = TextBox(win_class_captain, text=" ", grid=[2,3])
    captain_box3.bg = "#E2D4B7"
    button3 = PushButton(win_class_captain, command=save_data, text="Save Name", grid=[3,3], args=[3])

    #code for captain 4
    spacer = Box(win_class_captain, width=70, height=70, grid=[1,4])
    captain_box4 = Box(win_class_captain, width="fill", grid=[1,5])
    Text(captain_box4, text="Captain 4: ")
    input_box_4 = TextBox(win_class_captain, text=" ", grid=[2,5])
    captain_box4.bg = "#E2D4B7"
    button4 = PushButton(win_class_captain, command=save_data, text="Save Name", grid=[3,5], args=[4])


    win_class_captain.show(wait=True)
