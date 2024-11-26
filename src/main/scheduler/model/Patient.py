
import sys
sys.path.append("../util/*")
sys.path.append("../db/*")
from util.Util import Util
from db.SQLs import show_appointment_patient_details
from util import services
class Patient:
    pass
    def __init__(self, username, password=None, salt=None, hash=None):
        self.username = username
        self.password = password
        self.salt = salt
        self.hash = hash

    # getters
    def get(self):
        return_ob = None
        curr_salt, curr_hash = services.get_patient_by_name(self.username)
        calculated_hash = Util.generate_hash(self.password, curr_salt)
        if curr_hash == calculated_hash:
            self.salt = curr_salt
            self.hash = calculated_hash
            return_ob = self
        else:
            # print("Incorrect password")
            pass

        return return_ob

    def get_username(self):
        return self.username

    def get_salt(self):
        return self.salt

    def get_hash(self):
        return self.hash

    def save_to_db(self):
        services.insert_patient(self.username, self.salt, self.hash)
        
    def show_appointments(self) -> list[list]:
        sql = show_appointment_patient_details
        return services.show_appointment(sql, self.username)