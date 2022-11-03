import fantasy_game_inventory

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = {'gold coin': 42, 'rope': 1}

def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item not in inventory:
            inventory.setdefault(item, 1)
        else:
            inventory[item] += 1
    return inventory

inv = addToInventory(inv, dragonLoot)
fantasy_game_inventory.displayInventory(inv)