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
        self.todo_table['columns'] = ('id','title','completed')
        self.todo_table['show'] = 'headings'
        # conf
        self.todo_table.column('id',anchor=tk.CENTER,width=80)
        self.todo_table.column('title',anchor=tk.CENTER,width=80)
        self.todo_table.column('completed',anchor=tk.CENTER,width=80)
        # header
        self.todo_table.heading('id', text='id', anchor=tk.CENTER)
        self.todo_table.heading('title', text='title', anchor=tk.CENTER)
        self.todo_table.heading('completed', text='completed', anchor=tk.CENTER)

        for i in range(5):
            self.todo_table.insert(parent='', index=i, iid=i, text='', values=("Col 1","Col 1","Col 1"))


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