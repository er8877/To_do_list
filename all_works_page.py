import tkinter as tk
import mysql.connector

def connect_db():
    con = mysql.connector.connect(host="localhost", database= "works", user="root")
    return con

def select_works_did():
    user_id = open("user_id.txt", "r").read()
    u_id = int(user_id)
    con = connect_db()
    cursor = con.cursor()
    query = "SELECT `title` FROM `tasks` WHERE user_id=%s"
    cursor.execute(query, (u_id, ))
    data = cursor.fetchall()
    return data


class Ui_all_tasks_page:
    def __init__(self, root):
        self.root = root
        self.root.title("To Do List")
        self.root.geometry("800x570")
        self.root.configure(bg="#00A6FB")
        self.root.resizable(False,False)

        self.label = tk.Label(self.root, text="All tasks", font=("Roboto Black", 20, "bold"), bg="#051923", fg="#9BDEFF", bd=2, relief="solid", width=10, height=1)
        self.label.place(x=310, y=20)

        self.button_exit = tk.Button(self.root, text="Exit", font=("Arial", 20), bg="#051923", fg="#9BDEFF", bd=1, relief="solid", width=5, height=1, command=self.root.destroy)
        self.button_exit.place(x=60, y=28, width=80, height=30)

        self.listbox = tk.Listbox(self.root, bg="#051923", fg="#9BDEFF", bd=2, relief="solid", width=69, height=20)
        self.listbox.place(x=60, y=85, width=680, height=450)
        self.listbox.config(font=("", 15))

        works_did = select_works_did()
        works = [v[0] for v in works_did]
        for w in range(len(works)):
            self.listbox.insert(w, f"{w+1}. {works[w]}")


if __name__ == "__main__":
    root = tk.Tk()
    app = Ui_all_tasks_page(root)
    root.mainloop()