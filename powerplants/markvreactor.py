from powerplants.powerplant import PowerPlant

class MarkVReactor(PowerPlant):

    def __init__(self):
        super(MarkVReactor,self).__init__()
        print("MarkV Reactor is created!")

    def lightoff(self):
        print("MarkV Reactor is powered up and ready to answer all bells!")

    def shutdown(self):
        print("MarkV Reactor is shut down ...Cold and Dark!")
    
    