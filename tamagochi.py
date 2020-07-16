import tkinter as tk
from tkinter import ttk

from myClass import Pet

def game():
    global display
    display = tk.Tk()
    display.geometry("400x400")

    btn1 = ttk.Button(display, text = "Начать новую игру", command = lambda: new_char())
    btn1.place(x = 70, y =120)

    btn2 = ttk.Button(display, text = "Продолжить игру")
    btn2.place(relx = 0.25, rely = 0.5)
    display.mainloop()

def new_char():
    char_okno = tk.Toplevel()

    label1 = tk.Label(char_okno, text = 'Имя питомца')
    label2 = tk.Label(char_okno, text = 'Возраст питомца')
    label3 = tk.Label(char_okno, text = 'Пол питомца')

    label1.grid(row = 0, column = 0)
    label2.grid(row = 1, column = 0)
    label3.grid(row = 2, column = 0)

    field1 = tk.Entry(char_okno)
    field2 = tk.Entry(char_okno)
    field3 = tk.Entry(char_okno)

    field1.grid(row = 0, column = 1)
    field2.grid(row = 1, column = 1)
    field3.grid(row = 2, column = 1)

    button = ttk.Button(char_okno, text = "Создать питомца", command=lambda: pet_create(
        field1.get(), field2.get(), field3.get()))
    button.grid(row = 3, column = 0)
    char_okno.mainloop()


def pet_create(name, age, gender):
    pet = Pet(name, age, gender)
    print(pet.__dict__)

def start_game(animal):
    display.destroy()
    display_game = tk.Tk()

game()
