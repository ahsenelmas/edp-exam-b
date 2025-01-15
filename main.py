class Event:
    def __init__(self, name,payload):
        self.name = name
        self.payload = payload

class OrderedSubmittedEvent(Event):
    def __init__(self, ordered_number, is_submitted):
        super().__init__("ordered_submitted", {"ordered_number": ordered_number, "is_submitted": is_submitted})

class OrderedRejected(Event):
    def __init__(self, ordered_number, is_rejected):
        super().__init__("ordered_rejected", {"ordered_number": ordered_number, "is_rejected": is_rejected})

