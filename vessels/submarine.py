from vessels.vessel import Vessel
class Submarine(Vessel):
    def __init__(self,weapon,powerplant):
        ## Call constructor of the base/super class passing weapon and powerplant
        super(Submarine,self).__init__(weapon,powerplant)
        print("Submarine object created!")
    def lightoff_plant(self):
        self.powerplant.lightoff()
    def shutdown_plant(self):
        self.powerplant.shutdown()
    def aim_weapon(self):
        self.weapon.aim()
    def fire_weapon(self):
        self.weapon.fire()



