from typing import TypedDict
from .client import KitsuClient, default_client
from .entity import EntityDict

class EntityCasting(TypedDict):
    asset_id: str
    asset_name: str
    asset__type_name: str
    ready_for: str | None
    episode_id: str
    label: str
    nb_occurences: int
    is_shared: bool
    project_id: str

def get_shot_casting(
    shot: EntityDict, client: KitsuClient = default_client
) -> list[EntityCasting]: ...
def get_asset_casting(
    asset: EntityDict, client: KitsuClient = default_client
) -> list[EntityCasting]: ...
def get_sequence_casting(
    sequence: EntityDict, client: KitsuClient = default_client
) -> list[EntityCasting]: ...
def get_episode_casting(
    episode: EntityDict, client: KitsuClient = default_client
) -> list[EntityCasting]: ...
