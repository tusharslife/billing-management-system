from tkinter import *
import math,random,os
from tkinter import messagebox
import smtplib, ssl
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Store Billing System by Abhishek, Harsh and Abhinav")
        bg_color = "#224564"
        title = Label(self.root, text="Store Billing System by Abhishek, Harsh and Abhinav", bd=12, relief=GROOVE,
                      bg=bg_color, fg="white", font=("Monotype Corsiva", 30, "bold"), pady=2).pack(fill=X)
        #=====variables==========

        self.soap = IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.spray = IntVar()
        self.gell = IntVar()
        self.loshan = IntVar()
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()
        self.maza = IntVar()
        self.coke = IntVar()
        self.sugar = IntVar()
        self.frooti = IntVar()
        self.thumpsup = IntVar()
        self.limca = IntVar()
        self.sprite = IntVar()

        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drink_price = StringVar()

        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drink_tax = StringVar()

        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.c_mail = StringVar()

        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()

        #=============Customer Detail Frame=====

        F1 = LabelFrame(self.root, text="Customer Details", font=("times new roman", 15, "bold"), fg="gold",
                        bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)
        cname_lbl = Label(F1, text="Customer Name", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(
            row=0, column=0, padx=15, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font="arial 15", bd=7, relief=SUNKEN).grid(row=0,
                                                                                                             column=1,
                                                                                                             pady=5)

        cphn_lbl = Label(F1, text="Phone No.", bg=bg_color, fg="white",
                         font=("times new roman", 14, "bold")).grid(row=0, column=2, padx=15, pady=5)
        cphn_txt = Entry(F1, width=12, textvariable=self.c_phone, font="arial 15", bd=7, relief=SUNKEN).grid(row=0,
                                                                                                             column=3,
                                                                                                             pady=5)

        mail_lbl = Label(F1, text="Mail Id", bg=bg_color, fg="white",
                         font=("times new roman", 14, "bold")).grid(row=0, column=4, padx=15, pady=5)
        mail_txt = Entry(F1, width=20, textvariable=self.c_mail, font="arial 15", bd=7, relief=SUNKEN).grid(row=0,
                                                                                                            column=5,
                                                                                                            pady=5)

        c_bill_lbl = Label(F1, text="Bill Number", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(
            row=0, column=6, padx=15, pady=5)
        c_bill_txt = Entry(F1, width=6, textvariable=self.search_bill, font="arial 15", bd=7, relief=SUNKEN).grid(row=0,
                                                                                                                  column=7,
                                                                                                                  pady=5)

        bill_btn = Button(F1, text="Search", command=self.find_bill, width=8, bd=7, font="arial 10 bold").grid(row=0,
                                                                                                               column=8,
                                                                                                               padx=10,
                                                                                                               pady=10)
        #=================Cosmetics=================#

        F2 = LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=170,width=325,height=380)

        bath_lbl = Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="#96050C").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt = Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        face_cream_lbl = Label(F2, text="Face Cream", font=("times new roman", 16, "bold"), bg=bg_color, fg="#96050C").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        face_cream_txt = Entry(F2, width=10, textvariable=self.face_cream,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1,padx=10, pady=10)

        face_w_lbl = Label(F2, text="Face Wash", font=("times new roman", 16, "bold"), bg=bg_color, fg="#96050C").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        face_w__txt = Entry(F2, width=10,textvariable=self.face_wash, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1,padx=10, pady=10)

        Hair_s_lbl = Label(F2, text="Hair Spray", font=("times new roman", 16, "bold"), bg=bg_color,fg="#96050C").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        Hair_s__txt = Entry(F2, width=10, textvariable=self.spray,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        Hair_g_lbl = Label(F2, text="Hair Gel", font=("times new roman", 16, "bold"), bg=bg_color,fg="#96050C").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        Hair_g__txt = Entry(F2, width=10,textvariable=self.gell, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        Body_lbl = Label(F2, text="Body Loshan", font=("times new roman", 16, "bold"), bg=bg_color,fg="#96050C").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        Body__txt = Entry(F2, width=10, textvariable=self.loshan,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        # =================Grocery=================#

        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Grocery", font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F3.place(x=340, y=170, width=325, height=380)

        g1_lbl = Label(F3, text="Rice", font=("times new roman", 16, "bold"), bg=bg_color, fg="#96050C").grid(
            row=0, column=0, padx=10, pady=10, sticky="w")
        g1_txt = Entry(F3, width=10,textvariable=self.rice, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1,
                                                                                                       padx=10, pady=10)

        g2_lbl = Label(F3, text="Food Oil", font=("times new roman", 16, "bold"), bg=bg_color,
                               fg="#96050C").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        g2_txt = Entry(F3, width=10, textvariable=self.food_oil,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1,
                                                                                                             column=1,
                                                                                                             padx=10,
                                                                                                             pady=10)

        g3_lbl = Label(F3, text="Daal", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="#96050C").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        g3__txt = Entry(F3, width=10,textvariable=self.daal, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2,
                                                                                                          column=1,
                                                                                                          padx=10,
                                                                                                          pady=10)

        g4_lbl = Label(F3, text="Wheat", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="#96050C").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        g4__txt = Entry(F3, width=10, textvariable=self.wheat,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        g5_lbl = Label(F3, text="Sugar", font=("times new roman", 16, "bold"), bg=bg_color, fg="#96050C").grid(
            row=4, column=0, padx=10, pady=10, sticky="w")
        g5__txt = Entry(F3, width=10, textvariable=self.sugar,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4,
                                                                                                          column=1,
                                                                                                          padx=10,
                                                                                                          pady=10)

        g6 = Label(F3, text="Tea", font=("times new roman", 16, "bold"), bg=bg_color,
                         fg="#96050C").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        g6 = Entry(F3, width=10,textvariable=self.tea, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1,
                                                                                                        padx=10,
                                                                                                        pady=10)

        # =================Cold Drinks=================#

        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cold Drinks", font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F4.place(x=670, y=170, width=325, height=380)

        c1_lbl = Label(F4, text="Mazza", font=("times new roman", 16, "bold"), bg=bg_color, fg="#96050C").grid(
            row=0, column=0, padx=10, pady=10, sticky="w")
        c1_txt = Entry(F4, width=10, textvariable=self.maza,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1,
                                                                                                     padx=10, pady=10)

        c2_lbl = Label(F4, text="Coke", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="#96050C").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        c2_txt = Entry(F4, width=10,textvariable=self.coke, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1,
                                                                                                     column=1,
                                                                                                     padx=10,
                                                                                                     pady=10)

        c3_lbl = Label(F4, text="Frooti", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="#96050C").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        c3__txt = Entry(F4, width=10, textvariable=self.frooti,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2,
                                                                                                      column=1,
                                                                                                      padx=10,
                                                                                                      pady=10)

        c4_lbl = Label(F4, text="ThumbsUp", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="#96050C").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        c4__txt = Entry(F4, width=10, textvariable=self.thumpsup,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1,
                                                                                                      padx=10, pady=10)

        c5_lbl = Label(F4, text="Limca", font=("times new roman", 16, "bold"), bg=bg_color, fg="#96050C").grid(
            row=4, column=0, padx=10, pady=10, sticky="w")
        c5__txt = Entry(F4, width=10, textvariable=self.limca,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4,
                                                                                                      column=1,
                                                                                                      padx=10,
                                                                                                      pady=10)

        c6 = Label(F4, text="Sprite", font=("times new roman", 16, "bold"), bg=bg_color,
                   fg="#96050C").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        c6 = Entry(F4, width=10, textvariable=self.sprite,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1,
                                                                                                 padx=10,
                                                                                                 pady=10)

        #==========bill area===========

        F5 = Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=173,width=350,height=380)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #========buttonFrame==========

        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=140)
        m1_lbl = Label(F6,text="Total Cosmetic Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt = Entry(F6,width = 18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl = Label(F6, text="Total Grocery Price", bg=bg_color, fg="white",
                       font=("times new roman", 14, "bold")).grid(row=1, column=0, padx=20, pady=1, sticky="w")
        m2_txt = Entry(F6, width=18,textvariable=self.grocery_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        m3_lbl = Label(F6, text="Total Cold Drinks Price", bg=bg_color, fg="white",
                       font=("times new roman", 14, "bold")).grid(row=2, column=0, padx=20, pady=1, sticky="w")
        m3_txt = Entry(F6, width=18, textvariable=self.cold_drink_price,font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)

        c1_lbl = Label(F6, text="Cosmetic Tax", bg=bg_color, fg="white",
                       font=("times new roman", 14, "bold")).grid(row=0, column=2, padx=20, pady=1, sticky="w")
        c1_txt = Entry(F6, width=18, textvariable=self.cosmetic_tax,font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)

        c2_lbl = Label(F6, text="Grocery Tax", bg=bg_color, fg="white",
                       font=("times new roman", 14, "bold")).grid(row=1, column=2, padx=20, pady=1, sticky="w")
        c2_txt = Entry(F6, width=18, textvariable=self.grocery_tax,font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)

        c3_lbl = Label(F6, text="Cold Drinks Tax", bg=bg_color, fg="white",
                       font=("times new roman", 14, "bold")).grid(row=2, column=2, padx=20, pady=1, sticky="w")
        c3_txt = Entry(F6, width=18, textvariable=self.cold_drink_tax,font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)

        btn_F = Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=750,width=580,height=105)

        total_btn = Button(btn_F,command=self.total,text="Total",bg="#96050C",fg="white",pady=3,width=10,bd = 2 , font="arial 12 bold").grid(row=0,column=0,padx=5,pady=5)
        GBill_btn = Button(btn_F, text="Generate Bill", command=self.bill_area, bg="#96050C", fg="white", pady=3,
                           width=10, bd=2,
                           font="arial 12 bold").grid(row=0, column=1, padx=1, pady=1)
        Mail_btn = Button(btn_F, text="Send Mail", command=self.send_mail, bg="#96050C", fg="white", pady=3,
                          width=10, bd=2,
                          font="arial 12 bold").grid(row=0, column=3, padx=1, pady=1)
        Clear_btn = Button(btn_F, command=self.clear_data, text="Clear", bg="#96050C", fg="white", pady=3, width=10,
                           bd=2,
                           font="arial 12 bold").grid(row=0, column=2, padx=1, pady=1)

        Exit_btn = Button(btn_F, command=self.Exit_app, text="Exit", bg="#96050C", fg="white", pady=3, width=10, bd=2,
                          font="arial 12 bold").grid(row=0, column=4, padx=1, pady=1)
        self.welcome_bill()


    def total(self):
        self.c_s_p = self.soap.get() * 40
        self.c_fc_p = self.face_cream.get() * 120
        self.c_fw_p = self.face_wash.get() * 60
        self.c_hs_p = self.spray.get() * 180
        self.c_hg_p = self.gell.get() * 140
        self.c_bl_p = self.loshan.get() * 180
        self.total_cosmetic_price = float(self.c_s_p+self.c_fc_p+self.c_fw_p+self.c_hs_p+self.c_hg_p+self.c_bl_p)
        self.cosmetic_price.set("Rs. " + str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("Rs. " +  str(self.c_tax))

        self.g_r_p = self.rice.get()*40
        self.g_f_p = self.food_oil.get() * 180
        self.g_d_p = self.daal.get() * 60
        self.g_w_p = self.wheat.get() * 240
        self.g_s_p = self.sugar.get() * 45
        self.g_t_p = self.tea.get() * 150

        self.total_grocery_price = float(
            self.g_r_p +
            self.g_f_p +
            self.g_d_p +
            self.g_w_p +
            self.g_s_p +
            self.g_t_p
            )
        self.grocery_price.set("Rs. " + str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price * 0.1), 2)
        self.grocery_tax.set("Rs. " + str(self.g_tax))

        self.d_m_p = self.maza.get() * 60
        self.d_c_p = self.coke.get() * 60
        self.d_f_p = self.frooti.get() * 50
        self.d_t_p = self.thumpsup.get() * 45
        self.d_l_p = self.limca.get() * 40
        self.d_s_p = self.sprite.get() * 60
        self.total_drinks_price = float(
            self.d_m_p +
            self.d_c_p +
            self.d_f_p +
            self.d_t_p +
            self.d_l_p +
            self.d_s_p
        )
        self.cold_drink_price.set("Rs. " + str(self.total_drinks_price))
        self.d_tax=round((self.total_drinks_price * 0.1), 2)
        self.cold_drink_tax.set("Rs. " + str(self.d_tax))

        self.Total_bill = float(self.total_cosmetic_price+self.total_drinks_price+self.total_grocery_price+self.c_tax+self.g_tax+self.d_tax)

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone Number:{self.c_phone.get()}")
        self.txtarea.insert(END,f"\n Email:{self.c_mail.get()}")
        self.txtarea.insert(END,f"\n =====================================")
        self.txtarea.insert(END,f"\n Products\t\tQTY\t\tPrice")
        self.txtarea.insert(END,f"\n =====================================")

    def send_mail(self):

            if re.fullmatch(regex, self.c_mail.get()) or  self.c_phone.get()=="":
                port = 465  # For SSL
                smtp_server = "smtp.gmail.com"
                sender_email = "[YOUR MAIL ID]"
                receiver_email = self.c_mail.get()
                password = "[YOUR PASSWORD]"
                message = 'Subject: {}\n\n{}'.format("Store Billing System Payment Details",
                                                     self.txtarea.get(1.0, "end").strip())

                try:
                    context = ssl.create_default_context()
                    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                        server.login(sender_email, password)
                        server.sendmail(sender_email, receiver_email, message)
                    messagebox.showinfo("Success", "Email Send Successfully")

                except smtplib.SMTPException:
                    messagebox.showerror("Error", "Unable To Send Email")

            else:
                messagebox.showerror("Error", "Invalid Email")





    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Customer Details Are Must")
        elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_drink_price.get()=="Rs. 0.0":
            messagebox.showerror("Error", "No Product Purchased")
        else:
            self.welcome_bill()
            #===cosmetic======
            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
            if self.face_cream.get()!=0:
                self.txtarea.insert(END,f"\n Face Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")

            if self.face_wash.get()!=0:
                self.txtarea.insert(END,f"\n Face Wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
            if self.spray.get()!=0:
                self.txtarea.insert(END,f"\n Spray\t\t{self.spray.get()}\t\t{self.c_hs_p}")
            if self.gell.get()!=0:
                self.txtarea.insert(END,f"\n Hair Gell\t\t{self.gell.get()}\t\t{self.c_hg_p}")
            if self.loshan.get()!=0:
                self.txtarea.insert(END,f"\n Body Loshan\t\t{self.loshan.get()}\t\t{self.c_bl_p}")

            # ===grocery======
            if self.rice.get() != 0:
                self.txtarea.insert(END, f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
            if self.food_oil.get() != 0:
                self.txtarea.insert(END, f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_f_p}")
            if self.daal.get() != 0:
                self.txtarea.insert(END, f"\n Daal\t\t{self.daal.get()}\t\t{self.g_d_p}")
            if self.wheat.get() != 0:
                self.txtarea.insert(END, f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")
            if self.sugar.get() != 0:
                self.txtarea.insert(END, f"\n Sugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")
            if self.tea.get() != 0:
                self.txtarea.insert(END, f"\n Tea\t\t{self.tea.get()}\t\t{self.g_t_p}")

            # ====cold drinks====
            if self.maza.get() != 0:
                self.txtarea.insert(END, f"\n Maza\t\t{self.maza.get()}\t\t{self.d_m_p}")
            if self.coke.get() != 0:
                self.txtarea.insert(END, f"\n Coke\t\t{self.coke.get()}\t\t{self.d_c_p}")
            if self.frooti.get() != 0:
                self.txtarea.insert(END, f"\n Frooti\t\t{self.frooti.get()}\t\t{self.d_f_p}")
            if self.thumpsup.get() != 0:
                self.txtarea.insert(END, f"\n Thumps Up\t\t{self.thumpsup.get()}\t\t{self.d_t_p}")
            if self.limca.get() != 0:
                self.txtarea.insert(END, f"\n Limca\t\t{self.limca.get()}\t\t{self.d_l_p}")
            if self.sprite.get() != 0:
                self.txtarea.insert(END, f"\n Sprite\t\t{self.sprite.get()}\t\t{self.d_s_p}")

            self.txtarea.insert(END,f"\n-----------------------------------")
            if self.cosmetic_tax.get() !="Rs. 0.0":
                self.txtarea.insert(END, f"\n Cosmetic Tax\t\t{self.cosmetic_tax.get()}")
            if self.grocery_tax.get() !="Rs. 0.0":
                self.txtarea.insert(END, f"\n Grocery Tax\t\t{self.grocery_tax.get()}")
            if self.cold_drink_tax.get() !="Rs. 0.0":
                self.txtarea.insert(END, f"\n Cold Drink Tax\t\t{self.cold_drink_tax.get()}")

            self.txtarea.insert(END,f"\nTotal Bill : \t\t\t Rs. {str(self.Total_bill)}")
            self.txtarea.insert(END, f"\n-----------------------------------")
            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do You Want Save The Bill")
        if op>0:
            self.bill_data = self.txtarea.get('1.0',END)
            f1 = open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill No. : {self.bill_no.get()} Saved SuccessFully")
        else:
            return

    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1 = open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No.")

    def clear_data(self):
        self.soap.set(0)
        self.face_cream.set(0)
        self.face_wash.set(0)
        self.spray.set(0)
        self.gell.set(0)
        self.loshan.set(0)
        self.rice.set(0)
        self.food_oil.set(0)
        self.daal.set(0)
        self.wheat.set(0)
        self.sugar.set(0)
        self.tea.set(0)
        self.maza.set(0)
        self.coke.set(0)
        self.frooti.set(0)
        self.thumpsup.set(0)
        self.limca.set(0)
        self.sprite.set(0)

        self.cosmetic_price.set("")
        self.grocery_price.set("")
        self.cold_drink_price.set("")

        self.cosmetic_tax.set("")
        self.grocery_tax.set("")
        self.cold_drink_tax.set("")

        self.c_name.set("")
        self.c_phone.set("")
        self.c_mail.set("")
        self.bill_no.set("")
        x = random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.welcome_bill()

    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()

root=Tk()
obj=Bill_App(root)
root.mainloop()