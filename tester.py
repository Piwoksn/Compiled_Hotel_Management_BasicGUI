from tkinter import *

root = Tk()

#variables

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




#Main func
def login():

    #functions
    def tax():


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

        itemsFrame3 = Frame(root, bg=bgcolor5)
        itemsFrame3.grid(row=0, column=1, padx=20, pady=10, sticky='n')

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




    def forgotpwd():
        frame1.destroy()
        iconLabel1.destroy()
        loginLabel1.destroy()
        loginframe1.destroy()
        emailLabel1.destroy()
        emailEntry1.destroy()
        passwordLabel1.destroy()
        passwordEntry1.destroy()
        check1.destroy()
        forgotpwdButton1.destroy()
        loginButton1.destroy()
        registerButton1.destroy()

        root.geometry('1270x685')
        root.minsize(width=900, height=600)
        root.title('Venus')
        root.iconbitmap(icon4)
        root.config(bg=bgcolor4)

        frame14 = Frame(root, bg=bgcolor4)
        frame14.pack(fill=X)

        iconLabel4 = Label(frame14,
                           bg=bgcolor4,
                           image=logo4)
        iconLabel4.pack(pady=10)

        loginframe4 = Frame(root,
                            bg='white')
        loginframe4.pack(anchor='center')

        loginLabel4 = LabelFrame(loginframe4, text='Forgot Password', font=('arial', 10),
                                 bg='white',
                                 )
        loginLabel4.pack(fill=X, pady=10, padx=10)

        emailLabel4 = Label(loginLabel4, text='Email', font=('times new roman', 15),
                            bg='white')
        emailLabel4.grid(row=0, column=0, padx=100, sticky='w')

        emailEntry4 = Entry(loginLabel4, font=('arial', 20), bd=6, width=25)
        emailEntry4.grid(row=1, column=0, pady=10, padx=100)

        requestpwdButton4 = Button(loginLabel4, text='Request Password Reset',
                              font=('times new roman', 15),
                              bg='blue',
                              fg='white',
                              activebackground='blue')
        requestpwdButton4.grid(row=6, column=0, pady=10)

        def bcklogin():
            loginButton4.destroy()
            requestpwdButton4.destroy()
            emailEntry4.destroy()
            emailLabel4.destroy()
            loginLabel4.destroy()
            loginframe4.destroy()
            iconLabel4.destroy()
            frame14.destroy()
            login()

        loginButton4 = Button(loginframe4, text='back to login',
                                 font=('times new roman', 15, 'bold'),
                                 bd=0,
                                 command=bcklogin)
        loginButton4.pack(fill=X)

    #home function -------------------------------------------------
    def home():
        frame1.destroy()
        iconLabel1.destroy()
        loginLabel1.destroy()
        loginframe1.destroy()
        emailLabel1.destroy()
        emailEntry1.destroy()
        passwordLabel1.destroy()
        passwordEntry1.destroy()
        check1.destroy()
        forgotpwdButton1.destroy()
        loginButton1.destroy()
        registerButton1.destroy()



        root.geometry('1270x685')
        root.minsize(width=1270, height=685)
        root.title('Venus')
        root.iconbitmap(icon3)
        root.config(bg=bgcolor3)

        # Menu
        menuFrame3 = Frame(root, bg=menuColor3)
        menuFrame3.grid(row=0, column=0)

        logoLabel3 = Label(menuFrame3, image=logo3, bg=menuColor3, compound='left')
        logoLabel3.grid(row=0, column=0, pady=20)

        mainNavLabel3 = Label(menuFrame3, text='MAIN NAVIGATION', bg=menuColor3, fg='gray', font=('arial', 12,),
                              width=25)
        mainNavLabel3.grid(row=1, column=0, sticky='w', pady=10)

        dashboardButton3 = Button(menuFrame3, text='Dashboard', font=('arial', 15,), bd=0,
                                  image=dashboard_icon3,
                                  compound='left',
                                  bg=menuColor3,
                                  pady=15,
                                  padx=20,
                                  activebackground=menuColor3)
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

        def tx():
            #logoutButton3.destroy()
            #taxesButton3.destroy()
            #propertyInformationButton3.destroy()
            #settingLabel3.destroy()
            #newsubButton3.destroy()
            #subButton3.destroy()
            #acctLabel3.destroy()
            #dashboardButton3.destroy()
            #mainNavLabel3.destroy()
            #logoLabel3.destroy()
            #menuFrame3.destroy()
            #itemsFrame3.destroy()
            acctFrame3.destroy()
            acctbuttonLabel3.destroy()
            acctbuttonLabel3.destroy()
            barFrame3.destroy()
            barbuttonLabel3.destroy()
            barbutton3.destroy()
            gymFrame3.destroy()
            gymbuttonLabel3.destroy()
            gymbutton3.destroy()
            hrFrame3.destroy()
            hrbuttonLabel3.destroy()
            hrbutton3.destroy()
            reservationFrame3.destroy()
            reservationbuttonLabel3.destroy()
            reservationbutton3.destroy()
            restaurantFrame3.destroy()
            restaurantbuttonLabel3.destroy()
            restaurantbutton3.destroy()
            storeFrame3.destroy()
            storebuttonLabel3.destroy()
            storebutton3.destroy()

            tax()

        taxesButton3 = Button(menuFrame3, text='Taxes', font=('arial', 15,), bd=0,
                              image=round3,
                              compound='left',
                              bg=menuColor3,
                              pady=2,
                              padx=20,
                              activebackground=menuColor3,
                              command= tx)
        taxesButton3.grid(row=9, column=0, sticky='w')

        #logout--------------------------------------------------
        def backlogin():
            #Home
            logoutButton3.destroy()
            taxesButton3.destroy()
            propertyInformationButton3.destroy()
            settingLabel3.destroy()
            newsubButton3.destroy()
            subButton3.destroy()
            acctLabel3.destroy()
            dashboardButton3.destroy()
            mainNavLabel3.destroy()
            logoLabel3.destroy()
            menuFrame3.destroy()
            itemsFrame3.destroy()
            acctFrame3.destroy()
            acctbuttonLabel3.destroy()
            acctbuttonLabel3.destroy()
            barFrame3.destroy()
            barbuttonLabel3.destroy()
            barbutton3.destroy()
            gymFrame3.destroy()
            gymbuttonLabel3.destroy()
            gymbutton3.destroy()
            hrFrame3.destroy()
            hrbuttonLabel3.destroy()
            hrbutton3.destroy()
            reservationFrame3.destroy()
            reservationbuttonLabel3.destroy()
            reservationbutton3.destroy()
            restaurantFrame3.destroy()
            restaurantbuttonLabel3.destroy()
            restaurantbutton3.destroy()
            storeFrame3.destroy()
            storebuttonLabel3.destroy()
            storebutton3.destroy()





            login()





        logoutButton3 = Button(menuFrame3, text='Logout', font=('arial', 15,), bd=0,
                               compound='left',
                               bg='red',
                               fg='white',
                               pady=5,
                               padx=15,
                               activebackground='red',
                               command= backlogin)
        logoutButton3.grid(row=10, column=0, pady=50)

        # space
        space3 = Label(menuFrame3, bg=menuColor3).grid(row=11, column=0, pady=200
                                                       )
        # ---------------------------

        # Item Dashboard MainFrame

        itemsFrame3 = Frame(root, bg=bgcolor3)
        itemsFrame3.grid(row=0, column=1, padx=15, pady=30, sticky='n')

        # ----------------

        # account
        acctFrame3 = Frame(itemsFrame3, bg=bgcolor3)
        acctFrame3.grid(row=0, column=0)
        acctbutton3 = Button(acctFrame3, text='account',
                             font=('arial', 15),
                             image=acct3,
                             compound='bottom',
                             bg='white',
                             pady=10,
                             padx=30,
                             bd=0,
                             width=120,
                             height=150)
        acctbutton3.grid(row=0, column=0, padx=15)
        acctbuttonLabel3 = Label(acctFrame3, text='Enabled',
                                 bg='light green',
                                 fg='white',
                                 padx=40,
                                 width=14)
        acctbuttonLabel3.grid(row=1, column=0)

        # bar
        barFrame3 = Frame(itemsFrame3, bg=bgcolor3)
        barFrame3.grid(row=0, column=1)
        barbutton3 = Button(barFrame3, text='bar',
                            font=('arial', 15),
                            image=bar3,
                            compound='bottom',
                            bg='white',
                            pady=10,
                            padx=30,
                            bd=0,
                            width=120,
                            height=150)
        barbutton3.grid(row=0, column=0, padx=15)
        barbuttonLabel3 = Label(barFrame3, text='Enabled',
                                bg='lightgreen',
                                fg='white',
                                padx=40,
                                width=14)
        barbuttonLabel3.grid(row=1, column=0, )

        # gym
        gymFrame3 = Frame(itemsFrame3, bg=bgcolor3)
        gymFrame3.grid(row=0, column=2)
        gymbutton3 = Button(gymFrame3, text='gym',
                            font=('arial', 15),
                            image=gym3,
                            compound='bottom',
                            bg='white',
                            pady=10,
                            padx=30,
                            bd=0,
                            width=120,
                            height=150)
        gymbutton3.grid(row=0, column=0, padx=15)
        gymbuttonLabel3 = Label(gymFrame3, text='Disabled',
                                bg='light goldenrod',
                                fg='white',
                                padx=40,
                                width=14)
        gymbuttonLabel3.grid(row=1, column=0, )

        # hr
        hrFrame3 = Frame(itemsFrame3, bg=bgcolor3)
        hrFrame3.grid(row=0, column=3)
        hrbutton3 = Button(hrFrame3, text='hr',
                           font=('arial', 15),
                           image=hr3,
                           compound='bottom',
                           bg='white',
                           pady=10,
                           padx=30,
                           bd=0,
                           width=120,
                           height=150)
        hrbutton3.grid(row=0, column=0, padx=15)
        hrbuttonLabel3 = Label(hrFrame3, text='Disabled',
                               bg='light goldenrod',
                               fg='white',
                               padx=40,
                               width=14)
        hrbuttonLabel3.grid(row=1, column=0, )

        # reservation
        reservationFrame3 = Frame(itemsFrame3, bg=bgcolor3)
        reservationFrame3.grid(row=0, column=4)
        reservationbutton3 = Button(reservationFrame3, text='reservation',
                                    font=('arial', 15),
                                    image=bed3,
                                    compound='bottom',
                                    bg='white',
                                    pady=10,
                                    padx=30,
                                    bd=0,
                                    width=120,
                                    height=150)
        reservationbutton3.grid(row=0, column=0, padx=15)
        reservationbuttonLabel3 = Label(reservationFrame3, text='Enabled',
                                        bg='light green',
                                        fg='white',
                                        padx=40,
                                        width=14)
        reservationbuttonLabel3.grid(row=1, column=0, )

        # space
        space3 = Label(itemsFrame3, bg=bgcolor3).grid(row=1, column=0, pady=0)
        # -----------

        # restaurant
        restaurantFrame3 = Frame(itemsFrame3, bg=bgcolor3)
        restaurantFrame3.grid(row=2, column=0)
        restaurantbutton3 = Button(restaurantFrame3, text='restaurant',
                                   font=('arial', 15),
                                   image=spoon3,
                                   compound='bottom',
                                   bg='white',
                                   pady=10,
                                   padx=30,
                                   bd=0,
                                   width=120,
                                   height=150)
        restaurantbutton3.grid(row=0, column=0, padx=15)
        restaurantbuttonLabel3 = Label(restaurantFrame3, text='Enabled',
                                       bg='light green',
                                       fg='white',
                                       padx=40,
                                       width=14)
        restaurantbuttonLabel3.grid(row=1, column=0, )

        # store
        storeFrame3 = Frame(itemsFrame3, bg=bgcolor3)
        storeFrame3.grid(row=2, column=1)
        storebutton3 = Button(storeFrame3, text='store',
                              font=('arial', 15),
                              image=store3,
                              compound='bottom',
                              bg='white',
                              pady=10,
                              padx=30,
                              bd=0,
                              width=120,
                              height=150)
        storebutton3.grid(row=0, column=0, padx=15)
        storebuttonLabel3 = Label(storeFrame3, text='Enabled',
                                  bg='light green',
                                  fg='white',
                                  padx=40,
                                  width=14)
        storebuttonLabel3.grid(row=1, column=0, )

    #REgister Function ---------------------------------------------------
    def register():
        frame1.destroy()
        iconLabel1.destroy()
        loginLabel1.destroy()
        loginframe1.destroy()
        emailLabel1.destroy()
        emailEntry1.destroy()
        passwordLabel1.destroy()
        passwordEntry1.destroy()
        check1.destroy()
        forgotpwdButton1.destroy()
        loginButton1.destroy()
        registerButton1.destroy()


        root.geometry('1270x685')
        root.minsize(width=900, height=600)
        root.title('Venus')
        root.iconbitmap(icon2)
        root.config(bg=bgcolor2)

        logoLabel2 = Label(root, image=logo2, bg=bgcolor2)
        logoLabel2.pack(pady=10, fill=X)

        frame2 = Frame(root, bg='white')
        frame2.pack()

        labelFrame2 = LabelFrame(frame2, text='Create Your Account', bg='white', font=('arial', 10))
        labelFrame2.pack(pady=10, padx=10)

        hotelNameLabel2 = Label(labelFrame2, text='Hotel Name', font=('times new roman', 15),
                                bg='white')
        hotelNameLabel2.grid(row=0, column=0, padx=10, sticky='w')

        hotelNameEntry2 = Entry(labelFrame2, font=('arial', 20, 'bold'), bd=6, )
        hotelNameEntry2.grid(row=1, column=0, pady=10, padx=10)

        phoneNumberLabel2 = Label(labelFrame2, text='Phone Number', font=('times new roman', 15),
                                  bg='white')
        phoneNumberLabel2.grid(row=2, column=0, padx=10, sticky='w')

        phoneNumberEntry2 = Entry(labelFrame2, font=('arial', 20), bd=6, )
        phoneNumberEntry2.grid(row=3, column=0, pady=10, padx=10)

        passwordLabel2 = Label(labelFrame2, text='Password', font=('times new roman', 15),
                               bg='white')
        passwordLabel2.grid(row=4, column=0, padx=10, sticky='w')

        passwordEntry2 = Entry(labelFrame2, font=('arial', 20), bd=6, )
        passwordEntry2.grid(row=5, column=0, pady=10, padx=10)

        contactPersonLabel2 = Label(labelFrame2, text='Contact Person', font=('times new roman', 15),
                                    bg='white')
        contactPersonLabel2.grid(row=0, column=1, padx=10, sticky='w')

        contactPersonEntry2 = Entry(labelFrame2, font=('arial', 20), bd=6, )
        contactPersonEntry2.grid(row=1, column=1, pady=10, padx=10)

        emailLabel2 = Label(labelFrame2, text='Email', font=('times new roman', 15),
                            bg='white')
        emailLabel2.grid(row=2, column=1, padx=10, sticky='w')

        emailEntry2 = Entry(labelFrame2, font=('arial', 20), bd=6, )
        emailEntry2.grid(row=3, column=1, pady=10, padx=10)

        noOfRoomsLabel2 = Label(labelFrame2, text='Number of Rooms', font=('times new roman', 15),
                                bg='white')
        noOfRoomsLabel2.grid(row=4, column=1, padx=10, sticky='w')

        noOfRoomsEntry2 = Entry(labelFrame2, font=('arial', 20, 'bold'), bd=6, )
        noOfRoomsEntry2.grid(row=5, column=1, pady=10, padx=10)

        #taking to HOME-----------------------------------
        def gotohome():
            createAccountButton2.destroy()
            noOfRoomsEntry2.destroy()
            noOfRoomsLabel2.destroy()
            emailEntry2.destroy()
            emailLabel2.destroy()
            contactPersonEntry2.destroy()
            contactPersonLabel2.destroy()
            passwordEntry2.destroy()
            passwordLabel2.destroy()
            phoneNumberEntry2.destroy()
            phoneNumberLabel2.destroy()
            hotelNameEntry2.destroy()
            hotelNameLabel2.destroy()
            labelFrame2.destroy()
            frame2.destroy()
            logoLabel2.destroy()
            home()

        createAccountButton2 = Button(labelFrame2, text='Create Account',
                                      font=('times new roman', 15),
                                      bg='blue',
                                      fg='white',
                                      width=50,
                                      activebackground='blue',
                                      command=gotohome)
        createAccountButton2.grid(row=6, columnspan=2, pady=10)

        #Back to Login------------------------------------------------------------------------------------
        def back():
            createAccountButton2.destroy()
            noOfRoomsEntry2.destroy()
            noOfRoomsLabel2.destroy()
            emailEntry2.destroy()
            emailLabel2.destroy()
            contactPersonEntry2.destroy()
            contactPersonLabel2.destroy()
            passwordEntry2.destroy()
            passwordLabel2.destroy()
            phoneNumberEntry2.destroy()
            phoneNumberLabel2.destroy()
            hotelNameEntry2.destroy()
            hotelNameLabel2.destroy()
            labelFrame2.destroy()
            frame2.destroy()
            logoLabel2.destroy()
            login()

        loginButton2 = Button(frame2, text='Have an account? Go to login!',
                              font=('times new roman', 15, 'bold'),
                              bd=0,
                              command=back)
        loginButton2.pack(fill=X)
#End of REG----------------------------------------------
    #variables


    root.geometry('1270x685')
    root.minsize(width=900, height=600)
    root.title('Venus')
    root.iconbitmap(icon1)
    root.config(bg=bgcolor1)

    frame1 = Frame(root, bg=bgcolor1)
    #frame1.pack(fill=X)
    frame1.pack(fill=X)

    iconLabel1 = Label(frame1,
                  bg=bgcolor1,
                  image= logo1)
    iconLabel1.pack(pady=10)

    loginframe1 = Frame(root,
                       bg= 'white')
    loginframe1.pack(anchor='center')

    loginLabel1 = LabelFrame(loginframe1, text='Login', font=('arial', 10),
                            bg= 'white',
                            )
    loginLabel1.pack(fill=X, pady= 10, padx=10)

    emailLabel1 =Label(loginLabel1, text='Email', font=('times new roman', 15),
                      bg='white')
    emailLabel1.grid(row=0, column=0, padx=100, sticky='w')

    emailEntry1 = Entry(loginLabel1, font=('arial', 20), bd=6, width= 25)
    emailEntry1.grid(row=1, column=0, pady=10, padx=100)


    passwordLabel1 =Label(loginLabel1, text='Password', font=('times new roman', 15),
                      bg='white')
    passwordLabel1.grid(row=2, column=0,padx=100, sticky='w')

    passwordEntry1 = Entry(loginLabel1, font=('arial', 20), bd=6, width= 25)
    passwordEntry1.grid(row=3, column=0,pady=10, padx=100)


    check1 = Checkbutton(loginLabel1, text='Remember Password',
                        font=('times new roman', 15),
                        bg='white',
                        activebackground='white'
                        )
    check1.grid(row=4, column=0, sticky='w', padx=100, pady=10)

    forgotpwdButton1 = Button(loginLabel1, text = 'Forgot Password?',
                            font=('times new roman', 15, 'bold'),
                            bd=0,
                            bg='white',
                            fg='DodgerBlue4',
                            activebackground='white',
                              command= forgotpwd)
    forgotpwdButton1.grid(row=5, column=0, sticky='w', padx=100, pady=10)



    loginButton1 = Button(loginLabel1, text='Login',
                         font=('times new roman', 15),
                         bg='blue',
                         fg='white',
                         activebackground='blue',
                          command= home)
    loginButton1.grid(row=6, column=0, pady=10)


    registerButton1 = Button(loginframe1, text = 'Need an account? Sign up!',
                            font=('times new roman', 15, 'bold'),
                            bd=0,
                            command= register)
    registerButton1.pack(fill=X)


login()
root.mainloop()