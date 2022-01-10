################## LIB ##################################
import smtplib
import termcolor, os
from termcolor import colored
server= smtplib.SMTP('smtp.gmail.com.',587)


#################### EMAILER #############################
os.system("clear")


a = (""" 
  ___           _ __  _   _ 
 / _ \  _____  | '_ \| | | |
|  __/ |_____| | |_) | |_| |
 \___|         | .__/ \__, |
               |_|    |___/ 

                    by Mal4D
""")

print(colored(a,'cyan'))




s= input("Is this your first time using this app (Yes/No) : ")
if s == "yes":
    os.system("clear")
    print(colored(a,'yellow'))

    email= input("Enter your email : ")
    passw=input("Enter your pass : ")
    direction=input("Enter the direction : ")
    message=input("Input the message please : ")


    print(colored("Sending ...", "yellow"))

    f=open("email.txt" , "w+")
    f.write(email)
    f.close()
    f1=open("pass.txt" , "w+")
    f1.write(passw)
    f1.close()


    server.starttls()
    server.login(email,passw)
    server.sendmail(email,direction,message)

if s == "no":
    os.system("clear")
    print(colored(a,'green'))

    st=int(input("""1 ==> Send an email
2 ==> Erase all data 
Enter the number please :  """))
    if st == 1 :
        os.system("clear")
        print(colored(a,'magenta'))

        f2=open('email.txt', "r")
        email= f2.read()
        f3=open('pass.txt', "r")
        passw=f3.read()
        direction=input("Enter the direction : ")
        message=input("Input the message please : ")

        print(colored("Sending ...", "yellow"))

        server.starttls()
        server.login(email,passw)
        server.sendmail(email,direction,message)

    if st == 2:
        os.system("clear")
        print(colored(a,'red'))

        os.remove("email.txt")
        os.remove("pass.txt")

        print(colored("Removed Succesfully","red"))