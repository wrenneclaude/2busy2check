import tkinter as tk
from tkinter import font
import requests

HEIGHT = 700
WIDTH = 800

def refresh(players):
    response = requests.get("https://api.2b2t.dev/prioq")
    prioq = response.json()

    label['text'] = format_response(prioq)

def format_response(prioq):
    try:
        people = prioq[1]
        time = prioq[2]

        final_str = 'Players in priority queue: %s \nTime to get into server: %s' % (people, time)
    except:
        final_str = 'The API sucks'

    return final_str

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='m36nuwl22p531.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#000000', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)

button = tk.Button(frame, text="Refresh", font=40, command=lambda: refresh(entry.get()))
button.place(relx=0.5, relwidth=1, relheight=1, anchor='n')

lower_frame = tk.Frame(root, bg='#000000', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Terminal', 18), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

root.mainloop()
