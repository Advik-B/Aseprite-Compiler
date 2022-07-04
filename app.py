from util import (
    ERROR,
    INFO,
    WARNING,
    DEBUG,
    console,
    errors,
)
from rich.tree import Tree
from rich.theme import Theme
from rich.panel import Panel

custom_style = Theme(
    {"br": "white", "dep": "italic bold"},
)
console.push_theme(custom_style)


startup_message = (
    "[bold green]Welcome[/] to [bold purple][link=https://github.com/Advik-B/Aseprite-Compiler]Aseprite-Compiler[/][/].\n"
    "[bold purple]Aseprite-Compiler[/] is a CLI tool for compiling [bold blue link=https://www.aseprite.org]Aseprite[/] from its [italic cyan link=https://github.com/Aseprite/Aseprite]source code.[/]\n"
    "[italic bold green]Some technical details:[/]\n"
)

deps = Panel(
    "1. [italic bold red link=https://git-scm.com]Git[/] [bold white](Version Control System)[/]\n"
    "2. [italic bold blue link=https://github.com/Aseprite/Aseprite]Aseprite[/] [bold white](Source-Code)[/]\n"
    "3. [italic bold green link=https://github.com/aseprite/skia]Skia[/] [bold white](Library)[/]\n"
    "4. [italic bold cyan link=https://cmake.org]CMake[/] [bold white](Build-System)[/]\n"
    "5. [italic bold purple link=https://ninja-build.org/]Ninja[/] [bold white](Build-System/Assembler)[/]\n"
    "6. [italic bold magenta link=https://visualstudio.microsoft.com/downloads/]Visual Studio Build Tools[/] [bold white](Compiler)[/]\n"
    "7. [italic bold Yellow link=https://developer.microsoft.com/en-us/windows/downloads/windows-sdk/]Windows SDK[/] [bold white](Software Development Kit)[/]\n",
    title="There are the dependencies that Aseprite-Compiler needs.",
    highlight=True,
)

steps = Panel(
    "1. Check if any of the dependencies are missing on your system. [italic green][br]([/]Usally [cyan]fast[/][br])[/][/]\n"
    "2. Download the dependencies if they are missing. [italic yellow][br]([/]This will take [italic white]some[/] time[br])[/][/]\n"
    "3. Temporarily install the dependencies. [italic yellow][br]([/]This will take [italic white]some[/] time[br])[/][/]\n"
    "4. Compile Aseprite. [italic yellow][br]([/]This will take [bold white]A LOT[/] of time[br])[/][/]\n",
    highlight=True,
    title="There are the details on how [bold purple]Aseprite-Compiler[/] works.",
)
console.print(
    startup_message,
    deps,
    steps,
    highlight=True,
)
