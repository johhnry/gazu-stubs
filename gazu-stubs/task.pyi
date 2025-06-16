from typing import Any, Literal, NotRequired, TypedDict

from gazu.project import ProjectDict

from .client import KitsuClient, default_client
from .entity import EntityDict, EntityTypeLiteral
from .person import PersonDict

class TaskDict(TypedDict):
    name: str
    description: str | None
    priority: int
    duration: float
    estimation: float
    completion_rate: int
    retake_count: int
    sort_order: int
    start_date: None
    due_date: None
    real_start_date: None
    end_date: None
    done_date: None
    last_comment_date: None
    nb_assets_ready: int
    data: None
    shotgun_id: None
    last_preview_file_id: str | None
    project_id: str
    task_type_id: str
    task_status_id: str
    entity_id: str
    assigner_id: str
    assignees: list[str]
    id: str
    created_at: str
    updated_at: str
    type: Literal["Task"]
    # entity:
    # entity_type: EntityType
    is_subscribed: bool
    # persons: list[PersonDict]
    # project: Project
    task_status: TaskStatusDict
    # assigner: PersonDict
    # sequence: Sequence

class TaskStatusDict(TypedDict):
    name: str
    archived: bool
    short_name: str
    description: str | None
    color: str
    priority: int
    is_done: bool
    is_artist_allowed: bool
    is_client_allowed: bool
    is_retake: bool
    is_feedback_request: bool
    is_default: bool
    shotgun_id: str | None
    for_concept: bool
    id: str
    created_at: str
    updated_at: str
    type: Literal["TaskStatus"]

class TaskTypeDict(TypedDict):
    name: str
    short_name: str
    description: str | None
    color: str
    priority: int
    for_entity: EntityTypeLiteral
    allow_timelog: bool
    archived: bool
    shotgun_id: str | None
    department_id: str
    id: str
    created_at: str
    updated_at: str
    type: Literal["TaskType"]

class CommentAttachmentDict(TypedDict):
    id: str
    name: str
    size: int
    extension: str

class CommentChecklistDict(TypedDict):
    text: str
    checked: bool
    frame: NotRequired[int]
    revision: NotRequired[int]

class CommentReplyDict(TypedDict):
    created_at: str
    date: str
    department_mentions: list[str]
    id: str
    mentions: list[str]
    person_id: str
    text: str

class CommentDict(TypedDict):
    acknowledgements: list[str]
    attachment_files: list[str]
    checklist: list[CommentChecklistDict]
    created_at: str
    data: dict[str, Any] | None
    department_mentions: list[str]
    id: str
    links: list[str]
    mentions: list[str]
    object_id: str
    object_type: Literal["Task"]
    person_id: str
    pinned: bool | None
    preview_file_id: str | None
    previews: list[str]
    replies: list[CommentReplyDict]
    shotgun_id: str | None
    task_status_id: str
    text: str
    type: Literal["Comment"]
    updated_at: str

class PreviewDict(TypedDict):
    created_at: str
    duration: float
    extension: str
    height: int
    id: str
    original_name: str
    revision: int
    status: str
    task_id: str
    width: int

class FullTaskDict(TaskDict):
    task_type: TaskTypeDict

def get_task(task_id: str, client: KitsuClient = default_client) -> FullTaskDict: ...
def get_task_by_name(
    entity: EntityDict | str,
    task_type: TaskTypeDict | str,
    client: KitsuClient = default_client,
) -> TaskDict | None: ...
def new_task(
    entity: str | EntityDict,
    task_type: str | TaskTypeDict,
    name: str = "main",
    task_status: TaskStatusDict | None = None,
    assigner: str | PersonDict | None = None,
    client: KitsuClient = default_client,
) -> TaskDict: ...
def update_task(task: TaskDict, client: KitsuClient = default_client) -> TaskDict: ...
def update_task_data(
    task: TaskDict, data: dict[str, Any] = {}, client: KitsuClient = default_client
) -> TaskDict: ...
def get_task_by_entity(
    entity: EntityDict | str,
    task_type: TaskTypeDict | str,
    name: str = "main",
    client: KitsuClient = default_client,
) -> TaskDict | None: ...
def all_task_statuses(client: KitsuClient = default_client) -> list[TaskStatusDict]: ...
def get_task_status(
    task_status_id: str, client: KitsuClient = default_client
) -> TaskStatusDict | None: ...
def get_task_type(
    task_type_id: str, client: KitsuClient = default_client
) -> TaskTypeDict | None: ...
def all_task_statuses_for_project(
    project: str | ProjectDict, client: KitsuClient = default_client
) -> list[TaskStatusDict]: ...
def get_task_status_by_name(
    name: str, client: KitsuClient = default_client
) -> TaskStatusDict | None: ...
def get_task_status_by_short_name(
    task_status_short_name: str, client: KitsuClient = default_client
) -> TaskStatusDict | None: ...
def get_task_type_by_name(
    task_type_name: str,
    for_entity: str | None = None,
    department: str | None = None,
    client: KitsuClient = default_client,
) -> TaskTypeDict | None: ...
def all_task_types_for_project(
    project: ProjectDict | str, client: KitsuClient = default_client
) -> list[TaskTypeDict]: ...
def add_comment(
    task: TaskDict | str,
    task_status: TaskStatusDict | str,
    comment: str = "",
    person: PersonDict | str | None = None,
    checklist: list[CommentChecklistDict] = [],
    attachments: list[CommentAttachmentDict] = [],
    created_at: str | None = None,
    links: list[str] = [],
    client: KitsuClient = default_client,
) -> CommentDict | None: ...
def add_preview(
    task: TaskDict | str,
    comment: CommentDict | str,
    preview_file_path: str | None = None,
    preview_file_url: str | None = None,
    normalize_movie: bool = True,
    revision: int | None = None,
    client: KitsuClient = default_client,
) -> PreviewDict | None: ...
def get_comment(
    comment_id: str, client: KitsuClient = default_client
) -> CommentDict: ...
def assign_task(
    task: TaskDict | str, person: PersonDict | str, client: KitsuClient = default_client
) -> TaskDict: ...
def start_task(
    task: TaskDict | str,
    started_task_status: TaskStatusDict | str | None = None,
    client: KitsuClient = default_client,
) -> CommentDict: ...
