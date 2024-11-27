from . import (
    client,  # noqa: F401
    events,  # noqa: F401
    person,  # noqa: F401
    project,  # noqa: F401
    shot,  # noqa: F401
    task,  # noqa: F401
    asset,  # noqa: F401
    entity,  # noqa: F401
)
from .client import KitsuClient, default_client

def set_host(url: str, client: KitsuClient | None = default_client) -> None: ...
def log_in(
    email: str,
    password: str,
    totp: str | None = None,
    email_otp: str | None = None,
    fido_authentication_response: str | None = None,
    recovery_code: str | None = None,
    client: KitsuClient | None = None,
) -> None: ...
def set_event_host(url: str, client: KitsuClient | None = default_client) -> None: ...
