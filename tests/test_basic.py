import os
import sys
import pathlib

os.environ['SDL_VIDEODRIVER'] = 'dummy'

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import py_compile
import pygame


def test_compile_all():
    for path in pathlib.Path('.').rglob('*.py'):
        py_compile.compile(str(path), doraise=True)


def test_game_initialisation():
    pygame.init()
    screen = pygame.display.set_mode((1, 1))
    from game.engine import Game
    game = Game(screen)
    assert game.scherm is screen
    pygame.quit()


def test_item_effects():
    pygame.init()
    screen = pygame.display.set_mode((1, 1))
    from game.engine import Game
    from game.items import item_effects
    game = Game(screen)
    for func in item_effects.values():
        func(game)
    pygame.quit()


def test_shop_and_inventory():
    pygame.init()
    screen = pygame.display.set_mode((1, 1))
    from game.engine import Game
    game = Game(screen)
    game.goud = 100
    game.koop_item(0)
    assert len(game.inventory) == 1
    item = game.inventory[0]
    game.verkoop_item(item)
    assert item not in game.inventory
    pygame.quit()
