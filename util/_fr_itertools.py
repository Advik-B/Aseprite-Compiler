from alive_progress import alive_bar
from io import BytesIO
from requests import Response

def iter_content(file: BytesIO, conten_length:int,r: Response, chunk_size=1024):
    """Iterates over the response data in chunks of bytes."""
    # check if the file-size not divisible by chunk-size.
    if conten_length % chunk_size != 0:
        chunk_size = conten_length % chunk_size
    with alive_bar(conten_length // chunk_size) as bar:
        for data in r.iter_content(chunk_size=chunk_size):
            file.write(data)
            bar()