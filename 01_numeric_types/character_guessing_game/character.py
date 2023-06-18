class Character:
    """A model of a fictional character"""
    
    def __init__(self, first_name, quote, last_name=''):
        """
        Initial attributes for first name, associated quote, and 
        optional last name
        """
        self.first_name = first_name
        self.quote = quote
        self.last_name = last_name
        
    def get_full_name(self):
        """
        Return the character's full name, depending on whether they have a
        last name or not
        """
        if self.last_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return f"{self.first_name}"
