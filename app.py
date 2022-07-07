import os
import re
import subprocess
import sys
from os.path import join as pjoin
from time import sleep
from tkinter import filedialog

from rich.panel import Panel
from rich.table import Table
from rich.theme import Theme
from rich.tree import Tree

from util import (
    DEBUG,
    ERROR,
    INFO,
    WARNING,
    console,
    errors,
    find_executable_in_path,
    OS,
)

custom_style = Theme(
    {"br": "white", "dep": "italic bold"},
)
console.push_theme(custom_style)

if OS == "windows":
    path_step = "\\"
else:
    path_step = "/"
DEBUG_ = True
CL_VERSION_REGEX = r"\d+\.\d+\.\d+"
GIT_VERSION_REGEX = r"\d+\.\d+\.\d+.{0,10}"
# Pretty much the same thing, so ... why not
CMAKE_VERSION_REGEX = CL_VERSION_REGEX

startup_message = (
    "[bold green]Welcome[/] to [bold purple][link=https://github.com/Advik-B/Aseprite-Compiler]Aseprite-Compiler[/][/].\n"
    "[bold purple]Aseprite-Compiler[/] is a CLI tool for compiling [bold blue link=https://www.aseprite.org]Aseprite[/] from its [italic cyan link=https://github.com/Aseprite/Aseprite]source code.[/]\n"
    "Here is come information cause I dont know what-else to put here :grinning_face_with_sweat:\n"
)
deps = Panel(
    "1. [italic bold red link=https://git-scm.com]Git[/] [bold white](Version Control System)[/]\n"
    "2. [italic bold blue link=https://github.com/Aseprite/Aseprite]Aseprite[/] [bold white](Source-Code)[/]\n"
    "3. [italic bold green link=https://github.com/aseprite/skia]Skia[/] [bold white](Library)[/]\n"
    "4. [italic bold cyan link=https://cmake.org]CMake[/] [bold white](Build-System)[/]\n"
    "5. [italic bold purple link=https://ninja-build.org/]Ninja[/] [bold white](Build-System/Assembler)[/]\n"
    "6. [italic bold magenta link=https://visualstudio.microsoft.com/downloads/]Visual Studio Build Tools[/] [bold white](Compiler)[/]\n"
    "7. [italic bold Yellow link=https://developer.microsoft.com/en-us/windows/downloads/windows-sdk/]Windows SDK[/] [bold white](Software Development Kit)[/]\n",
    title="There are the dependencies that Aseprite-Compiler needs. (No need to install them :winking_face:)",
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

console.print("[italic]Anyways[/], let's start with some basic questions.")
console.print(
    "[italic]Where[/] do you want me to do [italic green]my work[/]? (Choose a folder)"
)
# console.input(
#     "[bold yellow]>> PRESS ENTER TO OPEN FOLDER DIALOG <<[/]",
#     password=True
# )
# folder = None


# while True:
#     if folder is None or folder == "":
#         folder = filedialog.askdirectory()
#         # Check if the folder is not an empty folder
#         # If it is, ask the user to choose an empty folder
#         if len(os.listdir(folder)) != 0:
#             console.print(
#                 "[bold italic red]The folder you chose is not empty. Please choose an empty folder.[/]",
#                 highlight=True,
#             )
#             folder = None
#             continue
#     else:
#         break

# console.print("Ok, I will work in [italic meganta]%s[/]" % folder)

# # Do basic setup
# SRC_FOLDER = pjoin(folder, "src")
# DOWNLOADS_FOLDER = pjoin(folder, "downloads")
# BUILD_FOLDER = pjoin(folder, "build")
# ASEPRITE_FOLDER = pjoin(folder, "Aseprite")

# # Iterate over the locales, if they end with FOLDER then ensure it exists
# locs = [*locals()]
# locs = tuple(locs)
# for locale in locs:
#     if locale.endswith("_FOLDER"):
#         if not os.path.exists(locals()[locale]):
#             os.makedirs(locals()[locale])


def find_cl_version():
    cl_version = subprocess.run(
        cl[0], universal_newlines=True, capture_output=True, shell=True
    )
    cl_version = cl_version.stderr
    cl_version = cl_version.split("\n")[0]
    cl_version = re.findall(CL_VERSION_REGEX, cl_version)
    if len(cl_version) <= 0:
        return None
    return cl_version[0]


def find_git_version():
    git_version = subprocess.run(
        git[0] + " --version", universal_newlines=True, capture_output=True, shell=True
    )
    git_version = git_version.stdout
    # git version 2.37.0.windows.1
    git_version = git_version.split("\n")[0]
    git_version = re.findall(GIT_VERSION_REGEX, git_version)
    if len(git_version) <= 0:
        return None
    return git_version[0]


def find_cmake_version():
    cmake_version = subprocess.run(
        cmake[0] + " --version",
        universal_newlines=True,
        capture_output=True,
        shell=True,
    )
    cmake_version = cmake_version.stdout
    # cmake version 3.12.0.win32-x86_64
    cmake_version = cmake_version.split("\n")[0]
    cmake_version = re.findall(CMAKE_VERSION_REGEX, cmake_version)
    if len(cmake_version) <= 0:
        return None
    return cmake_version[0]


def find_ninja_version():
    ninja_version = subprocess.run(
        ninja[0] + " --version",
        universal_newlines=True,
        capture_output=True,
        shell=True,
    )
    ninja_version = ninja_version.stdout
    # 1.10.0
    ninja_version = ninja_version.split("\n")[0]
    # No need to check for the regex, because it's a simple string
    return ninja_version[0]


version_dict = {
    "git": find_git_version,
    "cl": find_cl_version,
    "cmake": find_cmake_version,
    "ninja": find_ninja_version,
}

deps = {}
console.print("Ok, I'm [green]ready[/] to go.")
with console.status("Checking for dependencies...") as status:
    git = find_executable_in_path("git"), "Git", "git"
    cmake = find_executable_in_path("cmake"), "CMake", "cmake"
    ninja = find_executable_in_path("ninja"), "Ninja", "ninja"
    cl = find_executable_in_path("cl"), "Microsoft C++ Compiler", "cl"
    deps_ = (git, cmake, ninja, cl)
    for dep in deps_:
        if dep[0] is None:
            if DEBUG_:
                console.log(DEBUG, f"[bold red]{dep[1]} is missing.[/]")
            binary = dep[2]
            deps[binary] = {
                "path": None,
                "name": dep[1],
                "status": "[bold red]Missing[/]",
                "version": r"¯\_(ツ)_/¯",
            }
        else:
            if DEBUG_:
                console.log(
                    DEBUG,
                    f"[bold green]Found[/] {dep[1]} at [italic yellow]{dep[0]}[/]",
                )
            binary = dep[0].split(path_step)
            binary = binary[-1]
            binary = binary.removesuffix(".exe")
            deps[binary] = {
                "path": dep[0],
                "name": dep[1],
                "status": "[bold green]Found[/]",
                "version": version_dict[binary](),
            }

dependancy_table = Table("Dependancies")
dependancy_table.add_column("Version")
dependancy_table.add_column("Status")
dependancy_table.add_column("Path")

for binary in deps:
    dependancy_table.add_row(
        deps[binary]["name"],
        deps[binary]["version"],
        deps[binary]["status"],
        deps[binary]["path"],
    )

console.print(dependancy_table)
