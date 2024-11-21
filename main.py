### Main calendar program


### Virgil
import calendar
import random



### Initialize caregiver list
caregivers = []



### Create Caregiver class
class Caregiver:
    def __init__(self, name, phone, email, pay_rate):
        self.name = name
        self.phone = phone
        self.email = email
        self.pay_rate = pay_rate
        self.assigned_hours = 0
        self.availability = {
            "Monday": {"AM": "available", "PM": "available"},
            "Tuesday": {"AM": "available", "PM": "available"},
            "Wednesday": {"AM": "available", "PM": "available"},
            "Thursday": {"AM": "available", "PM": "available"},
            "Friday": {"AM": "available", "PM": "available"},
            "Saturday": {"AM": "available", "PM": "available"},
            "Sunday": {"AM": "available", "PM": "available"}
        }


    # Set the availability for the caregiver
    def set_availability(self, date, shift, availability):
        if date not in self.availability:
            self.availability[date] = {}
    
        self.availability[date][shift] = availability


    # Get the availability on a specific date
    def get_availability(self, date):
        return self.availability.get(date, {})


    # Add hours from a shift
    def add_hours(self, hours):
        self.assigned_hours += hours



### Function for adding new caregivers
def add_caregiver():
    # Input contact information
    name = input("Enter Caregiver's Name: ")
    phone = input("Enter Caregiver's Phone Number: ")
    email = input("Enter Caregiver's Email Address: ")

    # Input hourly pay rate
    try:
        pay_rate = float(input("Enter hourly pay rate (default $20/hr): ") or 20)

    except ValueError:
        print("Invalid input. Pay rate set to default $20/hr.")
        pay_rate = 20
    
    caregiver = Caregiver(name, phone, email, pay_rate)
    print(f"\nCaregiver {name} has been added.\n")
    return caregiver



### Set availability for each caregiver
def set_week_availability(caregiver):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print(f"\nSetting availability for {caregiver.name}:")
    
    # Begin to set availability for each day
    for day in days:
        print(f"\n--- {day} ---")
        
        # Set AM availability
        am_avail = input("Enter AM availability (preferred, available, unavailable): ").lower()

        if am_avail not in ['preferred', 'available', 'unavailable']:
            print("Invalid input. Defaulting to 'available'.")
            am_avail = 'available'
    
        caregiver.set_availability(day, 'AM', am_avail)

        # Set PM availability
        pm_avail = input("Enter PM availability (preferred, available, unavailable): ").lower()

        if pm_avail not in ['preferred', 'available', 'unavailable']:
            print("Invalid input. Defaulting to 'available'.")
            pm_avail = 'available'

        caregiver.set_availability(day, 'PM', pm_avail)

    print(f"\nAvailability set for {caregiver.name}.")



### Thomas



### Anthony
import tkinter as tk
from tkinter import ttk
from random import choice

#Calculating Weekly Pay
#def weekly_pay()



#Creating a Window 
window =tk.Tk()
window.geometry('2000x1000')
window.title("Weekly Pay and Monthly Totals")

#Data
caregivers = ['Anthony', 'Thomas', 'Virgil']
Hourly_Pay = [20, 20, 20]
Assigned_Hours = [40, 40, 40]
Weekly_Pay = [800, 800, 800]
Monthly_Pay = [3200, 3200, 3200]

#Table 
table = ttk.Treeview(window, columns = ('Name', 'Pay', 'Assigned', 'Weekly', 'Monthly'), show = 'headings')
table.heading('Name', text = 'Caregiver Name')
table.heading('Pay', text = 'Caregiver Hourly Pay')
table.heading('Assigned', text = 'Caregiver Weekly Hours')
table.heading('Weekly', text = 'Caregiver Weekly Pay')
table.heading('Monthly', text = 'Caregiver Monthly Pay')
table.pack(fill = 'both', expand = True)

#Inserting Data
for i in range(100):
    Name = choice(caregivers)
    table.insert(parent = '', index = 0, values = data)
    
    

#Keeping Window Running
window.mainloop()