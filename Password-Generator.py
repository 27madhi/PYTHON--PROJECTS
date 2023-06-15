"Password Generator"



import string
import random
character=list(string.ascii_letters + string.digits + "$&@#£€¥")
print(character)


def generate_password():
    passw_len=int(input("how long would you like your password to be: "))


    password=[]

    for i in range(passw_len):
        password.append(random.choice(character))


    random.shuffle(password)

    passw= "".join(password)
    print (passw)



user=input("do you want to generate password,then enter yes/no: ").lower()
print (user)
if user == 'yes':
    generate_password()
elif user== 'no':
    print( "Not generate the password")
    quit()
else:
    print("please enter yes/no")
    quit()