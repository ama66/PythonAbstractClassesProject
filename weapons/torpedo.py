from weapons.weapon import Weapon
class Torpedo(Weapon):
    ## Call Superclass constructor 
    def __init__(self):
        super(Torpedo,self).__init__()
        print("Torpedo typoe weapon object created")
    def aim(self):
        print("Torpedo being aimed and ready to fire!")
    def fire(self):
        print("Torpedo away...swoosh.....zzzzz...KABOOM!")