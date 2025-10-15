from typing import TypedDict
from gazu.asset import AssetDict
from gazu.project import ProjectDict

from gazu.shot import EpisodeDict, SequenceDict, ShotDict
from .client import KitsuClient, default_client

class CastingDictPartial(TypedDict):
    asset_id: str
    nb_occurences: int

class CastingDict(CastingDictPartial):
    asset_name: str
    asset_type_name: str
    ready_for: str | None
    episode_id: str
    label: str
    is_shared: bool
    project_id: str

def get_shot_casting(
    shot: ShotDict, client: KitsuClient = default_client
) -> list[CastingDict]: ...
def get_asset_casting(
    asset: AssetDict, client: KitsuClient = default_client
) -> list[CastingDict]: ...
def get_sequence_casting(
    sequence: SequenceDict, client: KitsuClient = default_client
) -> dict[str, list[CastingDict]]: ...
def get_episode_casting(
    episode: EpisodeDict, client: KitsuClient = default_client
) -> list[CastingDict]: ...
def update_shot_casting(
    project: str | ProjectDict,
    shot: str | ShotDict,
    casting: list[CastingDictPartial],
    client: KitsuClient = default_client,
) -> list[CastingDict]: ...
def update_asset_casting(
    project: str | ProjectDict,
    asset: str | AssetDict,
    casting: list[CastingDictPartial],
    client: KitsuClient = default_client,
) -> list[CastingDict]: ...
def update_sequence_casting(
    project: str | ProjectDict,
    asset: str | SequenceDict,
    casting: list[CastingDictPartial],
    client: KitsuClient = default_client,
) -> list[CastingDict]: ...
def update_episode_casting(
    project: str | ProjectDict,
    asset: str | EpisodeDict,
    casting: list[CastingDictPartial],
    client: KitsuClient = default_client,
) -> list[CastingDict]: ...
