class Event:
    def __init__(self, name, payload):
        self.name = name
        self.payload = payload

class OrderedSubmittedEvent(Event):
    def __init__(self, ordered_number, is_submitted):
        super().__init__("ordered_submitted", {"ordered_number": ordered_number, "is_submitted": is_submitted})

class OrderedRejected(Event):
    def __init__(self, ordered_number, is_rejected):
        super().__init__("ordered_rejected", {"ordered_number": ordered_number, "is_rejected": is_rejected})


class EventQueue:
    def __init__(self):
        self.queue = []
        self.handlers = {}

    def emit(self, event):
        self.queue.append(event)
        print(f"Event '{event.name}' emitted.")

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


class Store:
    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.order_counter = 0

    def ordered_from_customer(self, date):
        self.order_counter += 1
        ordered_number = f"{self.name[:3].upper()}-{self.order_counter:04d}"
        event = OrderedSubmittedEvent(ordered_number, date)
        communication_queue.emit(event)

    def handle_ordered_from_store(self, event):
        print(f"Store '{self.name}' received order submission: {event.payload}")


class Customer:
    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    def handle_ordered_from_store(self, event):
        print(f"Customer '{self.first_name} {self.last_name}' received order update: {event.payload}")
        is_submitted = True
        review_event = OrderedSubmittedEvent(event.payload["ordered_number"], is_submitted)
        communication_queue.emit(review_event)


store1 = Store("Happy", "Ankara", "5553336667")
customer1 = Customer("John", "Doe", "5551112222", "john.doe@example.com")

communication_queue.register_handler("ordered_submitted", store1.handle_ordered_from_store)
communication_queue.register_handler("ordered_submitted", customer1.handle_ordered_from_store)

store1.ordered_from_customer("2025-01-15")

communication_queue.process_events()

     