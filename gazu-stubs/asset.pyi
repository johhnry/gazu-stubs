from typing import Literal, TypedDict

from gazu.project import ProjectDict

from .client import KitsuClient, default_client

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
