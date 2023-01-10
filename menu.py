from guizero import App, PushButton, Window, Box
from classCaptains import class_captains
from votingScreen import candidate

def save_data():
    #name = Window(app, title="Enter class captains")
    #name.show(wait=true) #wait stops user from using the window from before
    class_captains(app)

def open_vote():
    #vote = Window(app, title="Vote for class captains")
    #vote.show(wait=True)
    candidate()

def open_results():
    results = Window(app, title="Final results")
    results.show(wait=True)

app = App(title="Menu", height=775, width=1400, bg="#034C3C")

cc_box = Box(app, width="fill", height=258)
v_box = Box(app, width="fill", height=258)
r_box = Box(app, width="fill", height=258)
open_button1 = PushButton(cc_box, text="Class captain", command=save_data)
open_button2 = PushButton(v_box, text="Voting", command=open_vote)
open_button3 = PushButton(r_box, text="Results", command=open_results)



app.display()


