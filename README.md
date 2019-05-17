# Setup

1. init local version of python
   `$ pyenv local 3.7.2`
2. init virtual environment
   `$ python -m venv .venv`
3. select interpreter for current project in VSCode in .vscode/settings.json

```
{
  "python.pythonPath": ".venv/bin/python"
}
```

4. upgrade pip
   `$ python -m pip install --upgrade pip`
5. install code quality tools
   `$ python -m pip install flake8 black isort`
6. create config for isort

```
[settings]
multi_line_output=3
include_trailing_comma=True
force_grid_wrap=0
combine_as_imports=True
line_length=120
not_skip=__init__.p
```

7. create config for flake8

```
[flake8]
max-line-length = 120
max-complexity = 1
```

8. init git repository
   `$ git init`

9. add .gitignore file: python, virtualenv, vscode

10. add debug launch configuration
