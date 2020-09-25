import sys
import os
import pymysql

py = sys.executable


def back():
    os.system('%s %s' % (py, 'main.py'))


def addMedicine():
    try:
        conn = pymysql.connect(host="localhost", user="root", password="root", database="stock")

        myCursor = conn.cursor()
        name = input("Enter the Medicine Name:")
        unit = input("Enter the Unit:")
        supplier_id = input("Enter the Supplier ID:")
        price = input("Enter the price of Medicine(per unit):")

        myCursor.execute("Insert into  medicine(m_name,unit,s_id,price) values (%s,%s,%s,%s)",
                         [name, unit, supplier_id, price])

        conn.commit()
        print("Medicine added Successfully")

    except:
        print("Something goes wrong")


def removeMedicine():
    a = input("Enter Medicine Name to remove:")
    try:
        conn = pymysql.connect(host="localhost", user="root", password="root", database="stock")
        myCursor = conn.cursor()
        myCursor.execute("Delete from  medicine where m_name = %s", [a])
        conn.commit()
        myCursor.close()
        conn.close()
        print("\t\tMedicine Removed Successfully")
        a.set("")
    except:
        print("")


def viewMedicine():
    try:
        conn = pymysql.connect(host="localhost", user="root", password="root", database="stock")
        myCursor = conn.cursor()
        myCursor.execute("Select * from medicine")

        conn.commit()
        myresult = myCursor.fetchall()

        for x in myresult:
            print(x)
        myCursor.close()
        conn.close()

    except:
        print("")

def remainingMedicine():
    try:
        conn = pymysql.connect(host="localhost", user="root", password="root", database="stock")
        myCursor = conn.cursor()
        myCursor.execute("Select * from medicine")

        conn.commit()
        myresult = myCursor.fetchall()

        for x in myresult:
            print("Medicine Name:",x[1])
            print("Remaining Unit:", x[5])
            print('------------------------------------------------------')
        myCursor.close()
        conn.close()

    except:
        print("")


while True:
    print('------------------------------------------------------')
    print('1.Add Medicine \n2.Remove Medicine\n3.View Medicine\n4.Remaining Medicine List\n5.Back To Menu')
    print('------------------------------------------------------')
    choice = input('Enter the number of your choice : ')
    print('------------------------------------------------------')

    if choice == '1':
        print('---------------------Add Medicine---------------------')
        addMedicine()
        print('------------------------------------------------------')


    elif choice == '2':
        print('---------------------Remove Medicine------------------')
        removeMedicine()
        print('------------------------------------------------------')

    elif choice == '3':
        print('------------------------Medicine----------------------')
        viewMedicine()
        print('------------------------------------------------------')

    elif choice == '4':
        print('------------------------Medicine----------------------')
        remainingMedicine()
        print('------------------------------------------------------')
    elif choice == '5':
        back()
        break

    else:
        print('You entered an invalid option')
