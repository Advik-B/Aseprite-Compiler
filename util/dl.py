import json

from requests import get
from rich.console import Console

from ..errors import NoInternetConnection
from .constants import ERROR, INFO, WARNING
from .o import console
from .prime_numbers import is_prime


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
    allow_redirects: bool = True,
    show_locals: bool = False,
):
    if check_internet_connection:
        if not check_internet_connection_():
            console.log(f"{ERROR} No internet connection.")
            return NoInternetConnection("Module: %s" % __name__)

    headers = {}
    validate_ssl = False
    if blend_in:
        headers = generate_fake_headers()
    if be_careful:
        validate_ssl = True

    response = get(url, headers=headers, verify=validate_ssl,
                   allow_redirects=allow_redirects)

    if show_headers:
        console.log(INFO, " Headers: ")
        console.print_json(json.dumps(response.headers), indent=4)

    if show_extra_info:
        console.log(INFO, " Extra info: ")
        console.print_json(
            json.dumps(
                {
                    "url": response.url,
                    "reason": response.reason,
                    "status_code": response.status_code,
                    "encoding": response.encoding,
                    "content_type": response.headers.get("content-type"),
                    "history": response.history,

                },
                indent=4,
                ensure_ascii=False)
        )

    # Get the filename from the response headers if possible.
    filename = fallback_filename
    if fallback_filename is None:
        try:
            filename = response.headers.get(
                "content-disposition").split("filename=")[1]
        except IndexError:
            pass

    if filename is None:
        filename = url.split("/")[-1]

    if show_locals:
        console.log(log_locals=True)

    file_size = int(response.headers.get("content-length", 0))
    if file_size < 1024:
        console.log(WARNING, f"File size: {file_size} bytes (less than 1MB)")

    chunk_dl = True
    if file_size >= 0:
        console.log(
            WARNING, f"File size is not known. Chunk downloading is not possible.")
        chunk_dl = False
