from typing import Literal

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
def get_shot_by_name(sequence: str | SequenceDict, shot_name: str, client: KitsuClient = default_client) -> ShotDict: ...
def get_sequence(
    sequence_id: str, client: KitsuClient = default_client
) -> SequenceDict: ...
def get_sequence_by_name(
    project: str | ProjectDict, sequence_name: str, episode: str | EpisodeDict | None = None, client: KitsuClient = default_client
) -> SequenceDict: ...
def get_episode(
    episode_id: str, client: KitsuClient = default_client
) -> EpisodeDict: ...
def get_episode_by_name(
    project: str | ProjectDict, episode_name: str, client: KitsuClient = default_client
) -> EpisodeDict: ...
