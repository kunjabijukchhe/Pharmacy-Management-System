import sys
import pymysql
from datetime import datetime
import os

py = sys.executable


def back():
    os.system('%s %s' % (py, 'main.py'))



py = sys.executable


def purchase():
    try:
        conn = pymysql.connect(host="localhost", user="root", password="root", database="stock")

        mid = input("Enter the Medicine ID:")
        name = input("Enter the Medicine Name:")
        sid = input("Enter the Supplier ID:")
        cid = input("Enter the Customer ID:")
        qun = input("Enter the quantity:")
        now = datetime.now()
        idate = now.strftime('%Y-%m-%d %H:%M:%S')

        # for category
        myCursor1 = conn.cursor()
        myCursor1.execute("Select category  from customer where cust_id= %s", [cid])
        conn.commit()
        myresult = myCursor1.fetchone()


        # for price
        myCursor2 = conn.cursor()
        myCursor2.execute("Select price  from medicine where m_id= %s", [mid])
        conn.commit()
        result = myCursor2.fetchone()

        p = int(qun) * int(result[0])

        if myresult[0] == "bronze":
            dis = int(p) * 0.05
        elif myresult[0] == "silver":
            dis = int(p) * 0.07
        elif myresult[0] == "gold":
            dis = int(p) * 0.10
        else:
            dis = int(p) * 0.025

        # discount
        tot = int(p) - int(dis)
        myCursor4 = conn.cursor()
        myCursor4.execute("Select remaining_unit from medicine where m_id= %s", [mid])
        conn.commit()
        result2 = myCursor4.fetchone()
        unit = result2[0]

        rem = int(unit) - int(qun)
        if rem < 2:
            print("\t\t***Stock is Nearly empty***")
            myCursor3 = conn.cursor()
            myCursor3.execute("Update medicine set remaining_unit=%s where m_id=%s", [rem, mid])
            conn.commit()
        elif rem <= 0:
            print("\t\t***Out of Stock***")

        else:
            print("\t\t***Purchased Successfully***")
            myCursor3 = conn.cursor()
            myCursor3.execute("Update medicine set remaining_unit=%s where m_id=%s", [rem, mid])
            conn.commit()



        myCursor = conn.cursor()
        myCursor.execute(
            "Insert into purchase(m_id,m_name,s_id,cust_id,quantity,date,price,discount,total,remaining_unit) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            [mid, name, sid, cid, qun, idate, p, dis, tot, rem])
        conn.commit()

        myCursor5 = conn.cursor()
        myCursor5.execute("Select * from customer where cust_id= %s", [cid])
        conn.commit()
        myresult = myCursor5.fetchall()

        myCursor6 = conn.cursor()
        myCursor6.execute("Select * from purchase where date= %s", [idate])
        conn.commit()
        result = myCursor6.fetchall()
        for x in myresult:
            print('--------------INVOCIE-----------------')
            print("Customer Name:", x[1])
            print("Customer Category:", x[4])
            print('--------------------------------------')
        for i in result:
            print("Purchase Medicine Name:", i[3])
            print("Purchase Quantity:", i[4])
            print('--------------------------------------')
            print('--------------INVOCIE-----------------')
            print("Purchase Date:", i[5])
            print('---------------RECEIPT----------------')
            print("Price:", i[9])
            print("Discount:", i[8])
            print("Total Price:", i[7])
            print('----------------END-------------------\n')

        myCursor5.close()
        myCursor6.close()
        myCursor.close()
        myCursor1.close()
        myCursor2.close()
        myCursor3.close()
        myCursor4.close()
        conn.close()

    except:
        print("\t\t***Something goes wrong or Out of Stock***")


def viewPurchase():
    try:
        conn = pymysql.connect(host="localhost", user="root", password="root", database="stock")
        myCursor = conn.cursor()
        myCursor.execute("Select * from purchase")

        conn.commit()
        myresult = myCursor.fetchall()
        print('+----------------------------+')
        print("|Total Purchased Till Now:", myCursor.rowcount, "|")
        print('+----------------------------+')

        for x in myresult:
            print('-----------------------Report-------------------------')
            print("Purchase Id:", x[0])
            print("Customer Id:", x[6])
            print("Medicine Name:", x[3])
            print("Total Price after Discount:", x[7])
            print("Date:", x[5])
            print('------------------------------------------------------')
        myCursor.close()
        conn.close()

    except:
        print("")



while True:
    print('------------------------------------------------------')
    print('1.Purchase Medicine \n2.View purchase Report\n3.Back To Menu')
    print('------------------------------------------------------')
    choice = input('Enter the number of your choice : ')
    print('------------------------------------------------------')

    if choice == '1':
        print('----------------------Purchase------------------------')
        purchase()
        print('------------------------------------------------------')

    elif choice == '2':
        print('-------------------Purchase---------------------------')
        viewPurchase()
        print('-----------------------*****--------------------------')

    elif choice == '3':
        back()
        break

    else:
        print('You entered an invalid option')
