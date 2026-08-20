from collections.abc import Callable
from typing import Any, Literal, NotRequired, TypedDict

from gazu.task import TaskDict

from .client import KitsuClient, default_client

class PreviewFileDataDict(TypedDict):
    original_duration: float
    original_file_size: int
    original_height: int
    original_width: int

class PreviewFileDict(TypedDict):
    annotations: list[dict[str, Any]] | None
    comments: NotRequired[list[str]]
    created_at: str
    data: PreviewFileDataDict | None
    description: str | None
    duration: float
    extension: str
    file_size: int
    height: int
    id: str
    is_movie: bool
    name: str
    original_name: str | None
    path: str | None
    person_id: str
    position: int
    revision: int
    shotgun_id: str | None
    source: str
    source_file_id: str | None
    status: str
    task_id: str
    token_in: str | None
    token_out: str | None
    type: Literal["PreviewFile"]
    updated_at: str
    uploaded_movie_name: str | None
    uploaded_movie_url: str | None
    url: str | None
    validation_status: str
    width: int

def download_preview_file_cover(
    preview_file: PreviewFileDict | str,
    file_path: str,
    progress_callback: Callable[[int, int], object] | None = None,
    client: KitsuClient = default_client,
) -> None: ...
def get_all_preview_files_for_task(
    task: TaskDict | str, client: KitsuClient = default_client
) -> list[PreviewFileDict]: ...
