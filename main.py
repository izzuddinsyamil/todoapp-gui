from tkinter import *
from functools import partial
from db import DB

class MyWindow:
    def __init__(self, win, db):
        self.db = db

        # list todo
        self.list_frame = LabelFrame(win,
            text="Todo List", borderwidth=2)
        self.list_frame.pack(fill="both",
            expand="yes")
        self.list_content = None
        self.get_list_todos()

        # insert todo
        insert_frame = LabelFrame(win, text="Insert Todo",
            borderwidth=2)
        insert_frame.pack(fill="both", expand="yes")

        insert_entry = Entry(insert_frame)
        insert_entry.pack(side="left", padx=10)

        submit_insert = Button(insert_frame, text="Submit",
            command=partial(self.insert_todo, insert_entry))
        submit_insert.pack(side="left")

        # delete todo
        delete_frame = LabelFrame(win, text="Delete Todo",
            borderwidth=2)
        delete_frame.pack(fill="both", expand="yes")

        delete_entry = Entry(delete_frame)
        delete_entry.pack(side="left", padx=10)

        submit_delete = Button(delete_frame, text="Submit",
            command=partial(self.delete_todo, delete_entry))
        submit_delete.pack(side="left")

    def get_list_todos(self):
        self.list_content = Frame(self.list_frame)
        self.list_content.pack()

        todos = self.db.list_todo()

        for todo in todos:
            Label(self.list_content, text=todo).pack()
    
    def insert_todo(self, name_entry):
        name = name_entry.get()
        self.db.insert_todo(name)
        self.refresh_list()
    
    def delete_todo(self, name_entry):
        name = name_entry.get()
        self.db.delete_todo(name)
        self.refresh_list()

    def refresh_list(self):
        self.list_content.destroy()
        self.get_list_todos()

def main():
    window = Tk()

    db = DB()

    MyWindow(window, db)
    window.title('Todo App')
    window.geometry("300x500")
    window.mainloop()


if __name__ == "__main__":
    main()
