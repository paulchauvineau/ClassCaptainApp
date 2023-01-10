from guizero import App, TextBox, PushButton


def save_data():
    x = input_box.value
    print(x)
    print("Button was pressed")

app = App()
button = PushButton(app, command=save_data)
input_box = TextBox(app, text="Enter class: ")


app.display()
