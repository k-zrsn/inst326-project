### Main calendar program


### Virgil


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