from tkinter import *
root=Tk()
root.geometry("500x300")
def getvals():
    print("Accepted")



Label(root,text="Registration form",font="arial 15 bold").grid(row=0, column=3)

name=Label(root, text="Name")
phone=Label(root, text="PHONE")
Gender=Label(root, text="Gender")
email=Label(root, text="Email")
Password=Label(root, text="Password")

name.grid(row= 1,column=2)
phone.grid(row=2 ,column=2)
Gender.grid(row= 3,column=2)
email.grid(row= 4,column=2)
Password.grid(row=5 ,column=2)




namevalue=StringVar
phonevalue=StringVar
gendervalue=StringVar
emailvalue=StringVar
passwordvalue=StringVar
checkvalue=IntVar

nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phonevalue)
genderentry=Entry(root,textvariable=gendervalue)
emailentry=Entry(root,textvariable=emailvalue)
passwordentry=Entry(root,textvariable=passwordvalue)

nameentry.grid(row= 1,column=3)
phoneentry.grid(row=2 ,column=3)
genderentry.grid(row=3 ,column=3)
emailentry.grid(row= 4,column=3)
passwordentry.grid(row=5 ,column=3)

checkbtn=Checkbutton(text="remeber me?", variable=checkvalue)
checkbtn.grid(row=6,column=3)

Button(text="Submit", command=getvals).grid(row=7, column=3)
root.mainloop()















