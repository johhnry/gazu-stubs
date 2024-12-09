from typing import Literal, TypedDict

from .client import KitsuClient, default_client

_PersonContract = Literal[
    "open-ended",
    "fixed-term",
    "short-term",
    "freelance",
    "apprentice",
    "internship",
]

_PersonRole = Literal["admin", "user", "supervisor", "manager"]

class PersonDict(TypedDict):
    first_name: str
    last_name: str
    email: str
    phone: str | None
    contract_type: _PersonContract
    active: bool
    archived: bool
    last_presence: str | None
    desktop_login: str | None
    login_failed_attemps: int
    last_login_failed: str
    totp_enabled: bool
    email_otp_enabled: bool
    fido_enabled: bool
    preferred_two_factor_authentication: str | None
    shotgun_id: str
    timezone: str
    locale: str
    data: None
    role: _PersonRole
    has_avatar: bool
    notifications_enabled: bool
    notifications_slack_enabled: bool
    notifications_slack_userid: str
    notifications_mattermost_enabled: bool
    notifications_mattermost_userid: str
    notifications_discord_enabled: bool
    notifications_discord_userid: bool
    is_bot: bool
    expiration_date: str | None
    studio_id: str
    is_generated_from_ldap: bool
    ldap_uid: str | None
    full_name: str
    id: str
    created_at: str
    updated_at: str
    type: Literal["Person"]
    fido_devices: list[str]

class DepartmentDict(TypedDict):
    archived: bool
    color: str
    created_at: str
    id: str
    name: str
    type: Literal["Department"]
    updated_at: str

def get_person(
    id: str, relations: bool = False, client: KitsuClient = default_client
) -> PersonDict: ...
def all_persons(client: KitsuClient = default_client) -> list[PersonDict]: ...
def get_person_by_email(
    email: str, client: KitsuClient = default_client
) -> PersonDict | None: ...
def get_department(
    department_id: str, client: KitsuClient = default_client
) -> DepartmentDict: ...
