# Flake 8 and his 100 plugins

[Flake8](https://github.com/PyCQA/flake8) based on **mccabe**, **pycodestyle** and **pyflakes**. 
A little bit information about this tools:
- **mccabe** - tool for calculating cyclomatic complexity of code.
- **pycodestyle** - python style linter.
- **pyflakes** - python logic linter. Try to found some issues in your code.

You can easily extend its capabilities with [plugins](https://github.com/DmytroLitvinov/awesome-flake8-extensions):
- [**flake8-bugbear**](https://github.com/PyCQA/flake8-bugbear) - flake plugin finding likely bugs and design problems in code. 
- [**flake8-comprehensions**](https://github.com/adamchainz/flake8-comprehensions) - flake plugin checking issues for any comprehensions.
- [**flake8-commas**](https://github.com/PyCQA/flake8-commas) - flake plugin for checking traling commas. It is incompatible with black format and add a lot of useless commas. I don't recomend it for using.
- [**flake8-docstrings**](https://github.com/PyCQA/flake8-docstrings) - flake plugin for checking docstrings conventions. Use with `docstring-convention=google`.
- [**flake8-eradicate**](https://github.com/wemake-services/flake8-eradicate) - flake plugin for checking commented code.
- [**flake8-isort**](https://github.com/gforcada/flake8-isort) - flake plugin for checking import order.
- [**flake8-broken-line**](https://github.com/wemake-services/flake8-broken-line) - flake linter for checking broken lines.
- [**pep8-naming**](https://github.com/PyCQA/pep8-naming) - flake linter for checking pep8 naming convention.
- [**flake8-string-format**](https://github.com/xZise/flake8-string-format) - flake linter for checking string format arguments.
- [**flake8-quotes**](https://github.com/zheller/flake8-quotes) - flake linter for checking quotes. Use with `--inline-quotes '"'`.
- [**flake8-bandit**](https://github.com/tylerwince/flake8-bandit) - flake integration bandit.
- [**flake8-debugger**](https://github.com/jbkahn/flake8-debugger) - flake linter for checking debug statements.
- [**flake8-builtins**](https://github.com/gforcada/flake8-builtins) - flake linter for checking variable names like builtins.
- [**pandas-vet**](https://github.com/deppen8/pandas-vet) - flake linter for checking pandas best practices.
- [**flake8-fastapi**](https://github.com/Kludex/flake8-fastapi) - flake linter for checking fastapi usage.
- [**flake8-black**](https://github.com/peterjc/flake8-black) - flake linter for checking black format.
- [**flake8-multiline-containers**](https://github.com/jsfehler/flake8-multiline-containers) - flake linter for checking multiline containers line breaks.
- [**flake8-expression-complexity**](https://github.com/best-doctor/flake8-expression-complexity) - flake linter for checking expression complexity.
- [**flake8-annotations-complexity**](https://github.com/best-doctor/flake8-annotations-complexity) - flake linter for checking annotations complexity.
- [**flake8-requirements**](https://github.com/Arkq/flake8-requirements) - flake linter for checking requirements.