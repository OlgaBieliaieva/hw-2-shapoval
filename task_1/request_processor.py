import random
import time
from request_queue import Request_queue

class Request_processor:
    def __init__(self):
        self.request_queue = Request_queue()

    def run(self):
        while True:
            if random.random() < 0.7:
                self.request_queue.generate_request()
            self.request_queue.process_request()
            time.sleep(1)