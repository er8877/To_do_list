import tkinter as tk
from tkinter import messagebox
import mysql.connector
from check_to_do_list2 import Ui_MainWindow
from all_works_page import Ui_all_tasks_page
from did_page_to_do_list import Ui_did_page

def connect_db():
    connect2 = mysql.connector.connect(
        host='localhost', 
        user='root', 
        database='works'
    )
    return connect2


def id_maker():
    con = connect_db()
    cursor = con.cursor()
    db_prompt = '''SELECT `id` FROM `tasks` WHERE id=(SELECT Max(id) FROM `tasks` )'''
    cursor.execute(db_prompt)
    current_id = cursor.fetchall()
    if current_id:
        return current_id[0][0] + 1
    else:
        return 1


def insert_user_tasks(title):
    global user_id
    u_id = open("user_id.txt", "r")
    user_id = u_id.read()
    user_id = int(user_id)

    con = connect_db()
    cursor = con.cursor()
    d_id = id_maker()
    query = """INSERT INTO `tasks`(id, user_id, title, is_doing) VALUES(%s, %s, %s, %s)"""
    val = (d_id, user_id, title, 0)
    cursor.execute(query, val)
    con.commit()
    con.close()


def select_valid_usernames():
    con = connect_db()
    query = """SELECT user_name FROM users"""
    cursor = con.cursor()
    cursor.execute(query)
    values = cursor.fetchall()
    cursor.close()

    return [v[0] for v in values]

def user_did(work):
    con = connect_db()
    cursor =con.cursor()
    query = "UPDATE `tasks` SET is_doing=%s WHERE id=%s"
    val = (1, 5)
    cursor.execute(query, val)
    con.commit()




class to_do_list_ui:
    def __init__(self, root):
        self.root = root
        self.root.title("To Do List")
        self.root.geometry("800x570")
        self.root.configure(bg="#00A6FB")
        self.root.resizable(False,False)

        self.label = tk.Label(self.root, text="To Do List", bg="#051923", fg="#9BDEFF", bd=2, relief="solid", font=("Roboto Black", 20), width=10)
        self.label.place(x=320, y=30)

        self.label_2 = tk.Label(self.root, text="Add task :", bg="#051923", fg="#9BDEFF", bd=2, relief="solid", font=("Arial", 16), width=10)
        self.label_2.place(x=40, y=150)

        self.textEdit_task = tk.Text(self.root, bg="#051923", fg="#9BDEFF", bd=2, relief="solid", font=("Arial", 14), height=6, width=37)
        self.textEdit_task.place(x=40, y=210)
        self.textEdit_task.config(padx=8, pady=8) 

        self.pushButton_add_task_db = tk.Button(self.root, text="Accept", bg="#051923", fg="#9BDEFF", bd=2, relief="solid", font=("MV Boli", 14), width=10, command=self.send_data_to_db)
        self.pushButton_add_task_db.place(x=40, y=380)

        self.pushButton_check = tk.Button(self.root, text="To do", bg="#051923", fg="#9BDEFF", bd=2, relief="solid", font=("Noto Serif", 16), width=13, command=self.open_check)
        self.pushButton_check.place(x=540, y=290)

        self.pushButton_did = tk.Button(self.root, text="Did", bg="#051923", fg="#9BDEFF", bd=2, relief="solid", font=("Noto Serif", 16), width=13, command=self.open_did)
        self.pushButton_did.place(x=540, y=370)

        self.pushButton_didnt = tk.Button(self.root, text="All tasks", bg="#051923", fg="#9BDEFF", bd=2, relief="solid", font=("Noto Serif", 16), width=13, command=self.open_all_tasks)
        self.pushButton_didnt.place(x=540, y=450)

        self.pushButton_exit = tk.Button(self.root, text="Exit", bg="#051923", fg="#9BDEFF", bd=2, relief="solid", font=("Roboto Condensed", 16), width=8)
        self.pushButton_exit.place(x=20, y=20)

        self.pushButton_add_task_db.bind("<Enter>", self.add_task_enter)
        self.pushButton_add_task_db.bind("<Leave>", self.add_task_leave)
        self.pushButton_check.bind("<Enter>", self.check_enter)
        self.pushButton_check.bind("<Leave>", self.check_leave)
        self.pushButton_did.bind("<Enter>", self.did_enter)
        self.pushButton_did.bind("<Leave>", self.did_leave)
        self.pushButton_exit.bind("<Enter>", self.exit_enter)
        self.pushButton_exit.bind("<Leave>", self.exit_leave)

    def send_data_to_db(self):
        u_task = self.textEdit_task.get("1.0", "end-1c")
        insert_user_tasks(title=u_task)
        messagebox.showinfo("added", "your task added", parent=self.root)
        self.textEdit_task.delete("1.0", tk.END)

    def add_task_enter(self, event):
        self.pushButton_add_task_db.config(bg="#003554", fg="#9BDEFF")
    def add_task_leave(self, event):
        self.pushButton_add_task_db.config(bg="#051923", fg="#9BDEFF", bd=2, relief=tk.SOLID, borderwidth=2, 
                                    highlightthickness=0, highlightbackground="#9BDEFF", highlightcolor="#9BDEFF")
    def check_enter(self, event):
        self.pushButton_check.config(bg="#003554", fg="#9BDEFF")
    def check_leave(self, event):
        self.pushButton_check.config(bg="#051923", fg="#9BDEFF", bd=2, relief=tk.SOLID, borderwidth=2, 
                                    highlightthickness=0, highlightbackground="#9BDEFF", highlightcolor="#9BDEFF")
        
    def did_enter(self, event):
        self.pushButton_did.config(bg="#003554", fg="#9BDEFF")
    def did_leave(self, event):
        self.pushButton_did.config(bg="#051923", fg="#9BDEFF", bd=2, relief=tk.SOLID, borderwidth=2, 
                                    highlightthickness=0, highlightbackground="#9BDEFF", highlightcolor="#9BDEFF")
    
    def didnt_enter(self, event):
        self.pushButton_didnt.config(bg="#003554", fg="#9BDEFF")
    def didnt_leave(self, event):
        self.pushButton_didnt.config(bg="#051923", fg="#9BDEFF", bd=2, relief=tk.SOLID, borderwidth=2, 
                                    highlightthickness=0, highlightbackground="#9BDEFF", highlightcolor="#9BDEFF")
        
    def exit_enter(self, event):
        self.pushButton_exit.config(bg="#003554", fg="#9BDEFF")
    def exit_leave(self, event):
        self.pushButton_exit.config(bg="#051923", fg="#9BDEFF", bd=2, relief=tk.SOLID, borderwidth=2, 
                                    highlightthickness=0, highlightbackground="#9BDEFF", highlightcolor="#9BDEFF")
        
    def open_check(self):
        root = tk.Tk()
        app = Ui_MainWindow(root)
        root.mainloop()
    
    def open_all_tasks(self):
        root = tk.Tk()
        app = Ui_all_tasks_page(root)
        root.mainloop()
    
    def open_did(self):
        root = tk.Tk()
        app = Ui_did_page(root)
        root.mainloop()
        
        

if __name__ == "__main__":
    root = tk.Tk()
    app = to_do_list_ui(root)
    root.mainloop()