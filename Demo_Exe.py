from tkinter import *
from PIL import ImageTk,Image
import sqlite3

bima =Tk()
bima.title("BIMA")
# Creating object of photoimage class
# Image should be in the same folder
# in which script is saved

# Setting icon of master window
bima.iconphoto(False, p1)
bima.geometry("500x500")


#create table           product button open product window id name category subcategory price. show,add,update and delete.
conn = sqlite3.connect("customers.db")
#create cursor
c = conn.cursor() 
c.execute("""CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    customername TEXT NOT NULL,
    customerno INTEGER NOT NULL,
    address TEXT NOT NULL,
    DATETIME DEFAULT CURRENT_)""")

#create save enter values to create submit function for save values
def submit():
    #database
    #cretae databse or connect database
    conn = sqlite3.connect("customers.db")
    #craete cursor
    c = conn.cursor()
# cur.execute("INSERT INTO book(title, author, year, isbn) VALUES (?,?,?,?)",
#                              (title, author, year, isbn))    
    #insert into databse
    c.execute("INSERT INTO customers (customername, customerno, address ) VALUES (:customername,:customerno,:address)",
    {
        "customername":customername.get(),
        "customerno":customerno.get(),
        "address":address.get(),
  
    })
    #create commit
    conn.commit()
    #close database
    conn.close()

    #clear the text after enter the values
    customername.delete(0,END)
    customerno.delete(0, END)
    address.delete(0,END)
   
#create save enter values to display query function for save values
def query():
    #database
    #cretae databse or connect database
    conn = sqlite3.connect("customers.db")
    #craete cursor
    c = conn.cursor()
    
    #query the databse login 
    c.execute("SELECT *,customer_id  FROM customers")
    records=c.fetchall() #use fetch one or many or all
    print(records)
    print_record = ""
    for record in records:
        print_record += str(record[0]) + " " + str(record[1]) + " " + str(record[2]) + " " + str(record[3]) + "\n"
    #query label displaying
    query_l = Label(bima,text=print_record)
    query_l.grid(row=11,column=0, columnspan=7)
    #create commit
    conn.commit()
    #close database
    conn.close()

#create save enter values to remove delete function for save values
def delete():
    #database
    #cretae databse or connect database
    conn = sqlite3.connect("customers.db")
    #craete cursor
    c = conn.cursor()
    
    #query the databse login 
    c.execute("DELETE FROM customers WHERE customer_id = " + delete_box.get())
    delete_box.delete(0, END)
    #create commit
    conn.commit()
    #close database
    conn.close()


# #create save enter values to modify to restore function for save values
def update():
    #database
    #cretae databse or connect database
    conn = sqlite3.connect("customers.db")
    #craete cursor
    c = conn.cursor()
    record_id = delete_box.get()
    c.execute("""UPDATE customers SET 
        customername = :customername,
        customerno = :customerno,
        address = :address

        WHERE customer_id = :customer_id""",
        {
            "customername":customername_edit.get(),
            "customerno":customerno_edit.get(),
            "address":address_edit.get(),
            
            
            "customer_id" : record_id
        })

    #create commit
    conn.commit()
    #close database
    conn.close()
    #clear the text after enter the values
    customername.delete(0,END)
    customerno.delete(0, END)
    address.delete(0,END)


    updater.destroy()



#create edit enter values to remove delete function for save values
def edit():
    global updater    
    updater =Tk()
    updater.title("BIMA")
    updater.iconbitmap("")
    updater.geometry("500x500")
    

    #database
    #cretae databse or connect database
    conn = sqlite3.connect("customers.db")
    #craete cursor
    c = conn.cursor()

    record_id = delete_box.get()
    #query the datbase to edit
    c.execute("SELECT * FROM customers WHERE customer_id = " + record_id)
    records = c.fetchall()

    #create global variable
    global customername_edit
    global customerno_edit
    global address_edit

    #input values using tkinter Entry widget
    customername_edit=Entry(updater,width=38)
    customername_edit.grid(row=1,column=1)
    customerno_edit=Entry(updater,width=38)
    customerno_edit.grid(row=2,column=1)
    address_edit=Entry(updater,width=38)
    address_edit.grid(row=3,column=1)

    #input keys using tkinter Label widget
    #input values using tkinter Entry widget
    customername_l=Label(updater,text="customername")
    customername_l.grid(row=1,column=0)
    customerno_l=Label(updater,text="customerno")
    customerno_l.grid(row=2,column=0)
    address_l=Label(updater,text="address")
    address_l.grid(row=3,column=0)

    #Loop thru resuts
    for record in records:
        customername_edit.insert(0, record[1])
        customerno_edit.insert(0, record[2])
        address_edit.insert(0, record[3])

    #enter edit  values to save  using tkinter Button widget
    save_rec_btn =Button(updater,text="SAVE EDIT",command=update)
    save_rec_btn.grid(row=7,column=0)
    #create commit
    conn.commit()
    #close database
    conn.close()



#input values using tkinter Entry widget
customername=Entry(bima,width=38)
customername.grid(row=1,column=1)
customerno=Entry(bima,width=38)
customerno.grid(row=2,column=1)
address=Entry(bima,width=38)
address.grid(row=3,column=1)
delete_box=Entry(bima,width=38)
delete_box.grid(row=10,column=1)


#input keys using tkinter Label widget
customername_l=Label(bima,text="customername")
customername_l.grid(row=1,column=0)
customerno_l=Label(bima,text="customerno")
customerno_l.grid(row=2,column=0)
address_l=Label(bima,text="address")
address_l.grid(row=3,column=0)
delete_box_l=Label(bima,text="Select Product ID")
delete_box_l.grid(row=10,column=0)


#enter  values using tkinter Button widget
submit_btn =Button(bima,text="New",command=submit)
submit_btn.grid(row=7,column=0)

#enter  values to display  using tkinter Button widget
query_btn =Button(bima,text="SHOW",command=query)
query_btn.grid(row=7,column=1)
#remove  values to display  using tkinter Button widget
delete_btn =Button(bima,text="ERASE",command=delete)
delete_btn.grid(row=12,column=0)
#update  values to display  using tkinter Button widget
update_btn =Button(bima,text="EDIT",command=edit)
update_btn.grid(row=12,column=1)

bima.mainloop()
