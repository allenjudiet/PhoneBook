import mysql.connector as sql
db=sql.connect(host="localhost",user="root",passwd="xiibk",database="phonebook")
global cursor
cursor=db.cursor()

def insert(name,phnum):
    cursor.execute("INSERT INTO contact(name,number) VALUES(%s,%s)",(name,phnum))
    db.commit()
    print("content added")
    
def viewall():
    cursor.execute("select *FROM contact")
    rec=cursor.fetchall()
    print("sno--name--number")
    for i in rec:
        print(i)
def terminate():
    cursor.execute("DELETE FROM contact")
    print("ALL CONTACTS DELETED")
    db.commit()

def search(name):
    cursor.execute("select *FROM contact WHERE name ='{}'".format(name))
    rec=cursor.fetchall()
    if len(rec)==0:
        print("contact not found")
    for i in rec:
        print(i)
        
def delete(sno):
    cursor.execute("DELETE FROM contact WHERE sno={}".format(sno))
    db.commit()
    print("content deleted")
    
def modify(sno):
    choice=input("would you like to change name/number (na/nu)")
    if choice=="na":
        data=input("ENTER NEW NAME: ")
        cursor.execute("UPDATE contact set name='{}' WHERE sno={}".format(data,sno))
        db.commit()
        print("CONTENT MODIFIED")
    elif choice=="nu":
            data=input("ENTER NEW NUMBER: ")
            cursor.execute("UPDATE contact set number='{}' WHERE sno={}".format(data,sno))
            db.commit()
            print("CONTENT MODIFIED")
    else:
        print("INVALID CHOICE")
        

def mainmenu():
    
    print(">ENTER 'A' TO VIEW ALL CONTACTS")
    print(">ENTER 'B' TO ADD NEW CONTACTS")
    print(">ENTER 'C' TO DELETE A CONTACT")
    print(">ENTER 'D' TO MODIFYA CONTACT")
    print(">ENTER 'E' TO SEARCH FOR A CONTACT")
    print(">ENTER 'X' TO DELETE ALL CONTACTS")
    print(">ENTER 'Q' TO QUIT")
    print()
    ch=input("CHOICE > ")
    ch=ch.upper()
    return ch

###MAIN
x=""
print("----WELCOME TO PHONEBOOK----")
x=mainmenu()
while x!='Q':
    if x=="A":
        viewall()
        print()
        x=mainmenu()
    elif x=="B":
        name=input("ENTER NAME: ")
        number=input("ENTER NUMBER: ")
        insert(name,number)
        print()
        x=mainmenu()
    elif x=="C":
        sno=int(input("ENTER INDEX: "))
        delete(sno)
        print()
        x=mainmenu()
    elif x=="D":
        sno=int(input("ENTER INDEX: "))
        modify(sno)
        print()
        x=mainmenu()
    elif x=="E":
        name=input("ENTER NAME: ")
        search(name)
        print()
        x=mainmenu()
    elif x=="X":
        terminate()
        print()
        x=mainmenu()
        print()
    else:
        print("INVALID CHOICE")
        print()
        x=mainmenu()
if x=="Q":
    print("THANKS FOR USING PHONEBOOK")

    quit()
