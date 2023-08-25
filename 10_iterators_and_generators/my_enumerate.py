class MyEnumerate:
    def __init__(self, data):
        self.data = data
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration

        value = self.data[self.index]
        current_index = self.index
        self.index += 1
        return (current_index, value)

for index,letter in enumerate('abc'):
    print(f'{index}: {letter}')
        
for index, letter in MyEnumerate('abc'):
    print(f'{index}: {letter}')
