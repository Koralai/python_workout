class FlexibleDict(dict):
    def __getitem__(self, __key):
        if __key not in self:
            return 'Key not found.'
        
        return super().__getitem__(__key)

fd = FlexibleDict()

fd[1] = 100
print(fd['1'])
