from typing import Any

class KitsuClient:
    pass

default_client: KitsuClient

def build_path_with_params(path: str, params: dict[Any, Any]) -> str: ...
def fetch_all(
    path: str,
    params: dict[Any, Any] | None = None,
    client: KitsuClient = default_client,
    paginated: bool = False,
    limit: int | None = None,
) -> list[dict[Any, Any]]: ...
def fetch_first(
    path: str,
    params: dict[Any, Any] | None = None,
    client: KitsuClient = default_client,
) -> dict[Any, Any] | None: ...
def fetch_one(
    model_name: str, id: str, client: KitsuClient = default_client
) -> dict[Any, Any] | None: ...
def create(
    model_name: str, data: dict[str, Any], client: KitsuClient = default_client
) -> dict[Any, Any] | None: ...
def update(
    model_name: str, id: str, data: dict[str, Any], client: KitsuClient = default_client
) -> dict[Any, Any] | None: ...
def delete(
    path: str,
    params: dict[str, Any] | None = None,
    client: KitsuClient = default_client,
) -> dict[Any, Any] | None: ...
