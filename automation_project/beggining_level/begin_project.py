import tkinter as tk


class Frame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.setupUI()

    def setupUI(self):
        self.hello_label = tk.Label(self, text="Привет, мир!", font="Times 16", padx=20, pady=25)
        self.input_text = tk.Entry(self, border=3, font="Times 14")
        self.answer_text = tk.Label(self, pady=1)
        self.button_print = tk.Button(self, text="Вывести", width=15, height=2, command=lambda: self.answer_text.config(text=self.input_text.get()))
        self.input_text.focus()
        for element in [self.hello_label, self.input_text, self.answer_text, self.button_print]:
            element.pack()


if __name__ == '__main__':
    app = tk.Tk(className="Начальный уровень")
    app.geometry("300x200")
    Frame(app).pack() 
    app.mainloop()