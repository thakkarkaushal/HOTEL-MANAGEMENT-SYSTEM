import sqlite3
from tkinter import *
import main


class CheckOut:
    def __init__(self, root):
        self.root = root
        pad = 3
        self.root.title("CHECK OUT")
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))

        # create mainframe to add message
        top = Frame(self.root)
        top.pack(side="top")

        bottom = Frame(self.root)
        bottom.pack(side="top")

        info_frame = Frame(self.root)
        info_frame.pack(side="top")

        # display message
        self.label = Label(top, font=('arial', 50, 'bold'), text="CHECK OUT", fg="#15d3ba", anchor="center")
        self.label.grid(row=0, column=3, padx=10, pady=10)

        # room no label
        self.room_no_label = Label(bottom, font=('arial', 20, 'bold'), text="ENTER THE ROOM NUMBER :", fg="#15d3ba",
                                   anchor="center")
        self.room_no_label.grid(row=2, column=2, padx=10, pady=10)

        # text enter field
        self.room_var = IntVar()
        self.room_no_entry = Entry(bottom, width=5, text=self.room_var)
        self.room_no_entry.grid(row=2, column=3, padx=10, pady=10)

        # text enter field
        self.get_info_entry = Text(info_frame, height=15, width=90)
        self.get_info_entry.grid(row=1, column=1, padx=10, pady=10)

        def check_out():
            room_number1 = int(self.room_no_entry.get())
            conn = sqlite3.connect('Hotel.db')
            with conn:
                cursor = conn.cursor()
            cursor.execute(
                'CREATE TABLE IF NOT EXISTS Hotel (Fullname TEXT,Address TEXT,mobile_number TEXT,number_days TEXT,'
                'room_number NUMBER)')
            conn.commit()
            with conn:
                cursor.execute("SELECT room_number FROM Hotel")
                ans = cursor.fetchall()
                room = []
                for i in ans:
                    room.append(i[0])
                if room_number1 in room:
                    with conn:
                        cursor.execute("SELECT Fullname,room_number FROM Hotel")
                        ans = cursor.fetchall()
                        for i in ans:
                            if room_number1 == int(i[1]):
                                self.get_info_entry.insert(INSERT,
                                                           '\n' + str(i[0]) + ' have check out from ' + str(i[1]) + '\n')
                                with conn:
                                    cursor.execute("""DELETE FROM Hotel where room_number = ?""", [room_number1])

                else:
                    self.get_info_entry.insert(INSERT, "PLEASE ENTER VALID ROOM NUMBER")

        # create submit button
        self.check_out_button = Button(bottom, text="CHECK OUT", font=('', 15), bg="#15d3ba", relief=RIDGE, height=2,
                                       width=15,
                                       fg="black", anchor="center", command=check_out)
        self.check_out_button.grid(row=3, column=2, padx=10, pady=10)

        # create submit button
        self.home_button = Button(bottom, text="HOME", font=('', 15), bg="#15d3ba", relief=RIDGE, height=2, width=15,
                                  fg="black", anchor="center", command=main.home_ui)
        self.home_button.grid(row=3, column=3, padx=10, pady=10)


def check_out_ui():
    root = Tk()
    application = CheckOut(root)
    root.mainloop()
