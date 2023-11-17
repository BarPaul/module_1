import tkinter as tk
from os import getcwd

class Clicker(tk.Frame):
    def __init__(self, master, parent: tk.Tk):
        self.parent = parent
        tk.Frame.__init__(self, master, name="clicker")
        self.setupUI_Clicker()

    def setupUI_Clicker(self):
        self.balance = 0
        self.balance_label = tk.Label(
            self, text=f"{self.balance} rub", font="Times 20", pady=40)
        try:
            self.img = tk.PhotoImage(file='../resources/rub.png')
            self.clicker_button = tk.Button(self, text="Получи рубль", image=self.img, command=lambda: self.change_balance(1), width=200, height=105)
            self.button_clear = tk.Button(self, text="Сброс", command=lambda : self.change_balance(-self.balance), font="Times 16", width=15, height=4)
            # self.store_button = tk.Button(self, text="Магазин", command=lambda: self.parent.change_page('Store'))
            for i, button in enumerate([self.clicker_button, self.button_clear]):
                button.place(relx=0.3 + (0.45 * i), rely=0.75, anchor="center")
            self.balance_label.pack()
        except tk.TclError:
            self.error_title = tk.Label(self, text="Ошибка!", fg="red", font="Verdana 32", pady=48)
            self.error_info = tk.Label(self, text=f'Неверная директория, либо отсутсвует файл rub.png!\nЕсли файл не отсутствует, \nто запустите проект из директории:\n./clicker_project/game\nВы запускаете проект из директории:\n./{'/'.join(getcwd().split('\\')[-3:])}', font="Verdana 12")
            for element in [self.error_title, self.error_info]:
                element.pack()
            print("Ошибка\nНеверная директория!\nЗапускайте из директории ./clicker_project/game")

    def change_balance(self, balance: float):
        self.balance += balance
        self.balance_label.configure(text=str(self.balance) + ' rub')


frames = tuple([Clicker])
