# A movie theater charge different price for different ages

ticket="Different tickets prices"
ticket+="\n What is your age?"

while True:
    age=int(input(ticket))

    if age<3:
        print("Free Ticket")
    elif age<12:
        print("The Ticket price is $10")
    elif age<20:
        print("The ticket price is $20"
    else:
        print("the ticket price is $15")

#This program is written using conditional statement (if, elif, else)


