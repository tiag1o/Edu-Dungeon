import random

def koop_item(game, index):
    item = game.winkel_actief[index]
    if game.goud >= item["prijs"]:
        game.goud -= item["prijs"]
        game.feedback = f"✅ Je hebt '{item['naam']}' gekocht!"
        game.inventory.append(item)
        # 🔄 Vervang met nieuw item (als er nog andere beschikbaar zijn)
        overgebleven = [i for i in game.winkel if i not in game.winkel_actief]
        if overgebleven:
            nieuw_item = random.choice(overgebleven)
            game.winkel_actief[index] = nieuw_item
        else:
            game.winkel_actief.pop(index)  # niks meer over
    else:
        game.feedback = f"❌ Niet genoeg goud voor '{item['naam']}'"
