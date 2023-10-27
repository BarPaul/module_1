import tkinter as tk


class Frame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, width=300, height=200)
        self.setupUI()

    def setupUI(self):
        self.hello_label = tk.Label(self, text="Привет, мир!", font="Times 16", padx=20, pady=25)
        self.input_text = tk.Entry(self, border=3, font="Times 14")
        self.answer_text = tk.Label(self, pady=1)
        self.button_print = tk.Button(self, text="Вывести", width=15, height=2, command=lambda: self.answer_text.config(text=self.input_text.get()))
        self.button_clear = tk.Button(self, text="Очистить", width=15, height=2, command=self.clear_input)
        self.input_text.focus()
        for element in [self.hello_label, self.input_text, self.answer_text]:
            element.pack()
        for i, button in enumerate([self.button_print, self.button_clear]):
            button.place(relx=0.3 + (0.45 * i), rely=0.75, anchor="center")

    def clear_input(self):
        self.answer_text.config(text='')
        self.input_text.delete(0, "end")

if __name__ == '__main__':
    app = tk.Tk(className="Базовый уровень")
    app.geometry("300x200")
    Frame(app).pack(expand=True, fill='both')
    app.mainloop()