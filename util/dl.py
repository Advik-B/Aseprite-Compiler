from requests import get
from alive_progress import alive_bar
from urllib.parse import quote
from . import is_prime
from . import cout
import random
import json

# Ignore insecure request warnings
import warnings

warnings.filterwarnings("ignore")



def download_file(url, show_headers=False, show_status=False, show_warnings=False):
    request = get(url, headers=generate_fake_headers(), stream=True)
    if show_headers:
        cout("Headers:", color="yellow")
        cout(json.dumps(request.headers, indent=4), color="white", styles=("italic",))

    file_size = request.headers.get("Content-Length")
    file_name = request.headers.get("Content-Disposition")
    if not file_name:
        file_name = url.split("/")[-1]
    
    use_chunked_transfer = file_size is not None
    if file_size is None:
        if show_warnings:
            cout(
                "Warning: The file size is not known. So chunk-downloading is not possible",
                color="yellow",
            )

    if show_status:
        cout("[+] Downloading file: ", color="green", styles=("bold",), end="")
        cout(file_name, color="white", styles=("underline",))
        cout("[+] File size: ", color="green", styles=("bold",), end="")
        cout(file_size, color="white", styles=("underline",))
