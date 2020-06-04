
class Item:
    def __init__(self, name, short_name):
        self.name = name
        self.short_name = short_name
        

    def about_item(self):
        print(f'This item is a {self.name}. and its purpose is to {self.short_name}')

map = Item('map', 'search for directions')
map.about_item()

        