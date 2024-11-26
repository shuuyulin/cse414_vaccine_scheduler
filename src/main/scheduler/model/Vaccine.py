import sys
sys.path.append("../util/*")
from util import services

class Vaccine:
    def __init__(self, vaccine_name, available_doses):
        self.vaccine_name = vaccine_name
        self.available_doses = available_doses

    # getters
    def get(self):
        self.available_doses = services.get_doses_by_vaccine_name(self.vaccine_name)
        if self.available_doses:
            return self
        else:
            return None

    def get_vaccine_name(self):
        return self.vaccine_name

    def get_available_doses(self):
        return self.available_doses

    def save_to_db(self):
        if self.available_doses is None or self.available_doses <= 0:
            raise ValueError("Argument cannot be negative!")
        services.insert_vaccine(self.vaccine_name, self.available_doses)

    # Increment the available doses
    def increase_available_doses(self, num:str):
        if num <= 0:
            raise ValueError("Argument cannot be negative!")
        self.available_doses += num
        services.update_vaccine(self.available_doses, self.vaccine_name)

    # Decrement the available doses
    def decrease_available_doses(self, num:str):
        if self.available_doses - num < 0:
            ValueError("Not enough available doses!")
        self.available_doses -= num
        services.update_vaccine(self.available_doses, self.vaccine_name)

    def __str__(self):
        return f"(Vaccine Name: {self.vaccine_name}, Available Doses: {self.available_doses})"
