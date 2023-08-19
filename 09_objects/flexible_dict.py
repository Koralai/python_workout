class FlexibleDict(dict):
    """
    A dictionary that uses type conversion to look up keys.
    Example: dict[1] and dict['1'] are both valid.
    """
    
    def __getitem__(self, __key):
        
        if __key not in self:
            
            # check if the key exists if converted to a string
            if str(__key) in self:
                return super().__getitem__(str(__key))
            
            # only convert the key to an int if it's a string of numbers               
            elif isinstance(__key, str) and __key.isdigit():
                
            # check if the key exists if converted to an int
                if int(__key) in self:
                    return super().__getitem__(int(__key))
            
            else:
                return 'Key not found.'
        
        return super().__getitem__(__key)

fd = FlexibleDict()

fd[1] = 100
print(fd['1'])

fd['23'] = 'hello'
print(fd[23])

print(fd['#'])
