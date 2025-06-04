# Edu-Dungeon
# 🧠 Wiskunde Dungeon Crawler

Een educatieve dungeon crawler waarin je wiskundemonsters verslaat door wiskundevragen op te lossen! Verzamel goud, koop items, level omhoog en gebruik je kladblok en ideeënbord om te winnen.

## Features

- **Interactieve landkaart**: Kies een eiland en krijg bijpassende wiskundevragen.
- **Monsters**: Versla unieke monsters met elk hun eigen vraag en loot.
- **Winkel**: Koop handige items met goud dat je verdient.
- **Inventaris**: Bekijk je verzamelde items. Klik met links om een item te
  gebruiken, rechts om het te verkopen.
- **Kladblok**: Maak aantekeningen of tekeningen tijdens het spelen.
- **Ideeënbord**: Typ vrij je ideeën of tussenantwoorden op een wit bord.
- **XP & Leveling**: Verdien XP, stijg in level en zie je voortgang in een XP-bar.
- **Sprite-afbeeldingen**: Monsters en winkelier worden als sprites weergegeven.
- **Volledig met muis en toetsenbord te bedienen.**

## Installatie

1. **Vereisten**
   - Python 3.8+
   - [pygame](https://www.pygame.org/)
   - [requests](https://pypi.org/project/requests/)
   - [duckduckgo_search](https://pypi.org/project/duckduckgo-search/) (optioneel, voor monsterplaatjes)
   - [sympy](https://pypi.org/project/sympy/) (voor sommige item-effecten)

   Installeer dependencies:
   ```bash
   pip install pygame requests duckduckgo_search sympy
   ```

2. **Project downloaden**
   - Download of clone deze repository.
   - Zorg dat alle assets (`Goudstukken.png`, `Landkaart.png`, `winkelier.png`, `assets/monsters/`) in de juiste map staan.

3. **Start het spel**
   ```bash
   python main.py
   ```

## Exporteren als .exe

Wil je het spel als `.exe` delen? Gebruik [PyInstaller](https://pyinstaller.org/):

```bash
pip install pyinstaller
pyinstaller main.py --onefile --windowed --add-data "Goudstukken.png;." --add-data "Landkaart.png;." --add-data "winkelier.png;." --add-data "assets;assets"
```
De `.exe` vind je in de `dist/` map.

## Besturing

- **Muis**: Klik op knoppen, eilanden, winkelitems, etc.
- **Toetsenbord**: Typ je antwoord, gebruik het ideeënbord, kladblok, etc.

## Relatieve paden

Alle assets worden via een helperfunctie (`resource_path`) geladen, zodat het spel werkt op elke computer én als .exe.

## Credits

- **Code**: Tiago Geerdink & contributors
- **Sprites**: DuckDuckGo, eigen werk, en rechtenvrije bronnen
- **Muziek/SFX**: (optioneel, voeg toe indien van toepassing)

## Licentie

MIT-licentie (of eigen keuze)

---

Veel plezier met spelen en leren! 🎲🧠
