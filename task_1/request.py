class Request:
    def __init__(self, request_id, data):
        self.request_id = request_id
        self.data = data

    def __repr__(self):
        return f"Request(id={self.request_id}, data='{self.data}')"