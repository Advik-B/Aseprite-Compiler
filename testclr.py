from util.scaffolding import console
from rich.terminal_theme import TerminalTheme

discord = TerminalTheme(
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



console.log("TerminalTest initilized", log_locals=True)
with open('out.html', 'wb') as f:
    f.write(console.export_html(theme=discord).encode('utf-8'))
