#!  /usr/bin/python3.6
# A Password locker program that allows you to generate new passwords and store your own
import string,random,sys

# function to generate password  and return it
def generate_password():
    letters_list =list(string.ascii_letters)
    number_list = list(range(0,53))
    new_password =''

    for i in range(0,4):
        random_integer = random.randint(0,52)
        new_password = new_password + letters_list[random_integer] + str(number_list[random_integer])

    return new_password
