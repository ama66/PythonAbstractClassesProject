from abc import ABCMeta, abstractmethod
class PowerPlant(metaclass=ABCMeta):
    def __init__(self):
        print(" powerplant Object Created")
    @abstractmethod
    def lightoff(self):
        pass
    @abstractmethod
    def shutdown(self):
        pass
    
