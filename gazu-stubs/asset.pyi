from typing import Any, Literal, TypedDict

from gazu.project import ProjectDict
from gazu.shot import EpisodeDict

from .client import KitsuClient, default_client
from .entity import EntityDict

class AssetDict(EntityDict):
    asset_type_id: str
    asset_type_name: str
    casting_episode_ids: list[str]
    type: Literal["Asset"]

class AssetTypeDict(TypedDict):
    name: str
    short_name: str | None
    description: str | None
    archived: bool
    id: str
    created_at: str
    updated_at: str
    type: Literal["AssetType"]

def all_asset_types_for_project(
    project: ProjectDict | str, client: KitsuClient = default_client
) -> AssetTypeDict: ...
def get_asset_type_by_name(
    name: str, client: KitsuClient = default_client
) -> AssetTypeDict | None: ...
def get_asset_by_name(
    project: ProjectDict | str,
    name: str,
    asset_type: str | AssetTypeDict,
    client: KitsuClient = default_client,
) -> AssetDict: ...
def get_asset(asset_id: str, client: KitsuClient = default_client) -> AssetDict: ...
def new_asset(
    project: ProjectDict | str,
    asset_type: str | AssetTypeDict,
    name: str,
    description: str | None = None,
    extra_data: dict[str, Any] = {},
    episode: str | EpisodeDict | None = None,
    is_shared: bool = False,
    client: KitsuClient = default_client,
) -> AssetDict: ...
def update_asset(
    asset: AssetDict, client: KitsuClient = default_client
) -> AssetDict: ...
def update_asset_data(
    asset: AssetDict, data: dict[str, Any] = {}, client: KitsuClient = default_client
) -> AssetDict: ...
def remove_asset(
    asset: str | AssetDict, client: KitsuClient = default_client
) -> None: ...
