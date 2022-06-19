
class OpenFile():
    def __init__(self):
        self.name=""
    def open_with_mode(self,name,mode):
        self.name=name
        try:
            self.fajl=open(self.name,mode)
        except FileNotFoundError:
            return -1
    def write_in_file(self,text):
        self.fajl.write(text)
    def read_from_file(self):
        return self.fajl.read()
