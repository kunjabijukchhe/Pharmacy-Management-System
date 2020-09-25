import sys
import os
import pymysql

py = sys.executable


def back():
    os.system('%s %s' % (py, 'main.py'))


def addCustomer():
    try:
        conn = pymysql.connect(host="localhost", user="root", password="root", database="stock")

        myCursor = conn.cursor()
        name = input("Enter the Customer Name:")
        pn = input("Enter the Customer phone No.")
        add = input("Enter the Customer Address:")
        cate = input("Enter the Customer category(gold,silver, bronze, normal):")
        myCursor.execute("Insert into customer(cust_name,cust_phone,cust_address,category ) values (%s,%s,%s,%s)",
                         [name, pn, add, cate])
        conn.commit()
        print("\t\tCustomer added Successfully")

    except:
        print("Something goes wrong")


def removeCustomer():
    a = input("Enter Customer Name to remove:")
    try:
        conn = pymysql.connect(host="localhost", user="root", password="root", database="stock")
        myCursor = conn.cursor()
        myCursor.execute("Delete from customer where cust_name = %s", [a])
        conn.commit()
        myCursor.close()
        conn.close()
        print("Customer Removed Successfully")
        a.set("")
    except:
        print("")


def viewCustomer():
    try:
        conn = pymysql.connect(host="localhost", user="root", password="root", database="stock")
        myCursor = conn.cursor()
        myCursor.execute("Select * from customer")

        conn.commit()
        myresult = myCursor.fetchall()
        print("Total number of Customer: ", myCursor.rowcount, "\n")
        for x in myresult:
            print("Customer Id:", x[0])
            print("Customer Name:", x[1])
            print("Customer Phone No.", x[2])
            print("Customer Address:", x[3])
            print("Customer Category:", x[4])
            print("\n")

        myCursor.close()
        conn.close()

    except:
        print("")


def searchCustomer():
    cid = input("Enter the Customer ID:")
    try:
        conn = pymysql.connect(host="localhost", user="root", password="root", database="stock")
        myCursor = conn.cursor()
        myCursor.execute("Select * from customer where cust_id= %s", [cid])
        conn.commit()
        myresult = myCursor.fetchall()

        myCursor1 = conn.cursor()
        myCursor1.execute("Select * from purchase where cust_id= %s", [cid])
        conn.commit()
        result = myCursor1.fetchall()
        print('--------------------------------------')
        print("Customer Have Purchased: ", myCursor1.rowcount, "times.")
        print('--------------------------------------')
        for x in myresult:
            print("Customer Name:", x[1])
            print("Customer Phone No.", x[2])
            print("Customer Address:", x[3])
            print("Customer Category:", x[4])
        for i in result:
            print("Customer Purchase Medicine:", i[3])
            print("Customer Purchase Medicine Quantity:", i[4])
            print('--------------------------------------')
            print("Purchase Date:", i[5])
            print('---------------RECEIPT----------------')
            print("Price:", i[9])
            print("Discount:", i[8])
            print("Total Price:", i[7])
            print('----------------END-------------------\n')

        myCursor.close()
        myCursor1.close()
        conn.close()

    except:
        print("")


while True:
    print('-----------------------------------------------------------')

    print('1.Add Customer \n2.Remove Customer\n3.View Customer\n4.Search Customer with Receipt\n5.Back To Menu')
    print('-----------------------------------------------------------')
    choice = input('Enter the number of your choice : ')
    print('-----------------------------------------------------------')

    if choice == '1':
        print('-----------------------Add Customer------------------------')
        addCustomer()
        print('-----------------------------------------------------------')


    elif choice == '2':
        print('-----------------------Remove Customer-----------------------')
        removeCustomer()
        print('-------------------------------------------------------------')

    elif choice == '3':
        print('-----------------------Customer-----------------------')
        viewCustomer()
        print('------------------------------------------------------')

    elif choice == '4':
        print('-------------Customer-----------------')
        searchCustomer()
        print('--------------------------------------')

    elif choice == '5':
        back()
        break

    else:
        print('You entered an invalid option')
