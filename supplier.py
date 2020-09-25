import sys
import os
import pymysql

py = sys.executable


def back():
    os.system('%s %s' % (py, 'main.py'))


def addSupplier():
    try:
        conn = pymysql.connect(host="localhost", user="root", password="root", database="stock")

        myCursor = conn.cursor()
        name = input("Enter the Supplier Name:")
        city = input("Enter the Supplier City:")
        pn = input("Enter the Supplier phone No.")

        myCursor.execute("Insert into supplier(s_name,s_city,s_phone) values (%s,%s,%s)",
                         [name, city, pn])
        conn.commit()
        print("Supplier added Successfully")

    except:
        print("Something goes wrong")


def removeSupplier():
    a = input("Enter Supplier Name to remove:")
    try:
        conn = pymysql.connect(host="localhost", user="root", password="root", database="stock")
        myCursor = conn.cursor()
        myCursor.execute("Delete from supplier where s_name = %s", [a])
        conn.commit()
        myCursor.close()
        conn.close()
        print("\t\tSupplier Removed Successfully")
        a.set("")
    except:
        print("")


def viewSupplier():
    try:
        conn = pymysql.connect(host="localhost", user="root", password="root", database="stock")
        myCursor = conn.cursor()
        myCursor.execute("Select * from supplier")

        conn.commit()
        myresult = myCursor.fetchall()

        for x in myresult:
            print(x)
        myCursor.close()
        conn.close()

    except:
        print("")


while True:
    print('-----------------------------------------------------------')
    print('1.Add Supplier \n2.Remove Supplier\n3.View Supplier\n4.Back To Menu')
    print('-----------------------------------------------------------')
    choice = input('Enter the number of your choice : ')
    print('-----------------------------------------------------------')

    if choice == '1':
        print('----------------------Add Supplier--------------------')
        addSupplier()
        print('------------------------------------------------------')


    elif choice == '2':
        print('--------------------Remove Supplier------------------')
        removeSupplier()
        print('------------------------------------------------------')


    elif choice == '3':
        print('---------------------Supplier-------------------------')
        viewSupplier()
        print('------------------------------------------------------')


    elif choice == '4':
        back()
        break

    else:
        print('You entered an invalid option')
