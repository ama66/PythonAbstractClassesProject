from abc import ABCMeta, abstractmethod
class powerplant(metaclass=ABCMeta):
    def __init(self):
        print(" powerplant Object Created")
    @abstractmethod
    def lightoff(self):
        pass
    @abstractmethod
    def shutdown(self):
        pass
    
