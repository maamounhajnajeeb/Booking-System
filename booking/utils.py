class Request:
    def __init__(self, request) -> None:
        self.request = request
        self.data = {}
    
    def retrieve_from(self, request_data):
        for key, value in request_data.items():
            self.data[key] = value
        self.data["user"] = self.request.user.pk
        