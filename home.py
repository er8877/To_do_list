import tkinter as tk

from sign_up import SignUpApp
from log_in import Ui_Log_in
import mysql.connector

class Ui_home:
    def __init__(self, MainWindow):
        MainWindow.title("Main Window")
        MainWindow.geometry("800x600")
        MainWindow.configure(bg="#00A6FB")
        MainWindow.resizable(False, False)

        self.centralwidget = tk.Frame(MainWindow, bg="#00A6FB", bd=2, relief=tk.SOLID)
        self.centralwidget.place(relwidth=1, relheight=1)

        self.button_sign_up = tk.Button(self.centralwidget, text="Sign Up", font=("Segoe Print", 14), command=self.open_signup)
        self.button_sign_up.place(x=210, y=300, width=140, height=100)
        self.button_sign_up.configure(bg="#051923", fg="#9BDEFF", bd=2, relief=tk.SOLID, borderwidth=2, 
                                      highlightthickness=0, highlightbackground="#9BDEFF", highlightcolor="#9BDEFF")

        self.button_log_in = tk.Button(self.centralwidget, text="Log In", font=("Segoe Print", 14), command=self.open_login)
        self.button_log_in.place(x=430, y=300, width=140, height=100)
        self.button_log_in.configure(bg="#051923", fg="#9BDEFF", bd=2, relief=tk.SOLID, borderwidth=2, 
                                    highlightthickness=0, highlightbackground="#9BDEFF", highlightcolor="#9BDEFF")

        self.label = tk.Label(self.centralwidget, text="Home", font=("Segoe Print", 20))
        self.label.place(x=300, y=60, width=191, height=51)
        self.label.configure(bg="#051923", fg="#9BDEFF", bd=2, relief=tk.SOLID, borderwidth=2, padx=10, pady=4)

        self.button_log_in.bind("<Enter>", self.login_enter)
        self.button_log_in.bind("<Leave>", self.login_leave)
        self.button_sign_up.bind("<Enter>", self.signup_enter)
        self.button_sign_up.bind("<Leave>", self.signup_leave)

    def login_enter(self, event):
        self.button_log_in.config(bg="#003554", fg="#9BDEFF")
    def login_leave(self, event):
        self.button_log_in.config(bg="#051923", fg="#9BDEFF", bd=2, relief=tk.SOLID, borderwidth=2, 
                                    highlightthickness=0, highlightbackground="#9BDEFF", highlightcolor="#9BDEFF")
    def signup_enter(self, event):
        self.button_sign_up.config(bg="#003554", fg="#9BDEFF")
    def signup_leave(self, event):
        self.button_sign_up.config(bg="#051923", fg="#9BDEFF", bd=2, relief=tk.SOLID, borderwidth=2, 
                                    highlightthickness=0, highlightbackground="#9BDEFF", highlightcolor="#9BDEFF")
    

    def signup_hover(self, event):
        self.button_sign_up.configure(background="red") 

    def open_signup(self):
        root = tk.Tk()
        app = SignUpApp(root)
        root.mainloop()


    def open_login(self):
        root = tk.Tk()
        ui = Ui_Log_in(root)
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    ui = Ui_home(root)
    root.mainloop()