# Flake8 и его 100 плагинов

[Flake8](https://github.com/PyCQA/flake8)  основан на **mccabe**, **pycodestyle** и **pyflakes**.
Коротко об этих инструментах:
- **mccabe** - подсчет цикломатичной(структурной) сложности кода.
- **pycodestyle** - стилистический линтер.
- **pyflakes** - логический линтер.

Список используемых [plugins](https://github.com/DmytroLitvinov/awesome-flake8-extensions):
- [**flake8-async**](https://github.com/cooperlees/flake8-async) - ищет плохие практики использвоания async/asyncio в коде.
- [**flake8-requirements**](https://github.com/Arkq/flake8-requirements) - проверяет используемые зависимости.
- [**flake8-unused-arguments**](https://github.com/nhoad/flake8-unused-arguments) - проверяет не используемые аргументы.
- [**flake8-black**](https://github.com/peterjc/flake8-black) - проверяет согласно форматированию black.
- [**flake8-isort**](https://github.com/gforcada/flake8-isort) - проверяет последовательность импортов.
- [**flake8-expression-complexity**](https://github.com/best-doctor/flake8-expression-complexity) - проверяет сложность выражения.
- [**flake8-annotations-complexity**](https://github.com/best-doctor/flake8-annotations-complexity) - проверяет сложность аннотаций типов.
- [**flake8-functions**](https://github.com/best-doctor/flake8-functions) - проверяет различные параметры функции (длину, чистоту, количество аргументов и тд).
- [**flake8-cognitive-complexity**](https://github.com/Melevir/flake8-cognitive-complexity) - проверяет цикломатическую сложность.
- [**nitpick**](https://github.com/andreoliwa/nitpick) - инструмент для синхронизации зависимостей.
- [**pep8-naming**](https://github.com/PyCQA/pep8-naming) - проверяет нейминг согласно `pep8`.
- [**flake8-builtins**](https://github.com/gforcada/flake8-builtins) - запрещает именовать как `builtins`.
- [**flake8-docstrings**](https://github.com/PyCQA/flake8-docstrings) - проверяет формат докстрингов.
- [**flake8-print**](https://github.com/JBKahn/flake8-print) - запрещает print в коде.
- [**flake8-noqa**](https://github.com/plinss/flake8-noqa) - проверяет написание noqa в коде.
- [**flake8-spellcheck**](https://github.com/MichaelAquilina/flake8-spellcheck) - ищет опечатки.
- [**flake8-string-format**](https://github.com/xZise/flake8-string-format) - проверяет формат аргументов при форматирвоании строк.
- [**flake8-annotations**](https://github.com/sco1/flake8-annotations) - проверяет наличие аннотаций.
- [**flake8-pep585**](https://github.com/decorator-factory/flake8-pep585) - запрещает deprecated аннотации типов.
