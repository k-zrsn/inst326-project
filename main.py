### Main calendar program


### Virgil
import calendar
import random



#amShift = ["7:00 AM - 1:00 PM"]
#pmShift = ["1:00 PM - 7:00 PM"]
day = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat","Sun"]
person = ["Gigi", "Noel", "Joe", "Silvia","Tess", "Rosa", "Lani", "Sayed"]


### Create Caregiver class
class Caregiver:
    def __init__(self, name, phone, email, pay_rate, hours=0):
        self.name = name
        self.phone = phone
        self.email = email
        self.pay_rate = pay_rate
        self.hours = hours
        self.availability = {
            "Monday": {"AM": "available", "PM": "available"},
            "Tuesday": {"AM": "available", "PM": "available"},
            "Wednesday": {"AM": "available", "PM": "available"},
            "Thursday": {"AM": "available", "PM": "available"},
            "Friday": {"AM": "available", "PM": "available"},
            "Saturday": {"AM": "available", "PM": "available"},
            "Sunday": {"AM": "available", "PM": "available"}
        }

    ### Shift and availability string
    def __str__(self):
        schedule = "\n".join(
            [f"{day}: AM - {shift['AM']}, PM - {shift['PM']}" for day, shift in self.availability.items()]
        )
        return (f"Caregiver: {self.name}, Phone: {self.phone}, Email: {self.email}, "
                f"Pay Rate: ${self.pay_rate}/hr, Hours: {self.hours}\n"
                f"Weekly Availability:\n{schedule}")

    ### Set availability function
    def set_availability(self, day, shift, status):
        if day in self.availability and shift in self.availability[day]:
            self.availability[day][shift] = status
            return f"{day} {shift} shift availability updated to: {status}"
        else:
            return "Invalid day or shift. Please enter a valid day and shift (AM/PM)."


### Establish 8 caregivers
caregiver1 = Caregiver(name = "Gigi", phone = "555-1234", email = "gigi@example.com", pay_rate = 20.0)

caregiver2 = Caregiver(name = "Noel", phone = "111-1234", email = "noel@example.com", pay_rate = 20.0)

caregiver3 = Caregiver(name = "Joe", phone = "222-1234", email = "joe@example.com", pay_rate = 20.0)

caregiver4 = Caregiver(name = "Silvia", phone = "333-1234", email = "silvia@example.com", pay_rate = 20.0)

caregiver5 = Caregiver(name = "Tess", phone = "444-1234", email = "tess@example.com", pay_rate = 20.0)

caregiver6 = Caregiver(name = "Rosa", phone = "665-1234", email = "rosa@example.com", pay_rate = 20.0)

caregiver7 = Caregiver(name = "Lani", phone = "777-1234", email = "lani@example.com", pay_rate = 20.0)

caregiver8 = Caregiver(name = "Sayed", phone = "888-1234", email = "sayed@example.com", pay_rate = 20.0)

print(caregiver1.set_availability())
print(caregiver1)





### Thomas



### Anthony