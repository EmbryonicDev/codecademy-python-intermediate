class FishInventory:
    def __init__(self, fishList):
        self.available_fish = fishList


fish_inventory_cls = FishInventory(["Bubbles", "Finley", "Moby"])

# Write your code below:
for x in fish_inventory_cls:
    print(x)
