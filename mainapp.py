from weapons.torpedo import Torpedo
from powerplants.markvreactor import MarkVReactor
from vessels.submarine import Submarine

def main():
    # print("Hello World, Fleet Sim Code Using Abstract Classes")
    # torpedo=Torpedo()
    # torpedo.aim()
    # torpedo.fire()
    # reactor=MarkVReactor()
    # reactor.lightoff()
    # reactor.shutdown()
    submarine=Submarine(Torpedo(),MarkVReactor())
    submarine.lightoff_plant()
    submarine.aim_weapon()
    submarine.fire_weapon()
    submarine.shutdown_plant()
    



if __name__=="__main__":
    main()
    