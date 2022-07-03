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
# "For this. it will:\n"
# "   - [bold green]Download[/] the latest version of [italic bold red][link=https://git-scm.com]git[/][/]\n"
# "   - [bold green]Download[/] Aseprite source code from [italic bold white link=https://github.com]github[/] using [italic bold red]git[/]\n"
)

workflow = Tree(label="There are the dependencies that Aseprite-Compiler needs to run.")
workflow.add('[italic bold red link=https://git-scm.com]Git[/] [bold white](Version Control System)[/]')
workflow.add('[italic bold blue link=https://github.com/Aseprite/Aseprite]Aseprite[/] [bold white](Source-Code)[/]')
workflow.add('[italic bold green link=https://github.com/aseprite/skia]Skia[/] [bold white](Library)[/]')
workflow.add('[italic bold cyan link=https://cmake.org]CMake[/] [bold white](Build-System)[/]')
workflow.add('[italic bold purple link=https://ninja-build.org/]Ninja[/] [bold white](Build-System/Assembler)[/]')
workflow.add('[italic bold magenta link=https://visualstudio.microsoft.com/downloads/]Visual Studio Build Tools[/] [bold white](Compiler)[/]')
# workflow.add('[italic bold white link=https://visualstudio.microsoft.com/downloads]Microsoft Visual C++ Redistributable[/] [bold white](Compiler)[/]')
workflow.add('[italic bold Yellow link=https://developer.microsoft.com/en-us/windows/downloads/windows-sdk/]Windows SDK[/] [bold white](Software Development Kit)[/]')

console.print(
    startup_message,
    workflow,
    highlight=True,
)
