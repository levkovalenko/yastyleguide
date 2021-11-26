import ast

from flake8.options.manager import OptionManager

from . import __version__
from .checkers import LoopChecker
from .types import ERROR_GENERATOR


class YASGPlugun:
    """Checker for yastyleguide."""

    version = __version__
    name = "yastyleguide"
    visitors = [LoopChecker]

    def __init__(self, tree: ast.AST):
        """Init of flake8 plugin yastyleguide.

        Args:
            tree (ast.AST): ast nodes for checking.
        """
        self.tree = tree

    @classmethod
    def add_options(cls, parser: OptionManager, use_config=True):
        """Used by flake8 to add options."""
        pass

    @classmethod
    def parse_options(cls, options, _extra=None):
        """Used by flake8 to parse options."""
        pass

    def run(self) -> ERROR_GENERATOR:
        """Run plugin."""
        for visitor in self.visitors:
            yield from visitor.from_plugin(self).errors()
