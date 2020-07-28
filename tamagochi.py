import tkinter as tk
from tkinter import ttk

from myClass import Pet
import time
import json

def game():
    global display
    display = tk.Tk()
    display.geometry("400x400")

    def loads():
        try:
            file = open('save.json', 'r')
            save = json.load(file)
            char = Pet(name = None, age=None, gender=None)
            char.__dict__ = save
            start_game(char)
            file.close()
        except:
            label_no = tk.Label(text = 'Сохранение отсутствует')
            label_no.place(relx = 0.24, rely = 0.6)

    btn1 = ttk.Button(display, text = "Начать новую игру", command = lambda: new_char())
    btn1.place(x = 70, y = 120)

    btn2 = ttk.Button(display, text = "Продолжить игру", command = lambda: loads())
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
    start_game(pet) #здесь у нас будет функция начала игры

def start_game(animal):
    display.destroy() #уничтожаются старые окна
    display_game = tk.Tk()
    label = tk.Label(display_game, text=f'Имя: {animal.name} \nВозраст: {animal.age} \nПол:{animal.gender}')
    label.grid(row = 0, column = 0)

    label_money = tk.Label(display_game, text = f'Всего денег : {animal.money}')
    label_money.grid(row =1, column = 0)

    btn_money = ttk.Button(display_game, text = "Пойти на работу", command = lambda: work(animal))
    btn_money.grid(row = 2, column = 0)

    label_test = tk.Label(display_game, bg='black', height = 12, width = 6)
    label_test2 = tk.Label(display_game, bg='black', height = 12, width = 6)
    label_test3 = tk.Label(display_game, bg='black', height = 12, width = 6)

    label_test.grid(row = 1, column = 1,  sticky = tk.S)
    label_test2.grid(row = 1, column = 2,  sticky = tk.S)
    label_test3.grid(row = 1, column = 3,  sticky = tk.S)

    label_hp = tk.Label(display_game, text = animal.hp, bg='red', height = percent(animal.hp), width = 6)
    label_en = tk.Label(display_game, text = animal.energy, bg='blue', height = percent(animal.energy), width = 6)
    label_mood = tk.Label(display_game, text = animal.mood, bg='green', height = percent(animal.mood), width = 6)
    label_hp.grid(row = 1, column = 1, sticky = tk.S)
    label_en.grid(row = 1, column = 2, sticky = tk.S)
    label_mood.grid(row = 1, column = 3, sticky = tk.S)


    btn_hp = ttk.Button(display_game, text = "Дать еды", command = lambda: buff(animal, 'Покормить'))
    btn_hp.grid(row = 2, column = 1)
    btn_en = ttk.Button(display_game, text = "Дать отдохнуть", command = lambda: buff(animal, 'Отдохнуть'))
    btn_en.grid(row = 2, column = 2)
    btn_mood = ttk.Button(display_game, text = "Поиграть", command = lambda: buff(animal, 'Поиграть'))
    btn_mood.grid(row = 2, column = 3)

    label_hp_text = tk.Label(display_game, text = 'Голод')
    label_hp_text.grid(row = 0, column = 1)
    label_en_text = tk.Label(display_game, text = "Энергия")
    label_en_text.grid(row = 0, column = 2)
    label_mood_text = tk.Label(display_game, text = "Настроение")
    label_mood_text.grid(row = 0, column = 3)

    def game_har(animal):
        if animal.hp > 0:
            animal.hp -= 10
            label_hp.configure(height = percent(animal.hp), text = animal.hp)
            display_game.after(2000, lambda: game_har(animal))
        else:
            finish()
    def finish():
        display_game.destroy()
        animal.time = round(time.monotonic())
        game_over = tk.Tk()
        label_game_over = tk.Label(game_over, text=f''
                                   f'GAME OVER \n'
                                   f'Ваш питомец покинул вас\n'
                                   f'{animal.time} сек', font=('Calibri', 120))
        label_game_over.grid(row = 0, column = 0)



    display_game.after(5000, lambda: game_har(animal))

    def game_har1(animal):
        if animal.energy > 0:
            animal.energy -= 10
            label_en.configure(height = percent(animal.energy), text = animal.energy)
        else:
            animal.hp -= 10
            label_hp.configure(height=percent(animal.hp), text=animal.hp)
        display_game.after(5000, lambda: game_har2(animal))

    display_game.after(5000, lambda: game_har1(animal))

    def game_har2(animal):
        if animal.mood > 0:
            animal.mood -=10
            label_mood.configure(height=percent(animal.mood), text=animal.mood)
        else:
            animal.energy -= 10
            label_en.configure(height = percent(animal.energy), text = animal.energy)
        display_game.after(5000, lambda: game_har1(animal))

    display_game.after(5000, lambda: game_har2(animal))

    def buff(animal, arg):
        if arg == 'Покормить' and animal.hp < 100 and animal.money > 49:
            animal.money -= 50
            animal.hp += 20
            label_money.configure(text = f'Всего денег {animal.money}')
            label_hp.configure(height = percent(animal.hp), text = animal.hp)
        elif arg == "Отдохнуть" and animal.energy < 100:
            animal.energy += 40
            if animal.energy > 100:
                animal.energy = 100
            btn_mood.configure(state='disabled')
            btn_en.configure(state='disabled')
            btn_hp.configure(state='disabled')
            display_game.after(4000, lambda: btn_hp.configure(state='enabled'))
            display_game.after(4000, lambda: btn_en.configure(state='enabled'))
            display_game.after(4000, lambda: btn_mood.configure(state='enabled'))

            label_en.configure(height = percent(animal.energy), text = animal.energy)
        elif arg == 'Поиграть' and animal.mood < 100:
            animal.mood += 20
            if animal.mood > 100:
                animal.mood = 100
            animal.energy -= 10
            animal.hp -= 5
            label_mood.configure(height = percent(animal.mood), text = animal.mood)
            label_mood.configure(height = percent(animal.energy), text = animal.energy)
            label_mood.configure(height = percent(animal.hp), text = animal.hp)


    def work(animal):
        btn_hp.configure(state='disabled')
        btn_en.configure(state='disabled')
        btn_mood.configure(state='disabled')
        btn_money.configure(state='disabled')
        display_game.after(5000, lambda:btn_money.configure(state='enabled'))
        display_game.after(5000, lambda:btn_hp.configure(state='enabled'))
        display_game.after(5000, lambda:btn_en.configure(state='enabled'))
        display_game.after(5000, lambda:btn_mood.configure(state='enabled'))
        animal.money += 200
        label_money.configure(text=f'Всего денег {animal.money}')

def percent(score):
    perc = score * 0.12
    if perc > 12:
        perc = 12
    return round(perc)




if __name__ == '__main__':
    game()
