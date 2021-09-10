import tkinter as tk
from tkinter import ttk

class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # self.hi_there = tk.Button(self)
        # self.hi_there["text"] = "Hello World\n(click me)"
        # self.hi_there["command"] = self.say_hi
        # self.hi_there.pack(side="top")

        # self.quit = tk.Button(self, text="QUIT", fg="red",command=self.master.destroy)
        # self.quit.pack(side="bottom")
        self.todo_table = ttk.Treeview(self)
        self.todo_table.pack(fill="both")

    def say_hi(self):
        print("hi there, everyone!")

def main():
    root = tk.Tk()
    app = Application(master=root)
    root.geometry('800x600+500+200')
    app.mainloop()


if __name__ == '__main__':
    main()