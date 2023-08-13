from ic_scoop import Scoop

class Bowl:
    def __init__(self, current_scoops=[]):
        self.current_scoops = current_scoops
        
    def add_scoops(self, *new_scoops):
        for scoop in new_scoops:
            self.current_scoops.append(scoop.flavor)

s_1 = Scoop('coffee')
s_2 = Scoop('vanilla')
s_3 = Scoop('chocolate fudge')

b = Bowl()
b.add_scoops(s_1)
b.add_scoops(s_2, s_3)
print(b.current_scoops)
