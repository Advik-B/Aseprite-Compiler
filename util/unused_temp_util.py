import sys
import termcolor


def buildblock(size):
    block = str()
    for _ in range(size):
        block += chr(random.randint(41, 91))
    return quote(block)


def generate_fake_url():
    BASE_URL = "https://www.google.com/search?q="
    return (
        BASE_URL
        + buildblock(random.randint(5, 10))
        + "+"
        + buildblock(random.randint(5, 10))
    )


def generate_fake_headers():
    return {
        "Referer": generate_fake_url(),
        "Keep-Alive": str(random.randint(110, 160)),
        "Connection": "keep-alive",
        "User-Agent": get("https://randua.deta.dev").json()["ua"],
    }


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
