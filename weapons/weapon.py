from abc import ABCMeta, abstractmethod
class weapon(metaclass=ABCMeta):
    def __init(self):
        print("Weapon Object Created")
    @abstractmethod
    def fire(self):
        pass
    @abstractmethod
    def aim(self):
        pass
    
