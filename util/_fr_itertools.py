from alive_progress import alive_bar
from io import BytesIO
from requests import Response
from rich.progress import Progress
from .errors import InvalidProgressBar


def iter_content(
    file: BytesIO,
    conten_length: int,
    r: Response,
    chunk_size=1024,
    progressbar: str = "alive",
):
    """Iterates over the response data in chunks of bytes."""
    # check if the file-size not divisible by chunk-size.
    if conten_length % chunk_size != 0:
        chunk_size = conten_length % chunk_size
    if progressbar.casefold() == "alive":
        with alive_bar(conten_length // chunk_size) as bar:
            for data in r.iter_content(chunk_size=chunk_size):
                file.write(data)
                bar()
    elif progressbar.casefold() == "rich":
        with Progress() as progress:
            download_task = progress.add_task(
                description="",
                total=conten_length // chunk_size,
            )
            for data in r.iter_content(chunk_size=chunk_size):
                file.write(data)
                progress.update(download_task, advance=1)

    else:
        raise InvalidProgressBar(f"Invalid progressbar: {progressbar}")
