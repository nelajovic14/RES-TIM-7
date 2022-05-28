class Message:
    def __init__(self, id, potrosnja):
        self.id = id
        self.potrosnja = potrosnja
    def __str__(self):
        return self.id + " " + self.potrosnja