import tkinter as tk
from random import choice


definitions = {
    "While": "Цикл 'while' используется для выполнения блока кода, пока условие истинно.",
    "For": "Цикл 'for' используется для итерации по элементам последовательности (например, списку или строке).",
    "If": "Условие 'if' позволяет выполнить определенный блок кода, если условие истинно.",
    "Function": "Функция - это блок кода, который можно вызывать с определенными аргументами.",
    "List": "Список - это упорядоченная коллекция элементов, которая может содержать разные типы данных."
}

class Frame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.setupUI()

    def setupUI(self):
        self.definition_text = tk.Label(self, font="Times 14", width=50, height=6, bg="white")
        self.button_show = tk.Button(self, text="Показать определение", command=self.show_random_defition, width=50, height=3, font="Times 16")
        for element in [self.definition_text, self.button_show]:
            element.pack()

    def show_random_defition(self):
        fin, new, old = '', choice(list(definitions.values())), self.definition_text['text']
        while new == old.replace('-\n', ''):
            new = choice(list(definitions.values()))
        for i, s in enumerate(new):
            fin += s
            if (i + 1) % 44 == 0: 
                fin += '-\n' if s.isalpha() else '\n'
        self.definition_text.configure(text=fin)


if __name__ == '__main__':
    app = tk.Tk(className="Определение python")
    app.geometry("400x300")
    Frame(app).pack(expand=True, fill='both')
    app.mainloop()
