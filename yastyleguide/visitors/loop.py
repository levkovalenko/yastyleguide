import ast
from collections import namedtuple
from typing import List


class LoopVisitor(ast.NodeVisitor):
    """Loop statement visitor.

    It based on `ast.NodeVisitor` which can automatically visit each node for checking.
    I overload Loop nodes visitors for saving them as errors.
    """

    Loop = namedtuple("Loop", ("name", "lineno", "col_offset"))

    def __init__(self):
        """Create for statement visitor."""
        self.loops: List[LoopVisitor.Loop] = []

    def visit_For(self, node: ast.AST):  # noqa: N802
        """Visit For loop statement.

        Name is not in convention because `ast.NodeVisitor` use
        `generic_visit` to use visit for each node type.
        I overloadFor statement visit.

        Args:
            node ([ast.AST]): ast tree.
        """
        self.loops.append(LoopVisitor.Loop("For", node.lineno, node.col_offset))
        self.generic_visit(node)

    def visit_While(self, node: ast.AST):  # noqa: N802
        """Visit While loop statement.

        Name is not in convention because `ast.NodeVisitor` use
        `generic_visit` to use visit for each node type.
        I overload While statement visit.

        Args:
            node ([ast.AST]): ast tree.
        """
        self.loops.append(LoopVisitor.Loop("While", node.lineno, node.col_offset))
        self.generic_visit(node)
