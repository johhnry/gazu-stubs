from typing import Literal, TypeAlias, TypedDict

from gazu.project import ProjectDict

from .client import KitsuClient, default_client

class EntityDictBase(TypedDict):
    id: str
    name: str
    code: str | None
    description: str | None
    shotgun_id: str | None
    canceled: bool
    nb_frames: int | None
    nb_entities_out: int
    is_casting_standby: bool
    status: Literal["standby", "running", "complete", "canceled"]
    project_id: str
    entity_type_id: str
    parent_id: str | None
    source_id: str | None
    preview_file_id: str | None
    data: dict[str, str]
    ready_for: str | None
    created_by: str
    created_at: str
    updated_at: str

class EntityDict(EntityDictBase):
    entities_out: list[str]
    entity_concept_links: list[str]
    instance_casting: list[str]
    entities_in: list[str]

class EntityTypeDictBase(TypedDict):
    name: str
    archived: bool | None
    id: str
    created_at: str
    updated_at: str
    type: Literal["EntityType"]

class EntityTypeDict(EntityTypeDictBase):
    task_types: list[str]

EntityTypeLiteral: TypeAlias = Literal["Asset", "Shot", "Sequence", "Edit", "Episode"]

def all_entities(client: KitsuClient = default_client) -> list[EntityDictBase]: ...
def all_entity_types(
    client: KitsuClient = default_client,
) -> list[EntityTypeDictBase]: ...
def get_entity(entity_id: str, client: KitsuClient = default_client) -> EntityDict: ...
def get_entity_by_name(
    entity_name: str,
    project: ProjectDict | str | None = None,
    client: KitsuClient = default_client,
) -> EntityDictBase: ...
def get_entity_type(
    entity_type_id: str, client: KitsuClient = default_client
) -> EntityTypeDict: ...
def get_entity_type_by_name(
    entity_type_name: str, client: KitsuClient = default_client
) -> EntityTypeDictBase: ...
def new_entity_type(
    name: str, client: KitsuClient = default_client
) -> EntityTypeDict: ...
def all_entities_with_tasks_linked_to_entity(
    entity: EntityTypeDictBase | str, client: KitsuClient = default_client
) -> list[EntityTypeDictBase]: ...
