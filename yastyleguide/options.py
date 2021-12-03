from typing import Any, Dict

from flake8.options.manager import OptionManager  # type: ignore


class Config:
    """Plugin configuration class."""

    options = {
        "max_line_complexity": {
            "type": "int",
            "default": 15,
            "help": (
                "User defined max line complexity."
                "Default max line complexity = 15"
                "For example: `--max-line-complexity=15`"
            ),
        },
        "max_line_count": {
            "type": "int",
            "default": 200,
            "help": (
                "User defined max line number in module."
                "Default max line number = 200."
                "For example: `--max-line-count=200`"
            ),
        },
        "max_module_complexity": {
            "type": "int",
            "default": 10,
            "help": (
                "User defined max module complexity."
                "Default max module complexity = 10."
                "For example: `--max-module-complexity=10`"
            ),
        },
        "max_function_definitions": {
            "type": "int",
            "default": 8,
            "help": (
                "User defined max number of function definitions."
                "Default max function definitions = 8."
                "For example: `--max-function-definitions=8`"
            ),
        },
        "max_class_definitions": {
            "type": "int",
            "default": 3,
            "help": (
                "User defined max number of class definitions."
                "Default max class definitions = 3."
                "For example: `--max-class-definitions=3`"
            ),
        },
    }

    def add_options(self, manager: OptionManager):
        """Add options to manager from config.

        Args:
            manager (OptionManager): manager for adding options.
        """
        # I consistently add options for manager, so i use for loop.
        for name, params in self.options.items():  # noqa: YASG101
            option_name = f"--{name.replace('_', '-')}"
            manager.add_option(option_name, **params)

    def parse_options(self, options) -> Dict[str, Any]:
        """Parse options from flake.

        Args:
            options (Options): flake options.

        Returns:
            Dict[str, Any]: dict of options.
        """
        return {option: getattr(options, option, None) for option in self.options}
