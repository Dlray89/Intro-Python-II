# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name=None, current_room=None):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def push(self, item):
        self.inventory.append(item)

    def pop(self):
        if len(self.inventory) < 1:
            return None
        return self.inventory.pop(0)

    def show(self):
        print(self.inventory)

    def size(self):
        return len(self.inventory)

    def __str__(self):
        return f"{self.name}, {self.current_room}, {self.inventory}, {self.item}"


player = Player('dave')
player.push('knife')
print(player.inventory)
player.pop()
print('new inventory: ', player.inventory)
player.push('torch')
player.push('hammer')
print(player.inventory)
print(player.size())





