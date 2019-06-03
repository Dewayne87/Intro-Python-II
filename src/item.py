class Item:
    def __init__(self, name,description):
        self.name = name
        self.description = description 
        
    def __str__(self):
        output = f"This is a {self.name}!"
        output += f"\n {self.description}" 
        return output
    def on_take(self):
        print(f"You have picked up {self.name}")
        
    def on_drop(self):
        print(f"You have dropped {self.name}")