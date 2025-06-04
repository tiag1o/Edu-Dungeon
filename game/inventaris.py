import random

def toggle_inventaris(game):
    game.inventaris_open = not game.inventaris_open

def verkoop_item(game, item):
    verkoop_percentage = random.randint(10, 300)
    verkoopprijs = int(item["prijs"] * verkoop_percentage / 100)
    game.goud += verkoopprijs
    game.inventory.remove(item)
    game.feedback = f"💰 Verkocht voor {verkoopprijs} goud ({verkoop_percentage}%)"
