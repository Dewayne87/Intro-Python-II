# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name,description,items=[]):
        self.name = name
        self.description = description 
        self.items = items
        
    def __str__(self):
        num = 1
        output = f"{self.name} room!"
        output += f"\n {self.description}" 
        if len(self.items) < 1:
            output += "\n There are no items in this room"
        else:
            output += "\n The Items in this room are:"
            for i in self.items:
                output += "\n " + str(num) + ". " + str(i)
                num +=1
        return output
