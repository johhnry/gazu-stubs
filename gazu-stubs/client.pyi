from typing import Any

class KitsuClient:
    pass

default_client: KitsuClient

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
