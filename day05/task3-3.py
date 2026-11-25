class Inventory:
    def __init__(self, items):
        self.items = items  

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

inv = Inventory(["pen", "book", "pencil"])
print("Total items:", len(inv))  
print("Item 0:", inv[0])  
print("Item 1:", inv[1])
print("Item 2:", inv[2])