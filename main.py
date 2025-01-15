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

class EventQueue:
    def _init_(self):
        self.queue = []
        self.handlers = {}

    def emit(self,event):
        self.queue.append(event)
        print(f"Event '{event.name}' emitted")

    def register_handler(self, event_name, handler):
        self.handlers[event_name] = handler
    
    def process_events(self):
        while self.queue:
            event = self.queue.pop(0)
            if event.name in self.handlers:
                handler = self.handlers[event.name]
                handler(event)
            else:
                print(f"No handler registered for event: {event.name}")

communication_queue = EventQueue()

