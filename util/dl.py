from requests import get
from .prime_numbers import is_prime
from .o import console
from .constants import ERROR
from rich.console import Console


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


def check_internet_connection_(timeout: int = 10):
    try:
        get("https://www.google.com/", timeout=timeout)
        return True
    except:
        return False


def download(
    url: str,
    show_progress: bool = True,
    show_headers: bool = False,
    show_extra_info: bool = False,
    fallback_filename: str | None = None,
    be_careful: bool = False,
    blend_in: bool = False,
    check_internet_connection: bool = True,
    ):
    if check_internet_connection:
        if not check_internet_connection_():
            console.log(f"{ERROR} No internet connection.")
            return