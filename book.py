class Book():
    def __init__(self,name,author,self_no,serial_no,available= False):
        self.name = name
        self.author = author
        self.self_no = str(self_no)
        self.serial_no = str(serial_no)
        self.available = str(available)

    def get_detail(self):
        l = [self.name,self.author,self.self_no,self.serial_no,self.available]
        return l
