import sqlite3
from tkinter import *
import main


class CustomerInfo:
    def __init__(self, root):
        self.root = root
        pad = 3
        self.root.title("CUSTOMER INFO")
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))

        # create mainframe to add message
        top = Frame(self.root)
        top.pack(side="top")

        bottom = Frame(self.root)
        bottom.pack(side="top")

        left = Frame(self.root, relief="solid")
        left.pack(side="left")

        right = Frame(self.root, relief="solid")
        right.pack(side="left")

        # display message
        self.label = Label(top, font=('arial', 50, 'bold'), text="LIST OF CUSTOMER", fg="#15d3ba", anchor="center")
        self.label.grid(row=0, column=3, padx=10, pady=10)

        # display message
        self.name_label = Label(left, font=('arial', 20, 'bold'), text="NAME", fg="#15d3ba", anchor="center")
        self.name_label.grid(row=0, column=1, padx=10, pady=10)

        # text enter field
        self.name_customer_entry = Text(left, height=30, width=70)
        self.name_customer_entry.grid(row=1, column=1, padx=10, pady=10)

        # display message
        self.room_no_label = Label(right, font=('arial', 20, 'bold'), text="ROOM NO", fg="#15d3ba", anchor="center")
        self.room_no_label.grid(row=0, column=1, padx=10, pady=10)

        # text enter field
        self.room_no_customer_entry = Text(right, height=30, width=70)
        self.room_no_customer_entry.grid(row=1, column=1, padx=10, pady=10)

        # create home button
        self.home_button = Button(top, text="HOME", font=('', 15), bg="#15d3ba", relief=RIDGE, height=2, width=15,
                                  fg="black", anchor="center", command=main.home_ui)
        self.home_button.grid(row=8, column=3, padx=10, pady=10)

        def display_info():

            conn = sqlite3.connect('Hotel.db')
            with conn:
                cursor = conn.cursor()
            cursor.execute(
                'CREATE TABLE IF NOT EXISTS Hotel (Fullname TEXT,Address TEXT,mobile_number TEXT,number_days TEXT,'
                'room_number NUMBER)')
            conn.commit()
            with conn:
                cursor.execute("SELECT Fullname FROM Hotel")
                ans = cursor.fetchall()
                for i in ans:
                    self.name_customer_entry.insert(INSERT, i[0] + '\n')

            with conn:
                cursor.execute("SELECT room_number FROM Hotel")
                ans = cursor.fetchall()
                for i in ans:
                    self.room_no_customer_entry.insert(INSERT, str(i[0]) + '\n')
        # create display button
        self.display_button = Button(top, text="DISPLAY", font=('', 15), bg="#15d3ba", relief=RIDGE, height=2, width=15,
                                     fg="black", anchor="center", command=display_info)
        self.display_button.grid(row=8, column=4, padx=10, pady=10)


def customer_info_ui():
    root = Tk()
    application = CustomerInfo(root)
    root.mainloop()
