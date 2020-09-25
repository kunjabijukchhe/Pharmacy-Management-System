import os
import sys

py = sys.executable

def m():
    os.system('%s %s' % (py, 'stock.py'))

def p():
    os.system('%s %s' % (py, 'invoice.py'))

def c():
    os.system('%s %s' % (py, 'customer.py'))

def s():
    os.system('%s %s' % (py, 'supplier.py'))
def h():
    os.system('%s %s' % (py, 'helpMenu.py'))

while True:
    print('----------------Welcome to the Pharmacy---------------')

    print('1.Medicine\n2.Purchase\n3.Customer \n4.Supplier\n5.Help\n6.Exit')
    print('------------------------------------------------------')
    choice = input('Enter the number of your choice : ')
    print('------------------------------------------------------')

    if choice == '1':
        m()
    elif choice == '2':
        p()
    elif choice == '3':
        c()
    elif choice == '4':
        s()
    elif choice == '5':
        h()
    elif choice == '6':
        print('----------------------exited--------------------------')
        break


    else:
        print('You entered an invalid option')
