# Install the rich traceback first before anything else.
# I am explicitly importing these constants because it helps with type
# hints and Tests.
from rich.terminal_theme import TerminalTheme
from rich.traceback import install

from .constants import DEBUG, ERROR, INFO, WARNING
from .dl import download
from .o import console

install(extra_lines=5, show_locals=True, console=console)

import os
import platform

OS = platform.system().casefold()


def find_executable_in_path(executable, multiple=False):
    """
    Finds the path of an executable.
    """
    if OS == "windows" and not executable.endswith(".exe"):
        executable += ".exe"
    executables = []
    path = os.environ["PATH"]
    for directory in path.split(os.pathsep):
        if os.path.exists(os.path.join(directory, executable)):
            executables.append(os.path.join(directory, executable))

    if len(executables) == 0:
        return None

    if multiple:
        return tuple(executables)
    else:
        return executables[0]



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
