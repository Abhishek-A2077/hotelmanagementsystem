from tkinter import *
from tkinter import messagebox,ttk
from datetime import datetime, date
import mysql.connector as sql
from PIL import ImageTk

class Hotel(Tk):
    def __init__(self):
        super().__init__()
        pad = 3
        self.title("Hotel Management System: OceanView")
        self.geometry("1600x950")
        self.iconbitmap("palm.ico")
        
        #making canvas
        my_canvas = Canvas(self, width = 1600, height = 950)
        my_canvas.pack(fill = 'both', expand = True)

        #making bg img
        bg = ImageTk.PhotoImage(file="bg_img.jpg")
        self.back = Label(self)
        self.back.image = bg; # Adding a reference to the image so that it isn't deleted from memory during class instantiation.
        my_canvas.create_image(0,0, image = bg, anchor = 'nw')

        #Adding label via canvas
        my_canvas.create_text(320, 5, text = "Welcome To OceanView Hotel!", font = ("High Tower Text", 50), fill = "#006b56", anchor = "nw")

        # create check in button
        cin = ImageTk.PhotoImage(file="cin_b.png")
        self.cin_l = Label(self, image=cin)
        self.cin_l.image = cin;
        cin_Button = my_canvas.create_image(450, 130, image=cin, anchor = 'nw') # Creating an image which will act as button
        my_canvas.tag_bind(cin_Button, "<Button-1>", self.open_check_in_window) # Binding a method to the image acting like a button

        # create check out button
        cout = ImageTk.PhotoImage(file="cout_b.png")
        self.cout_l = Label(self, image=cout)
        self.cout_l.image = cout;
        cout_Button = my_canvas.create_image(450, 240, image=cout, anchor = 'nw')
        my_canvas.tag_bind(cout_Button, "<Button-1>", self.open_check_out_window) 

        # create show list button
        cinf_r = ImageTk.PhotoImage(file="cinf_r.png")
        self.cinf_r_l = Label(self, image=cinf_r)
        self.cinf_r_l.image = cinf_r;
        cinf_r_Button = my_canvas.create_image(450, 350, image=cinf_r, anchor = 'nw') 
        my_canvas.tag_bind(cinf_r_Button, "<Button-1>", self.open_get_info_window) 
                                       
        # create get information of all the guest
        cinf_a = ImageTk.PhotoImage(file="cinf_a.png")
        self.cinf_a_l = Label(self, image=cinf_a)
        self.cinf_a_l.image = cinf_a;
        cinf_a_Button = my_canvas.create_image(450, 460, image=cinf_a, anchor = 'nw') 
        my_canvas.tag_bind(cinf_a_Button, "<Button-1>", self.open_full_cinfo_window) 
                                      
        # button to exit the program
        exxit = ImageTk.PhotoImage(file="exxit.png")
        self.exxit_l = Label(self, image=cinf_r)
        self.exxit_l.image = exxit;
        exxit_Button = my_canvas.create_image(570, 590, image=exxit, anchor = 'nw') 
        my_canvas.tag_bind(exxit_Button, "<Button-1>", self.close_win) 

        # button to view the about page
        abt = ImageTk.PhotoImage(file="abt.png")
        self.abt_l = Label(self, image=abt)
        self.abt_l.image = abt;
        abt_Button = my_canvas.create_image(570, 660, image=abt, anchor = 'nw') 
        my_canvas.tag_bind(abt_Button, "<Button-1>", self.open_about_window) 
        
        con = sql.connect(host = 'localhost',user = 'root', password = 'tiger')
        try:
            cur = con.cursor()
            cur.execute('CREATE DATABASE IF NOT EXISTS hotel;')
            cur.execute('USE Hotel;')
            cur.execute("CREATE TABLE IF NOT EXISTS Hotel (Name Varchar(20) primary key, mobile_number bigint, number_days int, room_number int, suite_t varchar(30), price int, date1 date default(current_date));")
            cur.execute('CREATE TABLE IF NOT EXISTS rooms_del (r_no int(3));')
            cur.execute('CREATE TABLE IF NOT EXISTS rooms_nondel (r_no int(3));')
            
            cur.execute("SELECT * FROM rooms_del;")
            r = cur.fetchall()
            if len(r) == 0:
                for i in range(51):
                    r = 100
                    cur.execute('INSERT INTO rooms_del VALUES ({});'.format(r+i))
            
            cur.execute("SELECT * FROM rooms_nondel;")
            r = cur.fetchall()
            if len(r) == 0:
                for i in range(51):
                    r = 100
                    cur.execute('INSERT INTO rooms_nondel VALUES ({});'.format(r+i+51))
            else:
                pass
            
            con.commit()
        except:
            print("ERROR_main")
            con.rollback()
        con.close()

    def open_check_in_window(self, holder1):
        window = CheckIN(self)
        window.grab_set()

    def open_check_out_window(self, holder2):
        window = CheckOut(self)
        window.grab_set()

    def open_get_info_window(self, holder3):
        window = GetInfo(self)
        window.grab_set()

    def open_full_cinfo_window(self, holder4):
        window = CustomerInfo(self)
        window.grab_set()

    def open_about_window(self, holder5):
        window = About(self)
        window.grab_set()

    def close_win(self,h2):
        self.destroy()




# GET INFO UI ========================================================================================================================================================================================================

class GetInfo(Toplevel):
    def __init__(self, root):
        super().__init__(root)
        pad = 3
        self.title("Customer Info")
        self.geometry("1600x950")
        self.iconbitmap("palm.ico")

        # Creating Canvas
        my_canvas = Canvas(self, width = 1600, height = 950)
        my_canvas.pack(fill = 'both', expand = True)

        #Adding Background Image
        bg = ImageTk.PhotoImage(file="bg_2.jpg")
        self.back = Label(self)
        self.back.image = bg; # Adding a reference to the image so that it isn't deleted from memory during class instantiation.
        my_canvas.create_image(0,0, image = bg, anchor = 'nw')

        # Adding Title
        my_canvas.create_text(420, 5, text = "Customer Info", font = ("High Tower Text", 50), fill = "#006b56", anchor = "nw")
        
        #room number
        my_canvas.create_text(350, 110, text = "Enter Room Number:", font = ("High Tower Text", 40), fill = "#006b56", anchor = "nw")                       
        
        # text entry field for room number
        self.room_var = StringVar()
        self.room_no_entry = Entry(self, width=10, text='')
        self.room_no_entry.place(x=900, y=140)

        # info window
        self.get_info_entry = Text(self, height=12, width=90)
        self.get_info_entry.place(x=400,y=230)
        self.get_info_entry.configure(state='disabled')

        def close_win(holder):
            self.destroy()

        def get_info_msq(holder):
            room_no = self.room_no_entry.get()
            if not room_no.isdigit():
                messagebox.showerror("ERROR", "The number you entered is invalid!", parent = self) # parent attribute keeps the error box displayed on top of current window
                self.room_no_entry.delete(0, END)
                self.room_no_entry.insert(0, "")
            else:
                try:
                    room_no = int(room_no)
                    con = sql.connect(host = 'localhost',user = 'root', password = 'tiger', database = 'hotel')
                    cur = con.cursor()
                    cur.execute("SELECT * FROM Hotel;")
                    r_list = cur.fetchall()
                    if len(r_list) == 0:
                        self.get_info_entry.configure(state='normal')
                        self.get_info_entry.delete('1.0', END)
                        self.get_info_entry.insert(INSERT, "\nNO ROOMS IN USE!")
                        self.get_info_entry.configure(state='disabled')
                    else:
                        for i in r_list:
                            if room_no == i[3]:
                                self.get_info_entry.configure(state='normal')
                                self.get_info_entry.delete('1.0', END)
                                self.get_info_entry.insert(INSERT, 'NAME: ' + str(i[0]) + '\nMOBILE NUMBER:  ' + str(i[1]) + '\nNUMBER OF DAYS: ' + str(i[2]) + '\nROOM NUMBER: ' + str(i[3]) + '\nSUITE TYPE: ' + str(i[4]))
                                self.get_info_entry.configure(state='disabled')
                                break
                        else:
                            self.get_info_entry.configure(state='normal')
                            self.get_info_entry.delete('1.0', END)
                            self.get_info_entry.insert(INSERT, 'Please Enter Valid Room Number!')
                            self.get_info_entry.configure(state='disabled')

                    con.commit()
                except:
                    print("ERROR_customer_info")
                    con.rollback()
                con.close()

        # Create get info button
        getinf = ImageTk.PhotoImage(file="get_info.png")
        self.getinf_l = Label(self, image=getinf)
        self.getinf_l.image = getinf;
        getinf_Button = my_canvas.create_image(250, 475, image=getinf, anchor = 'nw')
        my_canvas.tag_bind(getinf_Button, "<Button-1>", get_info_msq)                      

        # create home button
        home = ImageTk.PhotoImage(file="home.png")
        self.home_l = Label(self, image=home)
        self.home_l.image = home;
        home_Button = my_canvas.create_image(950, 475, image=home, anchor = 'nw')
        my_canvas.tag_bind(home_Button, "<Button-1>", close_win)

# FULL CUSTOMER UI ========================================================================================================================================================================================================

class CustomerInfo(Toplevel):
    def __init__(self, root):
        super().__init__(root)
        pad = 3
        self.dis = True
        self.title("Customer Info")
        self.geometry("1600x950")
        self.iconbitmap("palm.ico")
            
        # Creating Canvas
        my_canvas = Canvas(self, width = 1600, height = 950)
        my_canvas.pack(fill = 'both', expand = True)

        #Adding Background Image
        bg = ImageTk.PhotoImage(file="bg_2.jpg")
        self.back = Label(self)
        self.back.image = bg; # Adding a reference to the image so that it isn't deleted from memory during class instantiation.
        my_canvas.create_image(0,0, image = bg, anchor = 'nw')

        # Adding Title
        my_canvas.create_text(560, 5, text = "Customer List:", font = ("High Tower Text", 50), fill = "#006b56", anchor = "nw")

        # creating treeview to display data
        self.cols = ('Name', 'Mobile Number', 'No. of Days', 'Room Number', 'Suite Type', 'Price')
        self.tree = ttk.Treeview(self, columns=self.cols, show='headings')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Mobile Number', text='Mobile Number')
        self.tree.heading('No. of Days', text='No. of Days')
        self.tree.heading('Room Number', text='Room Number')
        self.tree.heading('Suite Type', text='Suite Type')
        self.tree.heading('Price', text='Price')
        self.tree.place(x=200,y=250)

        # scrollbar for treeview
        self.scrollbar = ttk.Scrollbar(self, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.place(x=1385,y=250,anchor='nw')
        
        def close_win(holder):
            self.destroy()

        def display_info_msq(holder):
            if self.dis == True:
                con = sql.connect(host = 'localhost',user = 'root', password = 'tiger', database = 'hotel')
                cur = con.cursor()
                cur.execute("SELECT * FROM Hotel")
                c_list = cur.fetchall()
                if len(c_list) == 0:
                    c = ['All Rooms Empty','','','','']
                    self.tree.insert('', END, values=c)
                else:
                    for selected_item in self.tree.selection():
                        self.tree.delete(selected_item)
                    for c in c_list:
                        self.tree.insert('', END, values=c)
                    con.commit()
                con.close()
                self.dis = False
            elif self.dis == False:
                pass

        # create display button
        showinf = ImageTk.PhotoImage(file="show_info.png")
        self.showinf_l = Label(self, image=showinf)
        self.showinf_l.image = showinf;
        showinf_Button = my_canvas.create_image(200, 600, image=showinf, anchor = 'nw')
        my_canvas.tag_bind(showinf_Button, "<Button-1>", display_info_msq)

        # create home button
        home = ImageTk.PhotoImage(file="home.png")
        self.home_l = Label(self, image=home)
        self.home_l.image = home;
        home_Button = my_canvas.create_image(1070, 600, image=home, anchor = 'nw')
        my_canvas.tag_bind(home_Button, "<Button-1>", close_win)

# ABOUT UI ========================================================================================================================================================================================================
class About(Toplevel):
    def __init__(self, root):
        super().__init__(root)
        pad = 3
        self.title("About the program")
        self.geometry("1600x950")
        self.iconbitmap("palm.ico")

        # Creating Canvas
        my_canvas = Canvas(self, width = 1600, height = 950)
        my_canvas.pack(fill = 'both', expand = True)

        #Adding Background Image
        bg = ImageTk.PhotoImage(file="bg_2.jpg")
        self.back = Label(self)
        self.back.image = bg; # Adding a reference to the image so that it isn't deleted from memory during class instantiation.
        my_canvas.create_image(0,0, image = bg, anchor = 'nw')

        # Adding Title
        my_canvas.create_text(500, 5, text = "About The Program:", font = ("High Tower Text", 50), fill = "#006b56", anchor = "nw")

        my_canvas.create_text(50, 100, text = 'Hotel Management System is a program that keeps track of all your occupants, 24/7.', font = ("High Tower Text", 30), fill = "#006b56", anchor = "nw")
        my_canvas.create_text(50, 140, text = 'Seamlessly keep track of check-ins and check-outs from your hotel.', font = ("High Tower Text", 30), fill = "#006b56", anchor = "nw")
        my_canvas.create_text(50, 180, text = 'View all your occupants, the room they occupy and their details with just one click.', font = ("High Tower Text", 30), fill = "#006b56", anchor = "nw")
        my_canvas.create_text(50, 220, text = 'Light, fast and resourceful. The perfect companion for the urban hotel owner.', font = ("High Tower Text", 30), fill = "#006b56", anchor = "nw")

        my_canvas.create_text(150, 350, text = 'This Program Was Made By:', font = ("High Tower Text", 40, 'bold'), fill = "#006b56", anchor = "nw")
        my_canvas.create_text(250, 450, text = 'Abhishek', font = ("High Tower Text", 30), fill = "#006b56", anchor = "nw")
        
        def close_win(holder):
            self.destroy()

        # create home button
        home = ImageTk.PhotoImage(file="home.png")
        self.home_l = Label(self, image=home)
        self.home_l.image = home;
        home_Button = my_canvas.create_image(800, 500, image=home, anchor = 'nw')
        my_canvas.tag_bind(home_Button, "<Button-1>", close_win)

if __name__ == '__main__':
    main_ = Hotel()
    main_.mainloop()

