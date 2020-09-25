import sys
import os


py = sys.executable


def back():
    os.system('%s %s' % (py, 'main.py'))


def help():
    print('------------------------------Help Menu------------------------------------')
    print("Press 1: To Add Medicine\t\t To Remove Medicine\t\t To View Medicine\t\tRemaining Medicine List")
    print('---------------------------------------------------------------------------')
    print("Press 2: Purchase Medicine\t\t View Purchased Medicine")
    print('---------------------------------------------------------------------------')
    print("Press 3: To Add Customer\t\t To Remove Customer\t\t To View Customer\t\t To Search Customer with Receipt")
    print('---------------------------------------------------------------------------')
    print("Press 4: To Add Supplier\t\t To Remove Supplier\t\t To View Supplier")
    print('---------------------------------------------------------------------------')


while True:
    print('------------------Welcome to the Pharmacy------------------')
    print('1.Help Details\n2.Back to Menu ')
    print('-----------------------------------------------------------')
    choice = input('Enter the number of your choice : ')
    print('-----------------------------------------------------------')

    if choice == '1':
        help()
    elif choice == '2':
        back()
        break

    else:
        print('You entered an invalid option')