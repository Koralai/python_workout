class Scoop:
    """A simple model of an ice cream scoop"""
    
    def __init__(self, flavor):
        """Define an attribute for the flavor of the scoop"""
        self.flavor = flavor

class Bowl:
    MAX_SCOOPS = 3
    
    def __init__(self):
        self.current_scoops = []
    
    def add_scoops(self, *new_scoops: Scoop):
        for scoop in new_scoops:
            if len(self.current_scoops) < self.MAX_SCOOPS:
                self.current_scoops.append(scoop)
    
    def __repr__(self):
        return ', '.join(s.flavor for s in self.current_scoops)

class BigBowl(Bowl):
    MAX_SCOOPS = 5
