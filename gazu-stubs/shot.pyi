from typing import Any, Literal

from .client import KitsuClient, default_client
from .entity import EntityDict
from .project import ProjectDict

class ShotDict(EntityDict):
    episode_id: str | None
    episode_name: str
    fps: float | None
    frame_in: int | None
    frame_out: int | None
    nb_frames: int
    project_name: str
    sequence_id: str
    sequence_name: str
    # tasks: ?
    type: Literal["Shot"]

class SequenceDict(EntityDict):
    nb_frames: int | None
    project_name: str
    type: Literal["Sequence"]

class EpisodeDict(EntityDict):
    project_name: str
    type: Literal["Episode"]

def get_shot(shot_id: str, client: KitsuClient = default_client) -> ShotDict: ...
def get_shot_by_name(
    sequence: str | SequenceDict, shot_name: str, client: KitsuClient = default_client
) -> ShotDict | None: ...
def new_shot(
    project: str | ProjectDict,
    sequence: str | SequenceDict,
    name: str,
    nb_frames: int | None = None,
    frame_in: int | None = None,
    frame_out: int | None = None,
    description: str | None = None,
    data: dict[str, Any] = {},
    client: KitsuClient = default_client,
) -> ShotDict: ...
def update_shot(shot: ShotDict, client: KitsuClient = default_client) -> ShotDict: ...
def update_shot_data(
    shot: ShotDict, data: dict[str, Any] = {}, client: KitsuClient = default_client
) -> ShotDict: ...
def remove_shot(
    shot: str | ShotDict, force: bool = False, client: KitsuClient = default_client
) -> None: ...
def get_sequence(
    sequence_id: str, client: KitsuClient = default_client
) -> SequenceDict: ...
def get_sequence_by_name(
    project: str | ProjectDict,
    sequence_name: str,
    episode: str | EpisodeDict | None = None,
    client: KitsuClient = default_client,
) -> SequenceDict | None: ...
def new_sequence(
    project: str | ProjectDict,
    name: str,
    episode: str | EpisodeDict | None = None,
    client: KitsuClient = default_client,
) -> SequenceDict: ...
def update_sequence(
    sequence: SequenceDict, client: KitsuClient = default_client
) -> SequenceDict: ...
def update_sequence_data(
    sequence: SequenceDict,
    data: dict[str, Any] = {},
    client: KitsuClient = default_client,
) -> SequenceDict: ...
def remove_sequence(
    sequence: str | SequenceDict,
    force: bool = False,
    client: KitsuClient = default_client,
) -> None: ...
def get_episode(
    episode_id: str, client: KitsuClient = default_client
) -> EpisodeDict: ...
def get_episode_by_name(
    project: ProjectDict | str, episode_name: str, client: KitsuClient = default_client
) -> EpisodeDict | None: ...
def new_episode(
    project: str | ProjectDict, name: str, client: KitsuClient = default_client
) -> SequenceDict: ...
def update_episode(
    episode: EpisodeDict, client: KitsuClient = default_client
) -> EpisodeDict: ...
def update_episode_data(
    episode: EpisodeDict,
    data: dict[str, Any] = {},
    client: KitsuClient = default_client,
) -> EpisodeDict: ...
def remove_episode(
    episode: str | EpisodeDict,
    force: bool = False,
    client: KitsuClient = default_client,
) -> None: ...
def all_shots_for_project(
    project: ProjectDict | str, client: KitsuClient = default_client
) -> list[ShotDict]: ...
def all_shots_for_episode(
    episode: EpisodeDict | str, client: KitsuClient = default_client
) -> list[ShotDict]: ...
def all_shots_for_sequence(
    sequence: SequenceDict | str, client: KitsuClient = default_client
) -> list[ShotDict]: ...
def all_sequences_for_project(
    project: ProjectDict, client: KitsuClient = default_client
) -> list[SequenceDict]: ...
def all_sequences_for_episode(
    episode: EpisodeDict | str, client: KitsuClient = default_client
) -> list[SequenceDict]: ...
def all_episodes_for_project(
    project: ProjectDict, client: KitsuClient = default_client
) -> list[EpisodeDict]: ...
