import queue
import random
import time
from request import Request

class Request_queue:
    def __init__(self):
        self.queue = queue.Queue()
        self.request_id = 0

    def generate_request(self):
        request = Request(self.request_id, f'Request data for ID {self.request_id}')
        self.queue.put(request)
        print(f"Generated and added request: {request}")
        self.request_id += 1

    def process_request(self):
        if not self.queue.empty():
            request = self.queue.get()
            print(f"Processing request: {request}")
            time.sleep(1)
            print(f"Finished processing request ID {request.request_id}")
        else:
            print("The queue is empty, no requests to process.")