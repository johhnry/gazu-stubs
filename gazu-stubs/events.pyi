from typing import Any, Callable

import socketio

from .client import KitsuClient, default_client

def init(
    client: KitsuClient = default_client,
    ssl_verify: bool = False,
    reconnection: bool = True,
    logger: bool = False,
    **kwargs: Any
) -> socketio.Client: ...
def add_listener(
    event_client: socketio.Client, event_name: str, event_handler: Callable[[Any], Any]
) -> None: ...
def run_client(event_client: socketio.Client) -> socketio.Client: ...
