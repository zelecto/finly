from pydantic import BaseModel
from typing import Optional as opcional 
import math

class Anualidad(BaseModel):
    vf:opcional[float]=None
    va:opcional[float]=None
    i:float
    n:float
    A:float

    def calcular_valor_futuro_anualidad(self):
        self.vf=self.A*(((math.pow((1+(self.i/100)),self.n)-1)/(self.i/100)))
        return self.vf

    def calcular_valor_anualidad(self):
        self.va=self.A*(((1-(math.pow((1+(self.i/100)),-self.n)))/(self.i/100)))
        return self.va
        