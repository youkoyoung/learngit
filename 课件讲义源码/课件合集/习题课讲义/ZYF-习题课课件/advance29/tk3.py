# encoding:utf-8

# 一个猜数字的小游戏，让计算机随机生成一个整数，用户输入去猜这个整数，如果用户输入正确，那么我们分数加1，并且显示计算机生成的数字
# 如果用户没有输入正确，那么我们的分数不变，还是要显示计算机生成的数字


import random
import tkinter as tk
window = tk.Tk()

maxNo = 10
score = 0
rounds = 0

def button_click():
    global score
    global rounds

    try:
        guess = int(guessBox.get())
        if 0 < guess <= maxNo:
            result = random.randrange(1, maxNo+1)
            if guess == result:
                score += 1
            rounds += 1
        else:
            result = "输入不合法"

    except:
        result = '输入不合法'

    resultLabel.config(text = result)
    scoreLabel.config(text = str(score)+"/"+str(rounds))
    guessBox.delete(0,tk.END)


scoreLabel = tk.Label(window)
resultLabel = tk.Label(window)
guessBox = tk.Entry(window)
guessLabel = tk.Label(window, text="请输入1到"+str(maxNo))
button = tk.Button(window, text="guess", command=button_click)

scoreLabel.pack()
resultLabel.pack()
guessBox.pack()
guessLabel.pack()
button.pack()

window.mainloop()