class Bus:
    
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = []
    
    def drive(self):
        return "Brum brum"
    
    def passenger_count(self):
        return len(self.passengers)
    
    def pick_up(self, person_object):
        self.passengers.append(person_object)
        
    def drop_off(self, person_object):
        self.passengers.remove(person_object)
        
    def empty(self):
        self.passengers = []