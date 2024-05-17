import tkinter as tk
from tkinter import font
import mysql.connector

def connect_db():
    connect2 = mysql.connector.connect(
        host='localhost', 
        user='root', 
        database='works'
    )
    return connect2

def select_works():
    user_id = open("user_id.txt", "r")
    u_id = int(user_id.read())
    user_id.close()
    
    con = connect_db()
    cursor = con.cursor()
    query = """SELECT title, id FROM tasks WHERE is_doing=%s AND user_id=%s"""
    cursor.execute(query, (0, u_id))
    works = cursor.fetchall()
    cursor.close()
    return works


class Ui_MainWindow:
    def done_work(self):
        con = connect_db()
        cursor = con.cursor()
        query = """UPDATE tasks SET is_doing=%s WHERE id=%s"""
        vals = (1, i)
        cursor.execute(query, vals)
        con.commit()
        cursor.close()


    def __init__(self, root):
        self.root = root
        self.root.title("To Do List")
        self.root.geometry("800x570")
        self.root.configure(bg="#00A6FB")
        self.root.resizable(False,False)

        self.label = tk.Label(self.root, text="Check", font=("Roboto Black", 20, "bold"), bg="#051923", fg="#9BDEFF", bd=2, relief="solid", width=10, height=1)
        self.label.place(x=310, y=20)

        self.border_label_password = tk.Label(self.root, bg="#9BDEFF")
        self.border_label_password.place(x=90, y=90, width=620, height=350)

        self.listbox = tk.Listbox(self.root, bg="#051923", fg="#9BDEFF", bd=2, relief="solid", width=69, height=20)
        self.listbox.place(x=100, y=100, width=600, height=330)
        self.listbox.config(font=("", 15))

        self.button_exit = tk.Button(self.root, text="Exit", font=("Arial", 20), bg="#051923", fg="#9BDEFF", bd=1, relief="solid", width=5, height=1, command=self.root.destroy)
        self.button_exit.place(x=100, y=28, width=80, height=30)

        self.listbox.bind("<<ListboxSelect>>", self.show_value)

        self.works_to_check = select_works()
        self.works = [w[0] for w in self.works_to_check]
        self.index_of_works = [w[1] for w in self.works_to_check]

        for wf in range(len(self.works)):
            self.listbox.insert(wf, f"{wf+1}. {self.works[wf]}")
        

        self.entry = tk.Text(self.root, font=("TkDefaultFont", 14), bg="#051923", fg="#9BDEFF", bd=2, relief="solid", width=25)
        self.entry.place(x=230, y=457, width=340, height=50)
        self.entry.config(padx=10, pady=10)

        self.label_2 = tk.Label(self.root, text="Attention :  When you click on your item that value will appear here .", font=("MV Boli", 14), bg="#00A6FB")
        self.label_2.place(x=40, y=500, width=700, height=90)

        self.button = tk.Button(self.root, text="Done", font=("Monotype Corsiva", 20, "italic"), bg="#051923", fg="#9BDEFF", bd=2, relief="solid", width=101, height=5, command=self.done_work)
        self.button.place(x=600, y=458, width=101, height=50)

        self.label_3 = tk.Label(self.root, text="Work :", font=("Segoe Print", 16), bg="#051923", fg="#9BDEFF", bd=2, relief="solid", width=7, height=1)
        self.label_3.place(x=100, y=460)


    def show_value(self, event):
        global i
        selected_index = event.widget.curselection()[0]
        selected_item = event.widget.get(selected_index).split(".")[1]
        selected_item = selected_item.strip()
        self.entry.delete(1.0, tk.END)  # Clear existing text
        self.entry.insert(tk.END, selected_item)

        index = self.works.index(selected_item)
        i = self.index_of_works[index]    


if __name__ == "__main__":
    root = tk.Tk()
    app = Ui_MainWindow(root)
    root.mainloop()