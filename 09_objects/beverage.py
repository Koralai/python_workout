class Beverage:    
    def __init__(self, name, container='cup', temp=75):
        self.name = name
        self.container = container
        self.temp = temp
        
    def serve(self):
        print(f"Serving a {self.container} of {self.name} at {self.temp}°F.")
        
bev_list = [Beverage('green tea', 'mug', 140), 
            Beverage('water'), 
            Beverage('boba tea', temp=42), 
            Beverage('pinot noir', 'glass', 60)]

for bev in bev_list:
    bev.serve()
