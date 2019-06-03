# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name,current_room,items=[]):
        self.name = name
        self.current_room = current_room 
        self.items = items
    def current_items(self):
        num = 1
        item_output = "\n The items in your inventory are:"
        if len(self.items) < 1:
            item_output += "\n You are currently holding no items."
        else:
            for i in self.items:
                item_output +=  "\n" + str(num) + " " + str(i)
                num +=1
        print(item_output)
    def get_item(self,item_name):
        for n in self.current_room.items:
            if n.name == item_name:
                n.on_take()
                self.items.append(n)
                self.current_room.items.remove(n)
            else:
                print("No item by that name")

    def drop_item(self,item_name):
        for n in self.items:
            if n.name == item_name:
                n.on_drop()
                self.current_room.items.append(n)
                self.items.remove(n)
            else:
                print("No item by that name")

    def __str__(self):
        num = 1
        output = f"You are in the {self.current_room} room!"
        if len(self.items) < 1:
            output += "\n You are currently holding no items."
        else:
            output += "\n The items in your inventory are:"
            for i in self.items:
                output += "\n" + str(num) + ". " + str(i)
                num += 1
        return output
