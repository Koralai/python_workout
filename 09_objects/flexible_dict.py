class FlexibleDict(dict):
    def __getitem__(self, __key):
        if __key not in self:
            if int(__key) in self:
                return super().__getitem__(int(__key))
            elif str(__key) in self:
                return super().__getitem__(str(__key))
            else:
                return 'Key not found.'
        
        return super().__getitem__(__key)

fd = FlexibleDict()

fd[1] = 100
print(fd['1'])

fd['23'] = 'hello'
print(fd[23])
