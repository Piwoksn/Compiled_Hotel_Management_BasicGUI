from tkinter import *

root = Tk()



#login Var
bgcolor1 = 'cornsilk2'
logo1 = PhotoImage(file='logo//plain_logo.png')
icon1 = PhotoImage('logo//venus_icon.ico')

#Register Var
bgcolor2 = 'cornsilk2'
logo2 = PhotoImage(file='logo//plain_logo.png')
icon2 = PhotoImage('logo//venus_icon.ico')


# Home Var
bgcolor3 = 'lightskyblue2'
menuColor3 = 'white'
logo3 = PhotoImage(file='200by100.png')
icon3 = PhotoImage('venus_icon.ico')
dashboard_icon3 = PhotoImage(file='dashbd.png')
sub3 = PhotoImage(file='sub.png')
setting3 = PhotoImage(file='setting.png')
acct3 = PhotoImage(file='money.png')
bar3 = PhotoImage(file='drink.png')
gym3 = PhotoImage(file='gym.png')
hr3 = PhotoImage(file='hr.png')
bed3 = PhotoImage(file='bed.png')
spoon3 = PhotoImage(file='spoon.png')
store3 = PhotoImage(file='store.png')
round3 = PhotoImage(file='dot.png')
plus3 = PhotoImage(file='plus.png')

#forget Password Var
bgcolor4 = 'cornsilk2'
logo4 = PhotoImage(file='logo//plain_logo.png')
icon4 = PhotoImage('logo//venus_icon.ico')

# Tax variables
bgcolor5 = 'lightskyblue2'
menuColor5 ='white'
logo5 = PhotoImage(file='200by100.png')
icon5 = PhotoImage('venus_icon.ico')
dashboard_icon5 = PhotoImage(file='dashbd.png')
sub5 = PhotoImage(file='sub.png')
setting5 = PhotoImage(file='setting.png')
acct5 = PhotoImage(file='money.png')
bar5 = PhotoImage(file='drink.png')
gym5 = PhotoImage(file='gym.png')
hr5 = PhotoImage(file='hr.png')
bed5 = PhotoImage(file='bed.png')
spoon5 = PhotoImage(file='spoon.png')
store5 = PhotoImage(file='store.png')
round5 = PhotoImage(file='dot.png')
plus5 = PhotoImage(file='plus.png')








class Portal:
    def __init__(self):
        menuFrame3 = Frame(root, bg=menuColor3)
        menuFrame3.grid(row=0, column=0)

        logoLabel3 = Label(menuFrame3, image=logo3, bg=menuColor3, compound='left')
        logoLabel3.grid(row=0, column=0, pady=20)

        mainNavLabel3 = Label(menuFrame3, text='MAIN NAVIGATION', bg=menuColor3, fg='gray', font=('arial', 12,),
                              width=25)
        mainNavLabel3.grid(row=1, column=0, sticky='w', pady=10)

        def backtohome():
            if self.tax():

                Portal.home(self)

        dashboardButton3 = Button(menuFrame3, text='Dashboard', font=('arial', 15,), bd=0,
                                  image=dashboard_icon3,
                                  compound='left',
                                  bg=menuColor3,
                                  pady=15,
                                  padx=20,
                                  activebackground=menuColor3,
                                  command=backtohome)
        dashboardButton3.grid(row=2, column=0, sticky='w')

        # space
        space3 = Label(menuFrame3, bg=menuColor3).grid(row=3, column=0, pady=10)
        # ---------------------------

        acctLabel3 = Label(menuFrame3, text='Account & Settings', bg=menuColor3, fg='gray', font=('arial', 12,),
                           pady=15,
                           padx=20,
                           )
        acctLabel3.grid(row=4, column=0, sticky='w')

        subButton3 = Button(menuFrame3, text='Subscription History', font=('arial', 15,), bd=0,
                            image=sub3,
                            compound='left',
                            bg=menuColor3,
                            pady=2,
                            padx=20,
                            activebackground=menuColor3,
                            )
        subButton3.grid(row=5, column=0, sticky='w')

        newsubButton3 = Button(menuFrame3, text='New Subscription', font=('arial', 15,), bd=0,
                               image=plus3,
                               compound='left',
                               bg=menuColor3,
                               pady=15,
                               padx=20,
                               activebackground=menuColor3, )
        newsubButton3.grid(row=6, column=0, sticky='w')

        settingLabel3 = Label(menuFrame3, text='Settings', font=('arial', 12,), bd=0,
                              compound='left',
                              bg=menuColor3,
                              pady=15,
                              padx=20,
                              fg='gray')
        settingLabel3.grid(row=7, column=0, sticky='w')

        propertyInformationButton3 = Button(menuFrame3, text='Property Information', font=('arial', 15,), bd=0,
                                            image=round3,
                                            compound='left',
                                            bg=menuColor3,
                                            pady=2,
                                            padx=20,
                                            activebackground=menuColor3,
                                            )
        propertyInformationButton3.grid(row=8, column=0, sticky='w')

        def bcktotax():
            #created a coordinate for the returned variables
            if Portal.home(self):
                Portal.home(self)
                Portal.tax(self)


        taxesButton3 = Button(menuFrame3, text='Taxes', font=('arial', 15,), bd=0,
                              image=round3,
                              compound='left',
                              bg=menuColor3,
                              pady=2,
                              padx=20,
                              activebackground=menuColor3,
                              command= bcktotax
                              )
        taxesButton3.grid(row=9, column=0, sticky='w')

        logoutButton3 = Button(menuFrame3, text='Logout', font=('arial', 15,), bd=0,
                               compound='left',
                               bg='red',
                               fg='white',
                               pady=5,
                               padx=15,
                               activebackground='red',
                               )
        logoutButton3.grid(row=10, column=0, pady=50)

        # space
        space3 = Label(menuFrame3, bg=menuColor3).grid(row=11, column=0, pady=200
                                                       )
        # ---------------------------

    def home(self):
            Portal.__init__(self)
            root.geometry('1270x685')
            root.minsize(width=1270, height=685)
            root.title('Venus')
            root.iconbitmap(icon3)
            root.config(bg=bgcolor3)


            #Menu


            #Item Dashboard MainFrame

            itemsFrame3 = Frame(root, bg= bgcolor3)
            itemsFrame3.grid(row=0, column=1, padx=15, pady=30, sticky='n',)

            #----------------

            #account
            acctFrame3 = Frame(itemsFrame3, bg=bgcolor3)
            acctFrame3.grid(row=0, column=0)
            acctbutton3 = Button(acctFrame3, text= 'account',
                                font=('arial', 15),
                                image= acct3,
                                compound='bottom',
                                bg='white',
                                pady= 10,
                              padx=30,
                              bd=0,
                              width=120,
                              height=150)
            acctbutton3.grid(row=0, column=0, padx=15)
            acctbuttonLabel3 = Label(acctFrame3, text='Enabled',
                                    bg='light green',
                                    fg='white',
                                    padx=40,
                                    width= 14)
            acctbuttonLabel3.grid(row=1, column=0)


            #bar
            barFrame3 = Frame(itemsFrame3, bg=bgcolor3)
            barFrame3.grid(row=0, column=1)
            barbutton3 = Button(barFrame3, text= 'bar',
                                font=('arial', 15),
                                image= bar3,
                                compound='bottom',
                                bg='white',
                                pady= 10,
                               padx=30,
                               bd=0,
                               width=120,
                               height=150)
            barbutton3.grid(row=0, column=0, padx=15)
            barbuttonLabel3 = Label(barFrame3, text='Enabled',
                                    bg='lightgreen',
                                    fg='white',
                                    padx=40,
                                    width= 14)
            barbuttonLabel3.grid(row=1, column=0,)


            #gym
            gymFrame3 = Frame(itemsFrame3, bg=bgcolor3)
            gymFrame3.grid(row=0, column=2)
            gymbutton3 = Button(gymFrame3, text= 'gym',
                                font=('arial', 15),
                                image= gym3,
                                compound='bottom',
                                bg='white',
                                pady= 10,
                                padx=30,
                                bd=0,
                               width=120,
                               height=150)
            gymbutton3.grid(row=0, column=0, padx=15)
            gymbuttonLabel3 = Label(gymFrame3, text='Disabled',
                                    bg='light goldenrod',
                                    fg='white',
                                    padx=40,
                                    width= 14)
            gymbuttonLabel3.grid(row=1, column=0,)



            #hr
            hrFrame3 = Frame(itemsFrame3, bg=bgcolor3)
            hrFrame3.grid(row=0, column=3)
            hrbutton3 = Button(hrFrame3, text= 'hr',
                                font=('arial', 15),
                                image= hr3,
                                compound='bottom',
                                bg='white',
                                pady= 10,
                              padx=30,
                              bd=0,
                              width=120,
                              height=150)
            hrbutton3.grid(row=0, column=0, padx=15)
            hrbuttonLabel3 = Label(hrFrame3, text='Disabled',
                                    bg='light goldenrod',
                                    fg='white',
                                    padx=40,
                                    width= 14)
            hrbuttonLabel3.grid(row=1, column=0,)



            #reservation
            reservationFrame3 = Frame(itemsFrame3, bg=bgcolor3)
            reservationFrame3.grid(row=0, column=4)
            reservationbutton3 = Button(reservationFrame3, text= 'reservation',
                                font=('arial', 15),
                                image= bed3,
                                compound='bottom',
                                bg='white',
                                pady= 10,
                              padx=30,
                              bd=0,
                              width=120,
                              height=150)
            reservationbutton3.grid(row=0, column=0, padx=15)
            reservationbuttonLabel3 = Label(reservationFrame3, text='Enabled',
                                    bg='light green',
                                    fg='white',
                                    padx=40,
                                    width= 14)
            reservationbuttonLabel3.grid(row=1, column=0,)


            #space
            space3 = Label(itemsFrame3, bg=bgcolor3).grid(row=1, column=0, pady=0)
            #-----------

            #restaurant
            restaurantFrame3 = Frame(itemsFrame3, bg=bgcolor3)
            restaurantFrame3.grid(row=2, column=0)
            restaurantbutton3 = Button(restaurantFrame3, text= 'restaurant',
                                font=('arial', 15),
                                image= spoon3,
                                compound='bottom',
                                bg='white',
                                pady= 10,
                              padx=30,
                              bd=0,
                              width=120,
                              height=150)
            restaurantbutton3.grid(row=0, column=0, padx=15)
            restaurantbuttonLabel3 = Label(restaurantFrame3, text='Enabled',
                                    bg='light green',
                                    fg='white',
                                    padx=40,
                                    width= 14)
            restaurantbuttonLabel3.grid(row=1, column=0,)


            #store
            storeFrame3 = Frame(itemsFrame3, bg=bgcolor3)
            storeFrame3.grid(row=2, column=1)
            storebutton3 = Button(storeFrame3, text= 'store',
                                font=('arial', 15),
                                image= store3,
                                compound='bottom',
                                bg='white',
                                pady= 10,
                              padx=30,
                              bd=0,
                              width=120,
                              height=150)
            storebutton3.grid(row=0, column=0, padx=15)
            storebuttonLabel3 = Label(storeFrame3, text='Enabled',
                                    bg='light green',
                                    fg='white',
                                    padx=40,
                                    width= 14)
            storebuttonLabel3.grid(row=1, column=0,
                                   )
            return acctFrame3,acctbuttonLabel3,barFrame3,barbuttonLabel3,\
                barbutton3,gymFrame3,gymbuttonLabel3,gymbutton3,hrFrame3,hrbuttonLabel3,hrbutton3,\
                reservationFrame3,reservationbuttonLabel3,reservationbutton3,restaurantFrame3,\
                restaurantbuttonLabel3,restaurantbutton3,storeFrame3,storebuttonLabel3,storebutton3

    def tax(self):
        Portal.__init__(self)


        def add5():
            if addtaxEntry5.get() != '':
                alltaxList5.insert(len(alltaxList5.get(0, END)),
                                   addtaxEntry5.get() + '  --  ' + ratetaxEntry5.get() + '%')
                # alltaxList.config(height=alltaxList.size())

                addtaxEntry5.delete(0, END)
                ratetaxEntry5.delete(0, END)
            else:
                pass

        def delete5():
            for index in reversed(alltaxList5.curselection()):
                alltaxList5.delete(index)
                # alltaxList.config(height=alltaxList.size())

        root.geometry('1270x685')
        root.minsize(width=1270, height=685)
        root.title('Venus')
        root.iconbitmap(icon5)
        root.config(bg=bgcolor5)

        # Menu


        # Item Dashboard MainFrame

        itemsFrame3 = Frame(root, bg=bgcolor5, )
        itemsFrame3.grid(row=0, columnspan=2, padx=20, pady=10, sticky='n',)

        taxLabel5 = Label(itemsFrame3, text='Taxes', font=('Arial', 20, 'bold'), bg=bgcolor5)
        taxLabel5.grid(row=0, column=0, pady=10, sticky='w')

        # alltax
        alltaxLabel5 = LabelFrame(itemsFrame3, text='All Taxes', font=('times new roman', 12), bg=bgcolor5, width=100)
        alltaxLabel5.grid(row=1, column=0, padx=20)

        scrollbar5 = Scrollbar(alltaxLabel5, orient=VERTICAL,
                               )
        scrollbar5.pack(side=RIGHT, fill=Y, pady=10)

        alltaxList5 = Listbox(alltaxLabel5, font=('arial', 15),
                              width=50,
                              height=20,
                              selectmode=MULTIPLE,
                              yscrollcommand=scrollbar5.set)
        alltaxList5.pack(pady=10, side=LEFT)

        scrollbar5.config(command=alltaxList5.yview)

        # addtax
        addtaxLabel5 = LabelFrame(itemsFrame3, text='Add Tax', font=('times new roman', 12), bg=bgcolor5)
        addtaxLabel5.grid(row=1, column=1, sticky='n')

        taxnameLabel5 = Label(addtaxLabel5, text='Tax Name', bg=bgcolor5, font=('times new roman', 15,))
        taxnameLabel5.grid(row=0, column=0, sticky='w', pady=5, padx=20)

        addtaxEntry5 = Entry(addtaxLabel5, font=('arial', 15), bd=5)
        addtaxEntry5.grid(row=1, column=0, padx=20)

        ratenameLabel5 = Label(addtaxLabel5, text='Rate (%)', bg=bgcolor5, font=('times new roman', 15,))
        ratenameLabel5.grid(row=2, column=0, sticky='w', pady=5, padx=20)

        ratetaxEntry5 = Entry(addtaxLabel5, font=('arial', 15), bd=5)
        ratetaxEntry5.grid(row=3, column=0, padx=20)

        addbutton5 = Button(addtaxLabel5, text='Add Tax', font=('arial', 15),
                            bg='blue',
                            fg='white',
                            activebackground='blue',
                            command=add5)
        addbutton5.grid(row=4, column=0, pady=10, padx=20, )

        deletebutton5 = Button(addtaxLabel5, text='Delete Tax', font=('arial', 15),
                               bg='orange',
                               fg='white',
                               activebackground='orange',
                               command=delete5)
        deletebutton5.grid(row=5, column=0, padx=10, pady=10)

        return itemsFrame3,taxLabel5,alltaxLabel5,scrollbar5,alltaxList5,addtaxLabel5,taxnameLabel5,addtaxEntry5,ratetaxEntry5,\
            ratenameLabel5,addbutton5,deletebutton5














home = Portal.home(True)
root.mainloop()
