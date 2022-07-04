from util import (
    ERROR,
    INFO,
    WARNING,
    DEBUG,
    console,
    errors,
)
from rich.tree import Tree
startup_message = (

"[bold green]Welcome[/] to [bold purple][link=https://github.com/Advik-B/Aseprite-Compiler]Aseprite-Compiler[/][/].\n"
"[bold purple]Aseprite-Compiler[/] is a CLI tool for compiling [bold blue link=https://www.aseprite.org]Aseprite[/] from its [italic cyan link=https://github.com/Aseprite/Aseprite]source code.[/]\n"
"[italic bold green]Some technical details:[/]\n"
)

deps = Tree(label="There are the dependencies that Aseprite-Compiler needs to run.")
deps.add('[italic bold red link=https://git-scm.com]Git[/] [bold white](Version Control System)[/]')
deps.add('[italic bold blue link=https://github.com/Aseprite/Aseprite]Aseprite[/] [bold white](Source-Code)[/]')
deps.add('[italic bold green link=https://github.com/aseprite/skia]Skia[/] [bold white](Library)[/]')
deps.add('[italic bold cyan link=https://cmake.org]CMake[/] [bold white](Build-System)[/]')
deps.add('[italic bold purple link=https://ninja-build.org/]Ninja[/] [bold white](Build-System/Assembler)[/]')
deps.add('[italic bold magenta link=https://visualstudio.microsoft.com/downloads/]Visual Studio Build Tools[/] [bold white](Compiler)[/]')
deps.add('[italic bold Yellow link=https://developer.microsoft.com/en-us/windows/downloads/windows-sdk/]Windows SDK[/] [bold white](Software Development Kit)[/]')

console.print(
    startup_message,
    deps,
    highlight=True,
)
