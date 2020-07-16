import tkinter as tk
from tkinter import ttk

def game():
    display = tk.Tk()
    display.geometry("400x400")

    btn1 = ttk.Button(display, text = "Начать новую игру")
    btn1.place(x = 70, y =120)

    btn2 = ttk.Button(display, text = "Продолжить игру")
    btn2.place(relx = 0.25, rely = 0.5)
    display.mainloop()

game()
