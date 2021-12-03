from typing import Dict

from yastyleguide.types import ERROR_GENERATOR
from yastyleguide.visitors import ComplexityVisitor

from .base import BaseChecker


class LineComplexityChecker(BaseChecker):
    """Check loop statement into ast tree."""

    base_visitor = ComplexityVisitor
    template = "YASG201 Line is to complex, {0} > {1}. To many ast nodes per line."
    max_line_complexity: int

    def _set_options(self, max_line_complexity: int = 8, **kwargs):
        """Set checker options.

        Args:
            max_line_complexity (int, optional): max complexity. Defaults to 8.
        """
        self.max_line_complexity = max_line_complexity

    def errors(self) -> ERROR_GENERATOR:
        """Rule for linter errors generator.

        Yield:
            ERROR_GENERATOR: errors in flake format.
        """
        # We use one implementation of NodeVisitor
        line_score: Dict[int, int] = self.visitor.line_score  # type: ignore
        max_complexity = self.max_line_complexity
        yield from (
            (lineno, 0, self.template.format(score, max_complexity), type(self.visitor))
            for lineno, score in line_score.items()
            if score > max_complexity
        )
