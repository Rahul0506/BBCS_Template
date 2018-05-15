from datetime import datetime
import time

class ChatBot:
    
    def __init__(self):
        # accepted_messages maps incoming messages to 
        # list of callback functions
        self.accepted_messages = {}
        
        # time of instantiation
        self.birth_time = datetime.now()
        
        # "registering" some basic callbacks
        self.register_callback("hi", 
                               self.respond_to_greeting)
        self.register_callback("bye", 
                               self.respond_to_departure)
        self.register_callback("age?",
                               self.respond_to_age_request)
        self.register_callback("age?",
                               self.respond_to_age_request_detailed)
		
    def register_callback(self, message, callback):
        """
        Registers a callback to a message.
        """
        if message not in self.accepted_messages:
            self.accepted_messages[message] = []
        self.accepted_messages[message].append(callback)
        
    def respond_to_greeting(self):
        return "Hello!"
        
    def respond_to_departure(self):
        return "Nice chatting with you!"
            
    def respond_to_age_request(self):
        age = datetime.now() - self.birth_time
        return "I am" + str(age.seconds) + "seconds old."
        
    def respond_to_age_request_detailed(self):
        age = datetime.now() - self.birth_time
        micros = age.microseconds
        return '{} {} {} {} {}'.format("Technically, I'm", age.seconds, "seconds and", 
              micros, "microseconds old")
        
    def handle_message(self, message):
        if message not in self.accepted_messages:
            return "Sorry, I don't understand " + '\"' + message + '\"'
        else:
            callbacks = self.accepted_messages[message]
            for callback in callbacks:
                return callback()   #ofc this needs to be changed
            #why are there multiple callbacks for each message anyway???
