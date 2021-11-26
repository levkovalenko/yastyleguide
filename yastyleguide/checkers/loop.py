from yastyleguide.types import ERROR_GENERATOR
from yastyleguide.visitors import LoopVisitor

from .base import BaseChecker


class LoopChecker(BaseChecker):
    """Check loop statement into ast tree."""

    base_visitor = LoopVisitor
    checks = {
        "For": "YASG101 Don't use any 'for' loops.",
        "While": "YASG102 Don't use any 'while' loops.",
    }

    def errors(self) -> ERROR_GENERATOR:
        """Rule for linter errors generator.

        Yield:
            ERROR_GENERATOR: errors in flake format.
        """
        # We use one implementation of NodeVisitor
        statements: LoopVisitor.Loop = self.visitor.loops  # type: ignore
        yield from (
            (lineno, col_offset, self.checks[error_name], type(self.visitor))
            for error_name, lineno, col_offset in statements
        )
