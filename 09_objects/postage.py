class Envelope:
    def __init__(self, weight=0.4):
        self.was_sent = False
        self.postage = 0
        self.weight = weight
    
    def postage_needed(self):
        return self.weight
    
    def add_postage(self, new_postage):
        self.postage += new_postage
    
    def send(self):
        if self.postage >= self.postage_needed():
            self.was_sent = True
            print('Letter sent.')
        else:
            print('More postage needed!')

my_letter = Envelope()
my_letter.send()
my_letter.add_postage(0.63)
my_letter.send()
