from typing import TypedDict
from gazu.asset import AssetDict
from gazu.project import ProjectDict

from gazu.shot import EpisodeDict, SequenceDict, ShotDict
from .client import KitsuClient, default_client
from .entity import EntityDict

class PartialEntityCasting(TypedDict):
    asset_id: str
    nb_occurences: int

class EntityCasting(PartialEntityCasting):
    asset_name: str
    asset_type_name: str
    ready_for: str | None
    episode_id: str
    label: str
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
def update_shot_casting(
    project: str | ProjectDict,
    shot: str | ShotDict,
    casting: list[PartialEntityCasting],
    client: KitsuClient = default_client,
) -> list[EntityCasting]: ...
def update_asset_casting(
    project: str | ProjectDict,
    asset: str | AssetDict,
    casting: list[PartialEntityCasting],
    client: KitsuClient = default_client,
) -> list[EntityCasting]: ...
def update_sequence_casting(
    project: str | ProjectDict,
    asset: str | SequenceDict,
    casting: list[PartialEntityCasting],
    client: KitsuClient = default_client,
) -> list[EntityCasting]: ...
def update_episode_casting(
    project: str | ProjectDict,
    asset: str | EpisodeDict,
    casting: list[PartialEntityCasting],
    client: KitsuClient = default_client,
) -> list[EntityCasting]: ...
