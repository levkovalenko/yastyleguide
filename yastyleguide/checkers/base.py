import ast
from typing import Type

from yastyleguide.types import ERROR_GENERATOR


class BaseChecker:
    """Base checker class."""

    base_visitor: Type[ast.NodeVisitor]

    def __init__(self, tree: ast.AST, **kwargs):
        """Create base checker with visitor and run it on tree.

        Args:
            visitor (ast.NodeVisitor): nodes visitor.
            tree (ast.AST): ast nodes for checking.
        """
        self.visitor = self.base_visitor()
        self.visitor.visit(tree)
        self._set_options(**kwargs)

    def _set_options(self, **kwargs):
        """Set checker options."""
        ...

    def errors(self) -> ERROR_GENERATOR:
        """Rule for linter errors generator.

        Raises:
            NotImplementedError: There is no inplementation here.

        Yield:
            ERROR_GENERATOR: errors in flake format.
        """
        raise NotImplementedError

    @classmethod
    def from_plugin(cls: Type["BaseChecker"], plugin) -> "BaseChecker":
        """Class method for initialization checker.

        Args:
            plugin: plugin with tree and options.

        Returns:
            "BaseChecker": checker object
        """
        return cls(plugin.tree, **plugin.options)
