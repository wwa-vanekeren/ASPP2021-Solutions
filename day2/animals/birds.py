# Writes file to destination folder
#Birds module
class Birds:
    def __init__(self): 
        ''' Constructor for this class. ''' 
        # Create some member animals 
        self.members = ['Seagul', 'Pigeon'] 
  
  
    def printMembers(self): 
        print('Printing members of the Birds class') 
        for member in self.members: 
           print('\t%s ' % member) 