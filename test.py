
import tkinter as tk
from tkinter import *

import random

questions = [
    "Кто изобрел язык программирования Pascal?",
    "Как называется оператор ветвления в Pascal?",
    "Как называется цикл, который выполняется до тех пор, пока условие истинно?",
    "Как объявить переменную в Pascal?",
    "Как объявить константу в Pascal?",
    "Как объявить функцию в Pascal?",
    "Что такое массив в Pascal?",
    "Какие типы данных поддерживает Pascal?",
    "Как объявить и использовать процедуру в Pascal?",
    "Какая функция используется для работы с файлами в Pascal?",
]

answers = [
    ["Никлаус Вирт", "Деннис Ритчи", "Дональд Кнут", "Бьерн Страуструп"],
    ["if", "else", "for", "while"],
    ["repeat", "for", "while", "until"],
    ["var myVar: integer","let myVar = 5;","myVar = 5"],
    ["const MY_CONST = 10","let MY_CONST = 10","var MY_CONST: constant = 10"],
    ["def myFunc(): integer","function myFunc(): integer","proc myFunc(): integer"],
    ["Упорядоченный набор элементов одного типа.","Список команд, которые нужно выполнить.","Способ объединения нескольких переменных в одну."],
    ["integer, string, boolean."," int, float, double.","number, bool, char."],
    ["function myProc(): void","proc myProc()","procedure myProc()"],
    ["fileOpen()","assign()","openFile()"],
]

# перемешать ответы на каждый вопрос
for i in range(len(answers)):
    random.shuffle(answers[i])

# список правильных ответов
correct_answers = ["Никлаус Вирт", "if", "repeat","var myVar: integer","const MY_CONST = 10","function myFunc(): integer","Упорядоченный набор элементов одного типа.","integer, string, boolean.","procedure myProc()","assign()"]

# функцию для проверки ответов
def check_answers():
    score = 0
    for i in range(len(questions)):
        answer = var[i].get()
        if answer == correct_answers[i]:
            score += 1
    result_label.config(text=f"Вы ответили правильно на {score} из {len(questions)} вопросов.")

# создать графический интерфейс
root = tk.Tk()
root.title("Тест по языку программирования Pascal")
#Frame
#Frame = Frame(top)
#Frame.pack()




# создать рамку для вопросов
questions_frame = tk.Frame(root)
questions_frame.pack(pady=10)

# создать переменные для ответов
var = []
for i in range(len(questions)):
    var.append(tk.StringVar())

# создавать ярлыки и кнопки для каждого вопроса
for i in range(len(questions)):
    label = tk.Label(questions_frame, text=questions[i])
    label.pack()

    for j in range(len(answers[i])):
        answer = answers[i][j]
        radio_button = tk.Radiobutton(questions_frame, text=answer, variable=var[i], value=answer)
        radio_button.pack()
#скрол бар
scrollbar = Scrollbar(orient="vertical", command=Frame.yview)
scrollbar.pack(side=RIGHT, fill=Y)
# создать кнопку для проверки ответов
button = tk.Button(root, text="Проверить ответы", command=check_answers)
button.pack()

# создать ярлык для результатов
result_label = tk.Label(root)
result_label.pack(pady=10)

#запустить графический интерфейс
root.mainloop()