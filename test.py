from util import console, discord_theme, download
from rich import inspect
from rich.markdown import Markdown
from time import sleep

download('https://github.com/libsdl-org/SDL_ttf/releases/download/release-2.0.18/SDL2_ttf-2.0.18.zip', progressbar='rich')