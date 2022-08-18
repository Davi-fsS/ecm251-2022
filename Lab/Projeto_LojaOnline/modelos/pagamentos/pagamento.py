#abc -> abstract class
from abc import ABC, abstractclassmethod

class Pagamento(ABC):
    @abstractclassmethod

    def realizar_pagamento(self):
        pass

    