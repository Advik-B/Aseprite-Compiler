# Install the rich traceback first before anything else.
from rich.traceback import install
from .o import console
install(extra_lines=5, show_locals=True, console=console)

from rich.terminal_theme import TerminalTheme
from .dl import download
from .constants import (
    ERROR,
    DEBUG,
    WARNING,
    INFO,
)  # I am explicitly importing these constants because it helps with type hints and Tests.

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
