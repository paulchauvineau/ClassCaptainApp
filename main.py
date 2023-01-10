from guizero import App, PushButton, Text, Window

num = 0

def change_background():
    global num
    print("boo")
    app.bg = "red"
    num += 1
    message.value = "yes"

app = App()
button = PushButton(app, command=change_background)
message = Text(app, text="does kai suck")
app.display()

#-----------------------------------------------------------------------------------------

