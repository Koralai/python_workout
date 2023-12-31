from ice_cream import Scoop

def create_scoops(flavor_1, flavor_2, flavor_3):
    """Use the Scoop class to create 3 scoops of ice cream."""
    
    scoops = [Scoop(flavor_1), 
              Scoop(flavor_2), 
              Scoop(flavor_3)]
    
    print("Scoops created:")
    for scoop in scoops:
        print(f"- {scoop.flavor.capitalize()}")

create_scoops('matcha', 'vanilla', 'strawberry')
