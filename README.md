# Gazu type stubs

This repository holds type stubs for [CGWire's Gazu](https://github.com/cgwire/gazu/) Python API.

Note: This is WIP for the moment

## Example

```python
import gazu

gazu.set_host("https://zou.cgwire.com/api")
gazu.log_in(email="email@example.com", password="password")

project = gazu.project.get_project_by_name("My Project")
reveal_type(project) # Type of "project" is "ProjectDict | None"

gazu.project.update_project({"fps": 30}) # Missing key "id" for TypedDict "ProjectDictPartial"
```

## Installation

Currently the project is not hosted on PyPi so you can install it directly from git:

```shell
❯ pip install git+https://github.com/johhnry/gazu-stubs.git
```

Or with Poetry/uv, add this to your dev dependencies:

```shell
❯ poetry add -G dev git+https://github.com/johhnry/gazu-stubs.git

# Or with uv
❯ uv add --dev git+https://github.com/johhnry/gazu-stubs.git
```
