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


def test_spare_bonus_roll_also_counts_toward_next_frame():
    game = Game()
    game.roll(2)
    game.roll(8)
    game.roll(2)
    game.roll(3)
    for _ in range(16):
        game.roll(0)
    assert game.score() == 17


def test_strike_bonus():
    game = Game()
    game.roll(10)
    game.roll(3)
    game.roll(4)
    for _ in range(16):
        game.roll(0)
    assert game.score() == 24


def test_strike_in_ninth_frame():
    game = Game()
    for _ in range(16):
        game.roll(0)
    game.roll(10)
    game.roll(6)
    game.roll(2)
    assert game.score() == 26


def test_perfect_game():
    game = Game()
    for _ in range(12):
        game.roll(10)
    assert game.score() == 300


def test_tenth_frame_spare_with_bonus_roll():
    game = Game()
    for _ in range(18):
        game.roll(0)
    game.roll(9)
    game.roll(1)
    game.roll(5)
    assert game.score() == 15


def test_tenth_frame_strike_with_bonus_rolls():
    game = Game()
    for _ in range(18):
        game.roll(0)
    game.roll(10)
    game.roll(4)
    game.roll(5)
    assert game.score() == 19


def test_scenario_1():
    game = Game()
    for pins in [8, 2, 9, 0, 9, 1, 10, 7, 1, 10, 6, 3, 10, 6, 3, 10, 8, 0]:
        game.roll(pins)
    assert game.score() == 148


def test_scenario_2():
    game = Game()
    for pins in [10, 9, 1, 7, 0, 9, 1, 10, 10, 8, 2, 10, 9, 1, 9, 1, 7]:
        game.roll(pins)
    assert game.score() == 188


def test_scenario_3_incomplete_last_frame():
    game = Game()
    for pins in [9, 1, 5, 4, 3, 7, 7, 3, 10, 6, 0, 6, 0, 8, 1, 5, 4]:
        game.roll(pins)
    assert game.score() == 107


def test_scenario_4():
    game = Game()
    for pins in [4, 0, 5, 0, 8, 0, 10, 1, 8, 1, 0, 6, 4, 8, 0, 9, 0, 7, 1]:
        game.roll(pins)
    assert game.score() == 89


def test_unresolved_strike_excludes_frame_and_later():
    game = Game()
    for _ in range(7):
        game.roll(1)
        game.roll(1)
    game.roll(10)
    game.roll(10)
    assert game.score() == 14
