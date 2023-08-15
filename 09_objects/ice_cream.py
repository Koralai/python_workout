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
        num_scoops = len(self.current_scoops)
        for scoop in new_scoops:
            num_scoops += 1
            if num_scoops <= Bowl.MAX_SCOOPS:
                self.current_scoops.append(scoop)
    
    def __repr__(self):
        return ', '.join(s.flavor for s in self.current_scoops)
    