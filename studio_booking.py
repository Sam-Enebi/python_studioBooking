# Author: Sam Enebi

#CONSTANTS
DAY_1 = 260
DAY_2_4 = 240
DAY_5_8 = 210
DAY_9_PLUS = 200
SESSION_MUSICIANS = 100
CREDIT_CARD = 1.05
CHEQUE = 1
CASH = 0.95
MAX_MUSICIANS = 8

#INPUTS
name = ""
while len(name) == 0:
    name = input("What is your band name? ")

email = ""
while email.find("@") == -1:
    email = input("What is your email? ")

valid_phone_number = False
while valid_phone_number == False:
    try:
        phone_number = int(input("What is your phone number? "))
        valid_phone_number = True
    except:
        print("Invalid Number")

start_date = input("What date do you want to start (dd/mm/yyyy)? ")
while len(start_date) < 10 or len(start_date) > 10:
    start_date = input("What date do you want to start (dd/mm/yyyy)? ")
    if len(start_date) == 10:
        while start_date[2] != ("/") and start_date[5] != ("/"):
            start_date = input("What date do you want to start (dd/mm/yyyy)? ")

valid_no_of_members = False
while valid_no_of_members == False:
    try:
        members = int(input("How many members are in the band? "))
        if members > 0 and members <= 8:
            valid_no_of_members = True
        else:
            print("Not within the allowed amount")
            valid_no_of_members = False
    except:
        print("Invalid Number")

valid_days = False
while valid_days == False:
    try:
        days = int(input("How many days? "))
        if days > 0:
            valid_days = True
        else:
            print("Invalid no. of days entered")
            valid_days = False
    except:
        print("Invalid no. of days entered")

# IF STATEMENT
if days == 1:
    days = DAY_1
elif days >= 2 and days <= 4:
    days = DAY_2_4 * days
elif days >= 5 and days <= 8:
    days = DAY_5_8 * days
else:
    days = DAY_9_PLUS * days

session_musicians_available = MAX_MUSICIANS - members

#WHILE LOOP
i = 1
list = ""
while i <= members:
    member_name = ""
    while len(member_name) == 0:
        member_name = input("What is band member #" + str(i) + "'s name? ")
        if len(member_name) != 0:
            instrument = ""
            while len(instrument) == 0:
                instrument = input("What is " + str(member_name) + "'s instrument? ")
    i = i + 1
    list = list + str(i - 1) + ":" + str(member_name) + " - " + str(instrument) + "\n"

#INPUT FOR MUSICIAN SESSIONS
session_musicians_number = False
session_musicians = int(
    input("There is room for " + str(session_musicians_available) + " session musicians - How many do you want? "))
if session_musicians + members <= MAX_MUSICIANS:
    session_musicians_number = True
else:
    print("Invalid amount of musicians allowed")
    session_musicians_number = False

#CALCULATIONS FOR TOTAL
amount_for_musicians = days * session_musicians
amount_per_day = days
amount = (days * session_musicians) + days

#PAYMENT METHOD
Credit_Card = CREDIT_CARD * amount
Cash = amount - (CASH * amount)
Cheque = amount
menu = "1: Credit Card \t""5% Levy" + "\n2: Cash \t""5% Discount" + "\n3: Cheque" + "\n"

#MENU IF STATEMENT
choice = int(input(menu))
if choice == 1:
    amount = Credit_Card
elif choice == 2:
    amount = Cash
else:
    amount = amount

#PRINT
print("")
print("Booking Application")
print("-------------------")
print("Requested by:", name, "(Contact:", email, "&", phone_number, ")")
print("Date requested:", start_date)
print("")
print("Band Members")
print("-------------------")
print(list)
print("Includes", session_musicians, "session musicians per day.\nPayment will be", amount, "Euros.")