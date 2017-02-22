from Classes import Login
# def pick_password():
#     file = '/home/basecamp/Desktop/Rental-Agency/pswd.txt'
#     print("Please input the same username you registered' ")
#     password = input()
#     target = open(file, 'w')
#     target.write(password)
#     file = '/home/basecamp/Desktop/Rental-Agency/existence_check.txt'
#     target = open(file, 'w')
#     target.write('YES')
# Function to check the password with the password located in pswd.txt
def password_check():
    file = '/home/basecamp/Desktop/Rental-Agency/pswd.txt'
    pwd_check = open(file).read()
    userpass = input("Create a Username.. If your such a 'CEO'\n")
    if userpass == pwd_check:
        print('Username accepted!')
        print('Saved into our Extremely secured Database so no worries!;)?')

    elif userpass != pwd_check:
        print('Sorry, wrong password.\n')
        exit()
    else:
        print('Invalid syntax.')
        exit()


# location of password existence check file
EC = '/home/basecamp/Desktop/Rental-Agency/existence_check.txt'
PWD = '/home/basecamp/Desktop/Rental-Agency/pswd.txt'  # Location of password file

pswd_exist = open(EC).read()  # Checking to see if the password exists
if pswd_exist == 'YES':
    pass
else:
    # pick_password()  # If it doesn't, user will pick a password

# Checking for password
    password_check()