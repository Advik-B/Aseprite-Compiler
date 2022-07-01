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


def download_git(path):
    """
    Downloads the latest version of the git repository.
    """
    if find_executable_in_path("git") is None:
        print("Git is not installed. Temporarily installing git...")
