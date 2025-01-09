from . import (
    asset,  # noqa: F401
    cache,  # noqa: F401
    casting,  # noqa: F401
    client,
    entity,  # noqa: F401
    events,  # noqa: F401
    exception,  # noqa: F401
    helpers,  # noqa: F401
    person,  # noqa: F401
    project,  # noqa: F401
    shot,  # noqa: F401
    task,  # noqa: F401
)
from . import client as raw  # noqa: F401
from .exception import (
    AuthFailedException,  # noqa: F401
    NotAuthenticatedException,  # noqa: F401
    ParameterException,  # noqa: F401
)

def set_host(url: str, client: client.KitsuClient = client.default_client) -> None: ...
def log_in(
    email: str,
    password: str,
    totp: str | None = None,
    email_otp: str | None = None,
    fido_authentication_response: str | None = None,
    recovery_code: str | None = None,
    client: client.KitsuClient = client.default_client,
) -> None: ...
def set_event_host(
    url: str, client: client.KitsuClient = client.default_client
) -> None: ...
