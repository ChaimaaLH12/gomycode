import tkinter as tk
import numpy as np

def computers_choice():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = np.random.choice(choices)
    return computer_choice

def play(player_choice):
    lf1 = tk.LabelFrame(f, height=100, width=100, bg='#2C3895', padx=90, pady=100)
    lf1.pack()
    
    l1 = tk.Label(lf1, bg='blue', fg='red', text='Computer', font=('Algerian', 25))
    l1.grid(row=1, column=2)

    computer_choice = computers_choice()
    l1.config(text=f'The Computer chose:\n{computer_choice}')

    lf2 = tk.LabelFrame(f, height=100, width=100, bg='#2C3895', padx=90, pady=100)
    lf2.pack()

    l2 = tk.Label(lf2, bg='blue', fg='red', text='Result', font=('Algerian', 25))
    l2.grid(row=1, column=2)

    if player_choice == computer_choice:
        l2.config(text='Tie')
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        l2.config(text='You won! Congrats!')
    else:
        l2.config(text='You lost, Try again.')

w = tk.Tk()
w.title("Rock, Paper, Scissors")
w.geometry('1000x1000')

f = tk.Frame(w)
f.pack()

lf = tk.LabelFrame(f, height=100, width=100, bg='#2C3895', padx=50, pady=50)
lf.pack()

l = tk.Label(lf, text='Player', bg='blue', fg='red', font=('Algerian', 25))
l.grid(row=0, column=2)

buttons = ['rock', 'paper', 'scissors']
functions = [lambda choice=choice: play(choice) for choice in buttons]

for idx, (btn_text, func) in enumerate(zip(buttons, functions)):
    button = tk.Button(lf, text=btn_text, width=20, bg='black', fg='#FFA701', activeforeground='black',
                       activebackground='#FFA701', command=func)
    button.grid(row=2, column=idx + 1)

w.mainloop()
