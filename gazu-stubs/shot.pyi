from typing import Any, Literal, TypedDict

from .client import KitsuClient, default_client

class ShotDict(TypedDict):
    canceled: bool
    data: dict[str, Any]
    description: str | None
    entity_type_id: str
    episode_id: str | None
    episode_name: str
    fps: float | None
    frame_in: int | None
    frame_out: int | None
    id: str
    name: str
    nb_frames: int
    parent_id: str
    preview_file_id: str
    project_id: str
    project_name: str
    sequence_id: str
    sequence_name: str
    source_id: str | None
    nb_entities_out: int
    is_casting_standby: bool
    # tasks: ?
    type: Literal["Shot"]
    code: str | None
    shotgun_id: str | None
    status: Literal["running"]
    ready_for: str | None
    created_by: str
    entities_out: list[str]
    entity_concept_links: list[str]
    instance_casting: list[str]
    created_at: str
    updated_at: str
    entities_in: list[str]

class SequenceDict(TypedDict):
    id: str
    name: str
    code: str | None
    description: str
    shotgun_id: str | None
    canceled: bool
    nb_frames: int | None
    nb_entities_out: int
    is_casting_standby: bool
    status: Literal["running"]
    project_id: str
    entity_type_id: str
    parent_id: str | None
    source_id: str | None
    preview_file_id: str | None
    data: dict[str, Any]
    ready_for: str | None
    created_by: str
    created_at: str
    updated_at: str
    type: Literal["Sequence"]
    project_name: str

def get_shot(shot_id: str, client: KitsuClient = default_client) -> ShotDict: ...
def get_sequence(
    sequence_id: str, client: KitsuClient = default_client
) -> SequenceDict: ...
