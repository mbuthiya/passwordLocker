#!  /usr/bin/python3.6
# A Password locker program that allows you to generate new passwords and store your own
import string,random,sys,pyperclip

# function to generate password  and return it
def generate_password():
    letters_list =list(string.ascii_letters)
    number_list = list(range(0,53))
    new_password =''

    for i in range(0,4):
        random_integer = random.randint(0,52)
        new_password = new_password + letters_list[random_integer] + str(number_list[random_integer])

    return new_password

def check_account(account_name):
    if account_name in passwords:
        pyperclip.copy(passwords[account_name])
        print(f"The {account_name} password has been coppied to clipboard")
    else:
        print('There is no account with that name stored would you like to generate a new password y/n:')
        response = input()

        if response == 'y':
            pyperclip.copy(generate_password())
            print(f"The {account_name} password has been coppied to clipboard")
        else:
            sys.exit()




# Dictionary to store the passwords and accounts
passwords = {'email':'2kdknknjndj'}
#Checking if there is a second argument passed in the command line
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]
check_account(account)
