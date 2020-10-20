class Person: 
    name = 'Ali' 
    def __repr__(self): 
        return repr(self.name) 

repr(Person()) 
