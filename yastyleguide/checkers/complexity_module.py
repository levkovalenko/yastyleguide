from statistics import median
from typing import Dict, List, Tuple

from yastyleguide.types import ERROR, ERROR_GENERATOR
from yastyleguide.visitors import ComplexityVisitor

from .base import BaseChecker


class ModuleComplexityChecker(BaseChecker):
    """Check loop statement into ast tree."""

    base_visitor = ComplexityVisitor

    max_line_count: int
    max_module_complexity: int
    max_function_defs: int
    max_class_defs: int

    line_count_template: str = "YASG203 To many lines per module, {0} > {1}."
    module_complexity_template: str = (
        "YASG202 To big median line complexity in module, {0} > {1}."
    )
    function_defs_template: str = (
        "YASG204 To many function definitions per module, {0} > {1}."
    )
    class_defs_template: str = (
        "YASG205 To many class definitions per module, {0} > {1}."
    )

    def _set_options(
        self,
        max_line_count: int = 200,
        max_module_complexity: int = 12,
        max_function_definitions: int = 8,
        max_class_definitions: int = 3,
        **kwargs,
    ):
        """Set checker options.

        Args:
            max_line_count (int, optional): max line count per module. Defaults to 200.
            max_module_complexity (int, optional): max json complexity. Defaults to 12.
            max_function_definitions (int, optional): function definitions per module.
                                    Defaults to 8.
            max_class_definitions (int, optional): class definitions per module.
                                    Defaults to 3.
        """
        self.max_line_count = max_line_count
        self.max_module_complexity = max_module_complexity
        self.max_function_defs = max_function_definitions
        self.max_class_defs = max_class_definitions

    def _check(self, value: int, expected: int, template: str) -> ERROR:
        if value <= expected:
            return -1, -1, "", None
        text = template.format(value, expected)
        return 0, 0, text, type(self.visitor)

    def errors(self) -> ERROR_GENERATOR:
        """Rule for linter errors generator.

        Yield:
            ERROR_GENERATOR: errors in flake format.
        """
        # We use one implementation of NodeVisitor
        line_score: Dict[int, int] = self.visitor.line_score  # type: ignore
        unit_count: Dict[str, int] = self.visitor.unit_count  # type: ignore

        line_count = len(line_score)

        if line_count == 0:
            return

        module_score = int(median(line_score.values()))  # noqa: PD011
        function_definitions = unit_count["function"]
        class_definitions = unit_count["class"]

        checks: List[Tuple[int, int, str]] = [
            (line_count, self.max_line_count, self.line_count_template),
            (module_score, self.max_module_complexity, self.module_complexity_template),
            (function_definitions, self.max_function_defs, self.function_defs_template),
            (class_definitions, self.max_class_defs, self.class_defs_template),
        ]
        check_results = [self._check(*params) for params in checks]
        errors = filter(lambda x: x[0] != -1, check_results)
        yield from errors
