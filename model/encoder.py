class Name:
    def __init__(self, your_name:str):
        self.name = "your name" if your_name is None else your_name

    def add(self, num1, num2):
        return num1+num2
    
    def get_name(self):
        return self.name