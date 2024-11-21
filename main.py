### Main calendar program


### Virgil
import calendar
from datetime import datetime



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


    # Calculate weekly pay for each caregiver
    def calculate_weekly_pay(self):
        return self.assigned_hours * self.pay_rate



### Add new caregivers
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
    print(f"\nSetting {caregiver.name}'s availability:")
    
    # Begin to set availability for each day
    for day in days:
        print(f"\n### {day} ###")
        
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

    print(f"\n{caregiver.name}'s availability set.")



### Update availability of a caregiver
def update_availability(caregivers):
    if not caregivers:
        print("\nNo caregivers available.")
        return

    # Display caregivers
    print("\n### Caregiver List ###")

    for i, caregiver in enumerate(caregivers, 1):
        print(f"{i}. {caregiver.name} ({caregiver.phone})")

    # Select caregiver
    try:
        choice = int(input("\nSelect a caregiver by NUMBER: "))

        if choice < 1 or choice > len(caregivers):
            print("Invalid selection.")
            return

    except ValueError:
        print("Invalid input.")
        return

    selected_caregiver = caregivers[choice - 1]
    print(f"\nSelected caregiver: {selected_caregiver.name}")

    # Update weekly availability
    set_week_availability(selected_caregiver)



### Assign a shift to a caregiver
def assign_shift(caregiver, date, shift):
    # Check if person is unavailable
    if caregiver.get_availability(date).get(shift, 'unavailable') == 'unavailable':
        print(f"{caregiver.name} is unavailable on {shift} {date}.")
        return
    
    # Assign shift 
    print(f"{caregiver.name} assigned to {shift} shift for {date}.")
    caregiver.add_hours(6)  # Each shift is 6 hours
    print(f"{caregiver.name} has now worked {caregiver.assigned_hours} hours.")

### Thomas
class Caregiver:
    def __init__(self, name, phone, email, pay_rate):
        self.name = name
        self.phone = phone
        self.email = email
        self.pay_rate = pay_rate
        self.availability = {"AM": "available", "PM": "available"}  # Default availability

    # Set availability for a specific shift
    def set_availability(self, shift, availability):
        if shift in self.availability and availability in ["preferred", "available", "unavailable"]:
            self.availability[shift] = availability
        else:
            print("Invalid input.")

    # Display caregiver's availability
    def display_availability(self):
        print(f"Availability for {self.name}:")
        for shift, status in self.availability.items():
            print(f"{shift} shift: {status}")

# Create caregiver instances
caregiver1 = Caregiver("Alice", "123-456-7890", "alice@example.com", 20)
caregiver2 = Caregiver("Bob", "234-567-8901", "bob@example.com", 20)

# Set availability for each caregiver
caregiver1.set_availability("AM", "preferred")
caregiver1.set_availability("PM", "unavailable")

caregiver2.set_availability("AM", "available")
caregiver2.set_availability("PM", "preferred")

# Display caregiver availability
caregiver1.display_availability()
caregiver2.display_availability()


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

