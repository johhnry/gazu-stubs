from typing import Any

def normalize_model_parameter(
    model_parameter: dict[str, Any] | str | None
) -> dict[str, Any] | None: ...
def normalize_list_of_models_for_links(
    models: list[dict[str, Any]] = []
) -> list[dict[str, Any]]: ...
def validate_date_format(date_text: str) -> str: ...
def sanitize_filename(filename: str) -> str: ...
def download_file(
    url: str, file_path: str | None = None, headers: dict[str, Any] = {}
) -> str: ...