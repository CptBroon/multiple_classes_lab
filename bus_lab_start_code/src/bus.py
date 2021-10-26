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

    def pick_up_from_stop(self, bus_stop_object):
        for person in bus_stop_object.queue:
            self.pick_up(person)
        bus_stop_object.clear()
            
        # self.pick_up([person for person in bus_stop_object.queue])
        
