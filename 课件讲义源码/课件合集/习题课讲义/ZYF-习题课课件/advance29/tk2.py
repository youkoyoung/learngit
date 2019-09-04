# 是一个输入密码的小程序，我们自己设定一个密码，如果用户输入正确则现实 正确，否则，显示不正确

# encoding:utf-8

import tkinter as tk
window = tk.Tk()

def check_password():
    password = '123456'
    entered_password = passwordEntry.get()
    if password == entered_password:
        confirmLabel.config(text="正确")
    else:
        confirmLabel.config(text='不正确')


passwordLabel = tk.Label(window, text="Password: ")
passwordEntry = tk.Entry(window, show="*")
button = tk.Button(window, text="校验", command=check_password)
confirmLabel = tk.Label(window)

passwordLabel.pack()
passwordEntry.pack()
button.pack()
confirmLabel.pack()




window.mainloop()