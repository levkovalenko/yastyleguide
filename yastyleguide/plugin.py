import ast
from argparse import Namespace
from typing import Union

from flake8.options.manager import OptionManager  # type: ignore

from . import __version__
from .checkers import LineComplexityChecker, LoopChecker
from .options import Config
from .types import ERROR_GENERATOR


class YASPlugin:
    """Checker for yastyleguide."""

    version = __version__
    name = "yastyleguide"
    visitors = [LoopChecker, LineComplexityChecker]
    options: dict[str, Union[str, int]]
    config: Config = Config()

    def __init__(self, tree: ast.AST):
        """Init of flake8 plugin yastyleguide.

        Args:
            tree (ast.AST): ast nodes for checking.
        """
        self.tree = tree

    @classmethod
    def add_options(cls, manager: OptionManager) -> None:
        """Used flake8 for add options.

        Args:
            manager (OptionManager): option manager.
        """
        cls.config.add_options(manager)

    @classmethod
    def parse_options(cls, options: Namespace) -> None:
        """Used flake8 for parse options.

        Args:
            options (Namespace): flake8 options object.
        """
        cls.options = cls.config.parse_options(options)

    def run(self) -> ERROR_GENERATOR:
        """Run plugin."""
        # I yield result of each visitor consistently.
        for visitor in self.visitors:  # noqa: YAS101
            yield from visitor.from_plugin(self).errors()
