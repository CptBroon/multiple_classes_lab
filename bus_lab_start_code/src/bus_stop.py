class BusStop:
    def __init__(self, name):
        self.name = name 
        self.queue = []

    def queue_length(self):
        return len(self.queue)

    def add_to_queue(self, person_object):
        self.queue.append(person_object)
    
    def clear(self):
        self.queue = []