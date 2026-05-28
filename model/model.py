from .encoder import Name
from .decoder import Decoder

class Model:
    def __init__(self):
        self.encoder = Name("Chaitanya Kohli")
        self.decoder = Decoder()
    
    def forward(self, num1, num2):
        return self.encoder.add(num1, num2), self.decoder.sub(num1, num2)
    