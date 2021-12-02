import ast
from itertools import zip_longest
from typing import List, Tuple

import pytest

from yastyleguide.visitors import LoopVisitor

FOR = "for i in []: pass"
WHILE = "while Truezip_longest: pass"
LIST_COMP = "[i for i in []]"
DICT_COMP = "{i:i for i in []}"
GENERATOR = "(i for i in [])"
DOUBLE_FOR = """
for i in []:
    for j in []:
        pass
"""
DOUBLE_WHILE = """
while True:
    while False:
        pass
"""
WHILE_FOR = """
while True:
    for i in []:
        pass
"""
FOR_WHILE = """
for i in []:
    while True:
        break
"""


@pytest.mark.parametrize(
    "snippet,expected",
    [
        (FOR, [("For", 1, 0)]),
        (WHILE, [("While", 1, 0)]),
        (DOUBLE_FOR, [("For", 2, 0), ("For", 3, 4)]),
        (DOUBLE_WHILE, [("While", 2, 0), ("While", 3, 4)]),
        (WHILE_FOR, [("While", 2, 0), ("For", 3, 4)]),
        (FOR_WHILE, [("For", 2, 0), ("While", 3, 4)]),
        (LIST_COMP, []),
        (DICT_COMP, []),
        (GENERATOR, []),
    ],
)
def test_visitor(snippet: str, expected: List[Tuple[str, int, int]]):  # noqa: D103
    visitor = LoopVisitor()
    ast_tree = ast.parse(snippet)
    visitor.visit(ast_tree)

    for res, exp in zip_longest(visitor.loops, expected):  # noqa: YASG101
        assert res == LoopVisitor.Loop(*exp)
