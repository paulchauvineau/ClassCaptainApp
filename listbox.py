from guizero import Box, Text, TextBox, PushButton, Window

def class_captains(app):
    cc_list = []

    #Instead of using an app just turned it to a window.
    win_class_captain = Window(app, title="Menu", bg="#034C3C", height="1400", width="1400")

    def save_data(box_no):
        if box_no == 1:
            value_of_textbox = input_box_1.value
            cc_list.append(input_box_1)

        elif box_no == 2:
            value_of_textbox = input_box_2.value
            cc_list.append(input_box_2)

        elif box_no == 3:
            value_of_textbox = input_box_3.value
            cc_list.append(input_box_3)

        elif box_no == 4:
            value_of_textbox = input_box_4.value
            cc_list.append(input_box_4)

        print(value_of_textbox)

    #this is the code for the title box
    spacer = Box(win_class_captain, width=20, height=20)
    title_box = Box(win_class_captain, width=200, height=40, border=True)
    Text(title_box, text="Enter the names of the class captains.", bg="#E2D4B7")
    #-----

    #code for captain 1 box
    spacer = Box(win_class_captain, width=70, height=30)
    captain_box1 = Box(win_class_captain, width="fill")
    Text(captain_box1, text="Captain 1: ")
    input_box_1 = TextBox(win_class_captain, text=" ")
    captain_box1.bg = "#E2D4B7"
    button1 = PushButton(win_class_captain, text="Save Name", command=save_data, args=[1])

    #code for captain 2
    spacer = Box(win_class_captain, width=70, height=150)
    captain_box2 = Box(win_class_captain, width="fill")
    Text(captain_box2, text="Captain 2: ")
    input_box_2 = TextBox(win_class_captain, text=" ")
    captain_box2.bg = "#E2D4B7"
    button2 = PushButton(win_class_captain, text="Save Name", command=save_data, args=[2])

    #code for captain 3
    captain_box3 = Box(win_class_captain, width="fill")
    Text(captain_box3, text="Captain 3: ")
    input_box_3 = TextBox(win_class_captain, text=" ")
    captain_box3.bg = "#E2D4B7"
    button3 = PushButton(win_class_captain, command=save_data, text="Save Name", args=[3])

    #code for captain 4
    spacer = Box(win_class_captain, width=70, height=70)
    captain_box4 = Box(win_class_captain, width="fill")
    Text(captain_box4, text="Captain 4: ")
    input_box_4 = TextBox(win_class_captain, text=" ")
    captain_box4.bg = "#E2D4B7"
    button4 = PushButton(win_class_captain, command=save_data, text="Save Name", args=[4])


    win_class_captain.show(wait=True)
    app.display()


