# Installation

# Using pip

[pip] is a package manager for Python.
You can use it to install `{{cookiecutter.project_name}}` and try it out:

```console
$ pip install {{cookiecutter.project_name}}
```

# Using poetry

[poetry] is a tool for managing Python project dependencies, and is the recommended way
to add `{{cookiecutter.project_name}}` to your project's dependencies. If you want to do so, you can do it
with the following command:

```console
$ poetry add {{cookiecutter.project_name}}
```

Or you can add `{{cookiecutter.project_name}}` to your `pyproject.toml` file:

```toml
[tool.poetry.dependencies]
{{cookiecutter.project_name}} = "^0.1"
```

## Python Version Requirement

Please note that `{{cookiecutter.project_name}}` requires Python 3.9 or higher. Please ensure
that you have such a version installed in your system. If not,
consider using a tool like [pyenv] to create a shell with the required Python version.

[pip]: https://pip.pypa.io/en/stable/
[poetry]: https://python-poetry.org/
[pyenv]: https://github.com/pyenv/pyenv
