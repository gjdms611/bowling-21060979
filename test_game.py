from game import Game


def test_gutter_game():
    game = Game()
    for _ in range(20):
        game.roll(0)
    assert game.score() == 0


def test_spare_bonus():
    game = Game()
    game.roll(5)
    game.roll(5)
    game.roll(3)
    for _ in range(17):
        game.roll(0)
    assert game.score() == 16
