from ic_scoop import Scoop

class Bowl:
    def __init__(self):
        self.current_scoops = []
        self.max_scoops = 3
    
    def add_scoops(self, *new_scoops: Scoop):
        num_scoops = len(self.current_scoops)
        for scoop in new_scoops:
            num_scoops += 1
            if num_scoops <= self.max_scoops:
                self.current_scoops.append(scoop)
    
    def __repr__(self):
        return ', '.join(s.flavor for s in self.current_scoops)

s_1 = Scoop('coffee')
s_2 = Scoop('vanilla')
s_3 = Scoop('chocolate fudge')
s_4 = Scoop('caramel swirl')

b = Bowl()
b.add_scoops(s_1)
b.add_scoops(s_2, s_3)
b.add_scoops(s_4)
print(b)
