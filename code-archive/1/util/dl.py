import json
import warnings
from typing import Union

from alive_progress import alive_bar
from requests import get
from urllib3.exceptions import InsecureRequestWarning

from ._fr_itertools import iter_content
from .constants import DEBUG, ERROR, INFO, WARNING
from .errors import NoInternetConnection
from .o import console
from .prime_numbers import is_prime

warnings.filterwarnings("ignore", category=InsecureRequestWarning)


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
    except BaseException:
        return False


def download(
    url: str,
    show_progress: bool = True,
    show_headers: bool = False,
    show_extra_info: bool = False,
    fallback_filename: Union[str, None] = None,
    be_careful: bool = False,
    blend_in: bool = False,
    check_internet_connection: bool = False,
    allow_redirects: bool = True,
    show_locals: bool = False,
    progressbar: str = "alive",
):
    # Clear the trailing slash if it exists
    if url[-1] == "/":
        url = url[:-1]

    if check_internet_connection and not check_internet_connection_():
        console.log(f"{ERROR} No internet connection.")
        raise NoInternetConnection(f"Module: {__name__}")

    headers = generate_fake_headers() if blend_in else {}
    validate_ssl = be_careful
    response = get(
        url,
        headers=headers,
        verify=validate_ssl,
        allow_redirects=allow_redirects,
        stream=True,
    )

    if show_headers:
        console.log(INFO, " Headers: ")
        console.print_json(json.dumps(dict(response.headers)), indent=4)

    if show_extra_info:
        console.log(INFO, " Extra info: ")
        console.print_json(
            data={
                "url": response.url,
                "reason": response.reason,
                "status_code": response.status_code,
                "encoding": response.encoding,
                "content_type": response.headers.get("content-type"),
                # "history": response.history,
            },
        )

    # Get the filename from the response headers if possible.
    filename = fallback_filename
    if filename is None:
        try:
            filename = response.headers.get(
                "content-disposition").split("filename=")[1]
        except (IndexError, AttributeError):
            pass
    if filename is None:
        filename = url.split("/")[-1]
        console.log(WARNING, f"No filename found. Using {filename}.")

    if show_locals:
        console.log(log_locals=True)

    file_size = response.headers.get("content-length")
    # console.log(DEBUG, 'Starting file-size: %s' % file_size)
    file_size = int(file_size)
    if file_size < 1024 and file_size > 0:
        console.log(WARNING, f"File size: {file_size} bytes (less than 1MB)")

    chunk_dl = True
    if file_size <= 0:
        console.log(
            WARNING,
            "File size is not known. Chunk downloading is not possible.",
        )

        chunk_dl = False

    chunk_size = 1024
    # Check if the file-size not divisible by chunk-size.
    if file_size % chunk_size != 0:
        chunk_size = file_size % chunk_size

    with open(filename, "wb") as f:
        if chunk_dl and show_progress:
            iter_content(f, file_size, response, progressbar=progressbar)
        else:
            for data in response.iter_content(chunk_size=chunk_size):
                f.write(data)
    if show_locals:
        console.log(log_locals=True)
