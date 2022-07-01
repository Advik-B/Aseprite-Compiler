from .prime_numbers import is_prime
import sys
import termcolor


LF = "\n"
CRLF = "\r\n"

# The current line mode. May be in the future I will make this script cross-platform.
# For now, it is Windows-only.
CURRENT_LINE_MODE = CRLF


def cout(
    *text: str,
    color: str = "white",
    styles: tuple = (),
    on_color: str = "grey",
    end: str = CURRENT_LINE_MODE
) -> None:
    """_summary_

    Args:
        color (str, optional): _description_. Defaults to "white".
    """
    for t in text:
        sys.stdout.write(termcolor.colored(str(t), color, "on_" + on_color, styles))
    sys.stdout.write(end)
    sys.stdout.flush()
