### Main calendar program


### Virgil
import calendar
import random



#amShift = ["7:00 AM - 1:00 PM"]
#pmShift = ["1:00 PM - 7:00 PM"]
day = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat","Sun"]
person = ["Gigi", "Noel", "Joe", "Silvia","Tess", "Rosa", "Lani", "Sayed"]



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

    def __str__(self):
        schedule = "\n".join(
            [f"{day}: AM - {shift['AM']}, PM - {shift['PM']}" for day, shift in self.availability.items()]
        )
        return (f"Caregiver: {self.name}, Phone: {self.phone}, Email: {self.email}, "
                f"Pay Rate: ${self.pay_rate}/hr, Hours: {self.hours}\n"
                f"Weekly Availability:\n{schedule}")

    def set_availability(self, day, shift, status):
        """Set the availability for a specific day and shift (AM or PM)."""
        if day in self.availability and shift in self.availability[day]:
            self.availability[day][shift] = status
            return f"{day} {shift} shift availability updated to: {status}"
        else:
            return "Invalid day or shift. Please enter a valid day and shift (AM/PM)."
























### Thomas



### Anthony