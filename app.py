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

workflow = Tree(label="")
workflow.add('[italic bold red][link=https://git-scm.com]Git[/][/]')
workflow.add('[italic bold blue]Aseprite (source code)[/]')
workflow.add('CMake')

console.print(
    startup_message,
    workflow,
    highlight=True,
)