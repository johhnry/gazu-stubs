from typing import Any, Callable, NotRequired, TypeAlias, TypedDict
from urllib.parse import _QueryType  # pyright: ignore[reportPrivateUsage]

from gazu.person import PersonDict

# JSON type
# See:https://stackoverflow.com/a/77361801
_JSON: TypeAlias = dict[str, "_JSON"] | list["_JSON"] | str | int | float | bool | None

# Alias the urllib private type for parameters
_Params: TypeAlias = _QueryType

class _Tokens(TypedDict):
    access_token: str | None
    refresh_token: str | None

_CallbackNotAuthenticated: TypeAlias = Callable[[KitsuClient, str], bool]

_AuthHeaders = TypedDict(
    "_AuthHeaders", {"User-Agent": str, "Authorization": NotRequired[str]}
)

class KitsuClient:
    def __init__(
        self,
        host: str,
        ssl_verify: bool = True,
        cert: str | None = None,
        use_refresh_token: bool = True,
        callback_not_authenticated: _CallbackNotAuthenticated | None = None,
        tokens: _Tokens = {"access_token": None, "refresh_token": None},
        access_token: str | None = None,
        refresh_token: str | None = None,
    ) -> None: ...
    @property
    def access_token(self) -> str: ...
    @access_token.setter
    def access_token(self, token: str) -> None: ...
    @property
    def refresh_token(self) -> str: ...
    @refresh_token.setter
    def refresh_token(self, token: str) -> None: ...
    def refresh_access_token(self) -> _Tokens: ...
    def make_auth_header(self) -> _AuthHeaders: ...

def create_client(
    host: str,
    ssl_verify: bool = True,
    cert: str | None = None,
    use_refresh_token: bool = False,
    callback_not_authenticated: _CallbackNotAuthenticated | None = None,
    **kwargs: Any,
) -> KitsuClient: ...

default_client: KitsuClient

def host_is_up(client: KitsuClient = default_client) -> bool: ...
def host_is_valid(client: KitsuClient = default_client) -> bool: ...
def get_host(client: KitsuClient = default_client) -> str: ...
def get_api_url_from_host(client: KitsuClient = default_client) -> str: ...
def set_host(new_host: str, client: KitsuClient = default_client) -> str: ...
def get_event_host(client: KitsuClient = default_client) -> str: ...
def set_event_host(new_host: str, client: KitsuClient = default_client) -> str: ...
def set_tokens(
    new_tokens: _Tokens, client: KitsuClient = default_client
) -> _Tokens: ...
def make_auth_header(client: KitsuClient = default_client) -> _AuthHeaders: ...
def url_path_join(*items: str) -> str: ...
def get_full_url(path: str, client: KitsuClient = default_client) -> str: ...
def build_path_with_params(path: str, params: _Params | None) -> str: ...
def fetch_all(
    path: str,
    params: _Params | None = None,
    client: KitsuClient = default_client,
    paginated: bool = False,
    limit: int | None = None,
) -> list[_JSON]: ...
def fetch_first(
    path: str,
    params: _Params | None = None,
    client: KitsuClient = default_client,
) -> _JSON: ...
def fetch_one(
    model_name: str, id: str, client: KitsuClient = default_client
) -> _JSON: ...
def create(
    model_name: str, data: _JSON, client: KitsuClient = default_client
) -> _JSON: ...
def update(
    model_name: str, id: str, data: _JSON, client: KitsuClient = default_client
) -> _JSON: ...
def get(
    path: str,
    json_response: bool = True,
    params: _Params | None = None,
    client: KitsuClient = default_client,
) -> _JSON: ...
def post(
    path: str,
    data: _JSON = None,
    client: KitsuClient = default_client,
) -> _JSON: ...
def put(
    path: str,
    params: _Params | None = None,
    client: KitsuClient = default_client,
) -> _JSON: ...
def delete(
    path: str,
    params: _Params | None = None,
    client: KitsuClient = default_client,
) -> _JSON: ...
def get_api_version(client: KitsuClient = default_client) -> str: ...

class CurrentUserDict(PersonDict):
    departments: list[str]

def get_current_user(client: KitsuClient = default_client) -> CurrentUserDict: ...
