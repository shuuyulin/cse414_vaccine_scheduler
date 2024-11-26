from util import services
class Reservation:
    pass
    def __init__(self, id=None, time=None, cusername=None, pusername=None, vname=None):
        self.id = id
        self.time = time
        self.cusername = cusername
        self.pusername = pusername
        self.vname = vname
    
    def get_id(self):
        return self.id

    def get_time(self):
        return self.time
    
    def get_cusername(self):
        return self.cusername
    
    def get_pusername(self):
        return self.pusername

    def save_to_db(self):
        self.id = services.insert_reservation(self.time, self.cusername, self.pusername, self.vname)

