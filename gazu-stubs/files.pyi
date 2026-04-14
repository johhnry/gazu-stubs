from typing import Callable, TypedDict

from .client import KitsuClient, default_client

class PreviewFileDict(TypedDict):
    id: str

def download_preview_file_cover(
    preview_file: PreviewFileDict | str,
    file_path: str,
    progress_callback: Callable[[int, int], object] | None = None,
    client: KitsuClient = default_client,
) -> None: ...
