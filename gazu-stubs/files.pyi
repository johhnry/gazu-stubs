from collections.abc import Callable
from typing import TypedDict

from gazu.task import TaskDict

from .client import KitsuClient, default_client

class PreviewFileDict(TypedDict):
    id: str

def download_preview_file_cover(
    preview_file: PreviewFileDict | str,
    file_path: str,
    progress_callback: Callable[[int, int], object] | None = None,
    client: KitsuClient = default_client,
) -> None: ...
def get_all_preview_files_for_task(
    task: TaskDict | str, client: KitsuClient = default_client
) -> list[TaskDict]: ...
