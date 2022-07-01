from .prime_numbers import is_prime
from rich.terminal_theme import TerminalTheme
from .o import console

discord_theme = TerminalTheme(
    (39, 41, 46),
    (255, 255, 255),
    [
        (0, 0, 0),
        (0, 200, 0),
        (0, 200, 0),
        (255, 255, 0),
        (100, 100, 255),
        (128, 0, 128),
        (0, 255, 255),
        (160, 187, 255),
    ],
    [
        (160, 187, 255),
        (255, 0, 0),
        (0, 255, 0),
        (255, 255, 0),
        (0, 0, 255),
        (255, 141, 255),
        (0, 255, 255),
        (255, 255, 255),
    ],
)
