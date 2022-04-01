import datetime
import time
from math import floor

class Parking_Garage():

    def __init__(self):
        self.tickets = ["1","2","3","4","5","6","7","8","9","10"]
        self.spaces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.current_ticket ={}
        self.s = None
    

    def take_ticket(self):
        while True:
            if len(self.spaces) > 0:
                t = self.tickets.pop()
                self.s = self.spaces.pop()

                self.current_ticket[t] = 'unpaid'
                print(f"Your ticket number is {t}. Please keep that handy when you go to pay.")
                start_t = time.time()
                self.current_ticket[self.s] = start_t
                break
        
            else:
                print("There are no move available spaces! Please try again later")
                break

    def leave_garage(self):
        ticket_number = input("What is your ticket number? ")
        if ticket_number in self.current_ticket.keys():
            print("Ticket Verified")
            if self.current_ticket[ticket_number] == 'unpaid':
                print("You haven't paid your ticket. Please pay before you leave the garage.")
                self.pay_ticket(ticket_number)
            if self.current_ticket[ticket_number] == 'paid':
                self.tickets.append(ticket_number)
                self.spaces.append(ticket_number)
                del self.current_ticket[ticket_number]
                del self.current_ticket[int(ticket_number)]
                print("Thank you. Have a nice day.")
                
        else:
            response = input("That is not a valid ticket number...Do you have a ticket? y/n.")
            if response.lower().strip() == 'y':
                self.leave_garage()
            else:
                print("Please take a ticket first.")

    def pay_ticket(self, ticket_number = None):
        if ticket_number == None:
                ticket_number = input("What is your ticket number? ")
        if ticket_number in self.current_ticket.keys():
            print("Ticket Verified")
            end_t = time.time()
            self.current_ticket[int(ticket_number)] -= end_t
            stay_duration = abs(self.current_ticket[int(ticket_number)])
            if stay_duration <= 10.0:
                cost = '$10'
            elif stay_duration > 10.0 and stay_duration <= 30.0:
                cost = '$20'
            else:
                cost = '$30'
            paid = input(f"You stayed {floor(stay_duration)} seconds. Please enter {cost} to pay for ticket. ")
            if paid.strip() == cost:
                self.current_ticket[ticket_number] = 'paid'
                print("Your ticket has been paid please leave in 15 mins")

            else:
                print(f"Invalid attempt, please enter {cost} to pay for ticket.")
                self.pay_ticket()
        else:
            response = input("That is not a valid ticket number...Do you have a ticket? y/n.")
            if response.lower().strip() == 'y':
                self.pay_ticket()
            else:
                print("Please take a ticket first.")
                

a_n_d_parking = Parking_Garage()        

def run():
    print("Welcome to our parking garage! ")

    home = "\nWhat do you want to do? Take Ticket / Pay Ticket / Leave Garage / Quit: "
    while True:
        response = input(home)
        if response.lower().strip() == 'take ticket':
            a_n_d_parking.take_ticket()
        elif response.lower().strip() == 'pay ticket':
            a_n_d_parking.pay_ticket()
        elif response.lower().strip() == 'leave garage':
            a_n_d_parking.leave_garage()
        elif response.lower().strip() == 'quit':
            print("Have a good day!")
            break
        else:
            print("Invalid Response...Try Again.")  


run()
