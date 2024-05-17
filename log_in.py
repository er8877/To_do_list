import tkinter as tk
import mysql.connector
from tkinter import messagebox
from to_do_list_home_part import to_do_list_ui


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
    db_prompt = '''SELECT `id` FROM `users` WHERE id=(SELECT Max(id) FROM `users` )'''
    cursor.execute(db_prompt)
    current_id = cursor.fetchall()
    if current_id:
        return current_id[0][0] + 1
    else:
        return 1


def insert_user_data(username, password):
    con = connect_db()
    cursor = con.cursor()
    d_id = id_maker()
    query = """INSERT INTO `users`(id, user_name, password) VALUES(%s, %s, %s)"""
    val = (d_id, username, password)
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


def select_uname_pass():
    con = connect_db()
    cursor = con.cursor()
    query = """SELECT user_name, password FROM users"""
    cursor.execute(query)
    data = cursor.fetchall()

    return data

def select_specified_username(username):
    con = connect_db()
    cursor = con.cursor()
    query = """SELECT password, id FROM users WHERE user_name=%s"""
    cursor.execute(query, (username, ))
    password = cursor.fetchall()
    return password


class Ui_Log_in:
    def __init__(self, root):
        self.root = root
        self.root.title("Sign Up")
        self.root.geometry("800x570")
        self.root.configure(bg="#00A6FB")
        self.root.resizable(False,False)

        # Border label for password entry
        self.border_label_password = tk.Label(self.root, bg="#9BDEFF")
        self.border_label_password.place(x=347, y=223, width=377, height=50)
        self.border_label_username = tk.Label(self.root, bg="#9BDEFF")
        self.border_label_username.place(x=347, y=295, width=377, height=50)

        self.label_password = tk.Label(self.root, text="Username : ", font=("Arial", 18), bg="#051923", fg="#9BDEFF", 
                                       bd=2, relief=tk.SOLID, borderwidth=2)
        self.label_password.place(x=110, y=220, width=191, height=51)
        self.label_username = tk.Label(self.root, text="Password : ", font=("Arial", 18), bg="#051923", fg="#9BDEFF", 
                                       bd=2, relief=tk.SOLID, borderwidth=2)
        self.label_username.place(x=110, y=293, width=191, height=51)

        # Border label for login label
        self.border_label_login = tk.Label(self.root, bg="#9BDEFF")
        self.border_label_login.place(x=315, y=37, width=200, height=57)

        self.lineEdit_password = tk.Entry(self.root, font=("Arial", 16), bg="#051923", fg="#9BDEFF", bd=2, relief=tk.SUNKEN, 
                                          borderwidth=2, insertbackground="#9BDEFF")
        self.lineEdit_password.place(x=350, y=300, width=371, height=41)

        self.lineEdit_username = tk.Entry(self.root, font=("Arial", 16), bg="#051923", fg="#9BDEFF", bd=2, relief=tk.SUNKEN, 
                                          borderwidth=2, insertbackground="#9BDEFF")
        self.lineEdit_username.place(x=350, y=227, width=371, height=41)

        self.label = tk.Label(self.root, text="Log In", font=("Arial", 20), bg="#051923", fg="#9BDEFF", bd=2, 
                             relief=tk.SOLID, borderwidth=2, padx=10, pady=4)
        self.label.place(x=320, y=40, width=191, height=51)

        self.button_accept = tk.Button(self.root, text="Accept", font=("Segoe Print", 14), bg="#051923", fg="#9BDEFF", bd=2, 
                                      relief=tk.SOLID, borderwidth=2, command=self.login_db)
        self.button_accept.place(x=350, y=440, width=100, height=100)

        self.exit_button = tk.Button(self.root, text="Exit", font=("Arial", 14), bg="#051923", fg="#9BDEFF",
                                     bd=2, relief=tk.SOLID, borderwidth=2, command=self.root.destroy)
        self.exit_button.place(x=30, y=30, width=101, height=41)

        self.button_accept.bind("<Enter>", self.accept_enter)
        self.button_accept.bind("<Leave>", self.accept_leave)
        self.exit_button.bind("<Enter>", self.exit_enter)
        self.exit_button.bind("<Leave>", self.exit_leave)

    
    def accept_enter(self, event):
        self.button_accept.config(bg="#003554", fg="#9BDEFF")
    def accept_leave(self, event):
        self.button_accept.config(bg="#051923", fg="#9BDEFF", bd=2, relief=tk.SOLID, borderwidth=2, 
                                    highlightthickness=0, highlightbackground="#9BDEFF", highlightcolor="#9BDEFF")
        
    def exit_enter(self, event):
        self.exit_button.config(bg="#003554", fg="#9BDEFF")
    def exit_leave(self, event):
        self.exit_button.config(bg="#051923", fg="#9BDEFF", bd=2, relief=tk.SOLID, borderwidth=2, 
                                    highlightthickness=0, highlightbackground="#9BDEFF", highlightcolor="#9BDEFF")

    def login_db(self):
        db_password = select_specified_username(username=self.lineEdit_username.get())[0][0]
        user_id = select_specified_username(username=self.lineEdit_username.get())[0][1]
        print(db_password, "\n", user_id)
        file = open("user_id.txt", "w")
        file.write(f"{user_id}")
        file.close()
        current_password = int(self.lineEdit_password.get().strip())
        print(current_password, type(current_password))

        if current_password == db_password:
            messagebox.showinfo("successful", "you successfully loged in", parent=self.root)
            self.open_to_do_list()
        else:
            messagebox.showerror("Error", "your password is invalid", parent=self.root)
    

    def open_to_do_list(self):
        root = tk.Tk()
        app = to_do_list_ui(root)
        root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    ui = Ui_Log_in(root)
    root.mainloop()