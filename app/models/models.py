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

def convertir_tiempo(t_a: opcional[float] = 0, 
                     t_m: opcional[float] = 0, 
                     t_d: opcional[float] = 0) -> float:
   
    tiempo = 0.0
    if t_a:
        tiempo += t_a
    if t_m:
        tiempo += t_m / 12
    if t_d:
        tiempo += t_d / 365
    
    if tiempo == 0:
        raise ValueError("Se debe proporcionar al menos uno de los valores de tiempo: t_a, t_m o t_d")
    
    return tiempo


class Interes_Simple(BaseModel):
    Vf:opcional[float]=None
    Vi:opcional[float]=None
    i:opcional[float]=None
    t_a:opcional[float]=None
    t_m:opcional[float]=None
    t_d:opcional[float]=None
    t: opcional[float] = None 
   
    def calcular_valor_futuro(self):
        tiempo = convertir_tiempo(self.t_a, self.t_m, self.t_d)
        self.Vf = self.Vi * (1 + (self.i/100) * tiempo)
        interes = self.Vf - self.Vi
        return { round(self.Vf, 2), round(interes, 2)}


    def calcular_valor_inicial(self):
        self.Vi = self.Vf / (1 + (self.i/100) * convertir_tiempo(self.t_a, self.t_m, self.t_d))
        return self.Vi
     
    def calcular_tiempo(self):
            if not self.Vi or not self.Vf or not self.i:
                raise ValueError("Faltan Vf, Vi o i para calcular el tiempo")
            self.t = ((self.Vf / self.Vi) - 1) /(self.i/100)
            return self.t

    
class Interes_compuesto(BaseModel):
    Vf:opcional[float]=None
    Vp:opcional[float]=None
    i:opcional[float]=None
    n:opcional[float]=None

    def calcular_valor_futuro(self):
        self.Vf=self.Vp*math.pow((1+(self.i/100)),self.n)
        return self.Vf
    
    def calcular_tasa_de_interes(self):
        self.i=math.pow((self.Vf/self.Vp),(1/self.n))-1
        return self.i*100
    
    def calcular_tiempo_necesario(self):
        self.n=(math.log(self.Vf)-math.log(self.Vp))/math.log(1+(self.i/100))
        return self.n

