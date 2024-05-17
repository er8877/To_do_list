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
    global d_id
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


def send_user_info(username, password):
    select_usernames = select_valid_usernames()
    if username not in select_usernames:
        insert_user_data(username, password)
        return True
    else:
        print("Invalid username")
        return False


class SignUpApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sign Up")
        self.root.geometry("800x570")
        self.root.configure(bg="#00A6FB")
        self.root.resizable(False,False)

        self.label = tk.Label(self.root, text="Sign Up", font=("Arial", 20), bg="#051923", fg="#9BDEFF",
                              bd=2, relief=tk.SOLID, borderwidth=2, padx=10, pady=4)
        self.label.place(x=310, y=40, width=191, height=51)

        self.label_username = tk.Label(self.root, text="Username : ", font=("Arial", 18), bg="#051923", fg="#9BDEFF",
                                       bd=2, relief=tk.SOLID, borderwidth=2)
        self.label_username.place(x=110, y=160, width=191, height=51)

        self.entry_username = tk.Entry(self.root, font=("Arial", 16), bg="#051923", fg="#9BDEFF", bd=2, relief=tk.SUNKEN,
                                       borderwidth=2, insertbackground="#9BDEFF")
        self.entry_username.place(x=340, y=165, width=371, height=41)

        self.label_password = tk.Label(self.root, text="Password : ", font=("Arial", 18), bg="#051923", fg="#9BDEFF",
                                       bd=2, relief=tk.SOLID, borderwidth=2)
        self.label_password.place(x=110, y=230, width=191, height=51)

        self.entry_password = tk.Entry(self.root, show="*", font=("Arial", 16), bg="#051923", fg="#9BDEFF", bd=2, 
                                       relief=tk.SOLID, borderwidth=2, insertbackground="#9BDEFF")
        self.entry_password.place(x=340, y=235, width=371, height=41)

        self.exit_button = tk.Button(self.root, text="Exit", font=("Arial", 14), bg="#051923", fg="#9BDEFF",
                                     bd=2, relief=tk.SOLID, borderwidth=2, command=self.root.destroy)
        self.exit_button.place(x=30, y=30, width=101, height=41)

        self.register_button = tk.Button(self.root, text="Accept", font=("Segoe Print", 14), bg="#051923", fg="#9BDEFF",
                                         bd=2, relief=tk.SOLID, borderwidth=2, command=self.register_user)
        self.register_button.place(x=360, y=410, width=100, height=100)

        self.label_confirm_password = tk.Label(self.root, text="Confirm\nPassword : ", font=("Arial", 18), bg="#051923", 
                                               fg="#9BDEFF", bd=2, relief=tk.SOLID, borderwidth=2)
        self.label_confirm_password.place(x=110, y=300, width=191, height=80)

        self.entry_confirm_password = tk.Entry(self.root, show="*", font=("Arial", 16), bg="#051923", fg="#9BDEFF", 
                                              bd=2, relief=tk.SOLID, borderwidth=2, insertbackground="#9BDEFF")
        self.entry_confirm_password.place(x=340, y=320, width=371, height=41)

        self.register_button.bind("<Enter>", self.register_enter)
        self.register_button.bind("<Leave>", self.register_leave)
        self.exit_button.bind("<Enter>", self.exit_enter)
        self.exit_button.bind("<Leave>", self.exit_leave)
    

    def register_enter(self, event):
        self.register_button.config(bg="#003554", fg="#9BDEFF")
    def register_leave(self, event):
        self.register_button.config(bg="#051923", fg="#9BDEFF", bd=2, relief=tk.SOLID, borderwidth=2, 
                                    highlightthickness=0, highlightbackground="#9BDEFF", highlightcolor="#9BDEFF")
    
    def exit_enter(self, event):
        self.exit_button.config(bg="#003554", fg="#9BDEFF")
    def exit_leave(self, event):
        self.exit_button.config(bg="#051923", fg="#9BDEFF", bd=2, relief=tk.SOLID, borderwidth=2, 
                                    highlightthickness=0, highlightbackground="#9BDEFF", highlightcolor="#9BDEFF")


    def register_user(self):
        if self.entry_confirm_password.get() != self.entry_password.get():
            messagebox.showwarning("Warning", "The confirma password doesn't match with main password", parent=self.root)
        else:
            if send_user_info(username=self.entry_username.get(), password=self.entry_password.get()):
                messagebox.showinfo("successful", "you registered successfully.you should step back and get in log in part.", parent=self.root)
                self.entry_username.delete(0, tk.END)
                self.entry_password.delete(0, tk.END)
                self.entry_confirm_password.delete(0, tk.END)

            else:
                messagebox.showerror("Error", "The username already exists", parent=self.root)


    def open_to_do(self):
        root1 = tk.Tk()
        app = to_do_list_ui(root1)
        root1.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = SignUpApp(root)
    root.mainloop()