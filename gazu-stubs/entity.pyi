from typing import Any, Literal, TypeAlias, TypedDict

from .client import KitsuClient, default_client

class EntityDict(TypedDict):
    canceled: bool
    data: dict[str, Any]
    description: str | None
    entity_type_id: str
    id: str
    name: str
    parent_id: str
    preview_file_id: str | None
    project_id: str
    source_id: str | None
    nb_entities_out: int
    is_casting_standby: bool
    code: str | None
    shotgun_id: str | None
    status: (
        Literal["standby"]
        | Literal["running"]
        | Literal["complete"]
        | Literal["canceled"]
    )
    ready_for: str | None
    created_by: str
    entities_out: list[str]
    entity_concept_links: list[str]
    instance_casting: list[str]
    created_at: str
    updated_at: str
    entities_in: list[str]

class EntityTypeDict(TypedDict):
    id: str
    name: str
    short_name: str
    description: str | None
    task_types: list[str]
    created_at: str
    updated_at: str
    type: Literal["EntityType"]

EntityTypeLiteral: TypeAlias = Literal["Asset", "Shot", "Sequence", "Edit"]

def get_entity(entity_id: str, client: KitsuClient = default_client) -> EntityDict: ...
def get_entity_by_name(
    entity_name: str, project: str | None = None, client: KitsuClient = default_client
) -> EntityDict: ...
def get_entity_type(
    entity_type_id: str, client: KitsuClient = default_client
) -> EntityTypeDict: ...
def get_entity_type_by_name(
    entity_type_name: str, client: KitsuClient = default_client
) -> EntityTypeDict: ...
