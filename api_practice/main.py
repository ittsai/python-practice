import requests
from tkinter import *

window = Tk()
window.title("My api say...")
window.config(pady=50, padx=50)

def get_quote():
    response =requests.get("https://api.kanye.rest")
    response.raise_for_status()
    
    if response.status_code == 200:
        data = response.json()
        quote = data.get("quote")
        canvas.itemconfig(quote_text, text=f"{quote}")
    else:
        canvas.itemconfig(quote_text, text=f"Error")

canvas = Canvas(width=300, height=414)
bg_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=bg_img)
quote_text = canvas.create_text(150, 207, text="", width=250, font=("Ariel", 20, "bold"), fill="black")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()
