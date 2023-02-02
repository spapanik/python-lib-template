from __future__ import annotations

project = "{{cookiecutter.project_name}}"
project_copyright = "2022, {{cookiecutter.author_name}}"
author = "{{cookiecutter.author_name}}"

extensions: list[str] = []
templates_path = ["_templates"]
exclude_patterns: list[str] = []

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
