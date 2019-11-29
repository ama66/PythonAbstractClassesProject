from weapons.torpedo import Torpedo
from powerplants.markvreactor import MarkVReactor

def main():
    print("Hello World, Fleet Sim Code Using Abstract Classes")
    torpedo=Torpedo()
    torpedo.aim()
    torpedo.fire()
    reactor=MarkVReactor()
    reactor.lightoff()
    reactor.shutdown()
    


if __name__=="__main__":
    main()
    