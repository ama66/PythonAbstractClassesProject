from abc import ABCMeta, abstractmethod
class Vessel(metaclass=ABCMeta):
    def __init__(self,weapon,powerplant):
        self.powerplant=powerplant
        self.weapon=weapon
        print("vessel Object Created")
    @abstractmethod
    def lightoff_plant(self):
        pass
    @abstractmethod
    def shutdown_plant(self):
        pass
    @abstractmethod
    def aim_weapon(self):
        pass
    @abstractmethod
    def fire_weapon(self):
        pass

    
