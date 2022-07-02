from .constants import ERROR, INFO, WARNING, DEBUG
from .prime_numbers import is_prime
from .o import console
import json
import warnings
from requests import get
from urllib3.exceptions import InsecureRequestWarning
from rich.progress import (
    BarColumn,
    DownloadColumn,
    Progress,
    TaskID,
    TextColumn,
    TimeRemainingColumn,
    TransferSpeedColumn,
)

# from ..errors import NoInternetConnection


class NoInternetConnection(Exception):
    pass


warnings.filterwarnings("ignore", category=InsecureRequestWarning)

progress = Progress(
    TextColumn("[bold blue]{task.fields[filename]}", justify="right"),
    BarColumn(bar_width=None),
    "[progress.percentage]{task.percentage:>3.1f}%",
    "•",
    DownloadColumn(),
    "•",
    TransferSpeedColumn(),
    "•",
    TimeRemainingColumn(),
    console=console,
    transient=True,
)


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
    # Clear the trailing slash if it exists
    if url[-1] == "/":
        url = url[:-1]

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

    response = get(
        url, headers=headers, verify=validate_ssl, allow_redirects=allow_redirects, stream=True
    )

    if show_headers:
        console.log(INFO, " Headers: ")
        console.print_json(json.dumps(response.headers), indent=4)

    if show_extra_info:
        console.log(INFO, " Extra info: ")
        console.print_json(
            data={
                "url": response.url,
                "reason": response.reason,
                "status_code": response.status_code,
                "encoding": response.encoding,
                "content_type": response.headers.get("content-type"),
                "history": response.history,
            },
        )

    # Get the filename from the response headers if possible.
    filename = fallback_filename
    if fallback_filename is None:
        try:
            filename = response.headers.get(
                "content-disposition").split("filename=")[1]
        except IndexError:
            pass
        except AttributeError:
            pass

    if filename is None:
        filename = url.split("/")[-1]
        console.log(WARNING, f"No filename found. Using {filename}.")

    if show_locals:
        console.log(log_locals=True)

    file_size = response.headers.get("content-length")
    console.log(DEBUG, 'Starting file-size: %s' % file_size)
    file_size = int(file_size)
    if file_size < 1024 and file_size > 0:
        console.log(WARNING, f"File size: {file_size} bytes (less than 1MB)")

    chunk_dl = True
    if file_size <= 0:
        console.log(
            WARNING, f"File size is not known. Chunk downloading is not possible."
        )
        chunk_dl = False

    chunk_size = 1024
    # Check if the file-size not divisible by chunk-size.
    if file_size % chunk_size != 0:
        chunk_size = file_size % chunk_size

    if chunk_dl:
        if show_progress:
            task_id = progress.add_task(
                filename,
                total=file_size,
                visible=True,
            )
            with open(filename, "wb") as f:
                for data in response.iter_content(chunk_size=chunk_size):
                    f.write(data)
                    progress.update(task_id=task_id, increment=len(data),
                                    data=data, total=file_size)
        else:
            with open(filename, "wb") as f:
                for data in response.iter_content(chunk_size=chunk_size):
                    f.write(data)
    else:
        with open(filename, "wb") as f:
            f.write(response.content)

    console.log(INFO, f"Downloaded {filename}")
