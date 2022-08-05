from tkinter import *
import check_in_ui
import check_out
import get_info
import customer_info
import os


class Hotel:
    def __init__(self, root):
        self.root = root
        pad = 3
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))

        #making mainframe to show mssgs
        top = Frame(self.root)
        top.pack(side="top")

        # make frame to include buttons
        bottom = Frame(self.root)
        bottom.pack(side="top")

        # print mssgs
        self.label = Label(top, font=('arial', 50, 'bold'), text="WELCOME", fg="#15d3ba", anchor="center")
        self.label.grid(row=0, column=3)

        # button to check in
        self.check_in_button = Button(bottom, text="CHECK IN", font=('', 20), bg="#15d3ba", relief=RIDGE, height=2,
                                      width=50,
                                      fg="black", anchor="center",
                                      command=check_in_ui.check_in_ui_fun)  # call check_in_ui_fun from check_in_ui.py file
        self.check_in_button.grid(row=0, column=2, padx=10, pady=10)

        # button to check out
        self.check_out_button = Button(bottom, text="CHECK OUT", font=('', 20), bg="#15d3ba", relief=RIDGE, height=2,
                                       width=50, fg="black", anchor="center",
                                       command=check_out.check_out_ui)  # call check_out_ui function from check_out.py file
        self.check_out_button.grid(row=1, column=2, padx=10, pady=10)

        # button to show list of customers
        self.room_info_button = Button(bottom, text="INFORMATION OF ROOMS", font=('', 20), bg="#15d3ba", relief=RIDGE,
                                       height=2,
                                       width=50, fg="black", anchor="center",
                                       command=get_info.get_info_ui)  # call get_info_ui function from get_info.py file
        self.room_info_button.grid(row=2, column=2, padx=10, pady=10)

        # create get information of all the guest
        self.get_info_button = Button(bottom, text="INFORMATION OF ALL GUEST", font=('', 20), bg="#15d3ba",
                                      relief=RIDGE,
                                      height=2, width=50, fg="black", anchor="center",
                                      command=customer_info.customer_info_ui)
        # call fucnition customer_info_ui function whcih is made in customer_info.py file
        self.get_info_button.grid(row=3, column=2, padx=10, pady=10)

        # creating button to exit
        self.exit_button = Button(bottom, text="EXIT", font=('', 20), bg="#15d3ba", relief=RIDGE, height=2, width=50,
                                  fg="black",
                                  anchor="center", command=quit)
        self.exit_button.grid(row=4, column=2, padx=10, pady=10)


def home_ui():
    root = Tk()
    application = Hotel(root)
    root.mainloop()


if __name__ == '__main__':
    home_ui()
