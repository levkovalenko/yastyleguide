import ast
from collections import defaultdict
from typing import Dict

from .node_name import name
from .stop_node import stop_node
from .use_node import use_node


class ComplexityVisitor(ast.NodeVisitor):
    """Complexity visitor.

    It based on `ast.NodeVisitor` which can automatically visit each node for checking.
    Complexity visitor count nodes in line and node definitions per module.
    """

    DEFINITIONS = {
        "ClassDef": "class",
        "AsyncFunctionDef": "function",
        "FunctionDef": "function",
    }

    def __init__(self):
        """Create line visitor."""
        self.line_score: Dict[int, int] = defaultdict(int)
        self.unit_count: Dict[str, int] = defaultdict(int)

    def visit(self, node: ast.AST):
        """Method for calculating nodes in each line.

        I overload standart visit method.

        Args:
            node (ast.AST): ast node.
        """
        lineno = getattr(node, "lineno", None)
        node_type = name(node)

        if lineno and use_node(node):
            self.line_score[lineno] += 1

        if stop_node(node):
            return

        if node_type in self.DEFINITIONS:
            self.unit_count[self.DEFINITIONS[node_type]] += 1

        super().visit(node)
