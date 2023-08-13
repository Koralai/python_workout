from ic_scoop import Scoop

def create_scoops(flavor_1, flavor_2, flavor_3):
    """Use the Scoop class to create 3 scoops of ice cream."""
    
    s_1 = Scoop(flavor_1)
    s_2 = Scoop(flavor_2)
    s_3 = Scoop(flavor_3)
    
    scoops = [s_1, s_2, s_3]
    
    print("Scoops created:")
    for scoop in scoops:
        print(f"- {scoop.flavor.capitalize()}")

create_scoops('matcha', 'vanilla', 'strawberry')
