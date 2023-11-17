from windows import frames
import tkinter as tk

class MainApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry('500x300')
        self.frames = {}

        main_fr = tk.Frame(self)
        main_fr.pack(side="top", fill="both", expand=True)
        main_fr.grid_rowconfigure(0, weight=1)
        main_fr.grid_columnconfigure(0, weight=1)

        for frame in frames:
            frame_class = frame(master=main_fr, parent=self)
            self.frames[frame.__name__] = frame_class

            frame_class.grid(row=0, column=0, sticky="nsew")

        self.change_page("Clicker")

    def change_page(self, page):
        frame = self.frames[page]
        frame.tkraise()


if __name__ == '__main__':
    app = MainApp(className="Итоговый проект")
    app.mainloop()
