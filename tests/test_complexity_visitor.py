import ast
from typing import Dict

import pytest

from yastyleguide.visitors import ComplexityVisitor

FUNC = "function"
CLS = "class"
COMPLEX_LINE = "a = 1*2*3*4*5*6*7*8*9*10*11*12*13*14*15*16*17"
MULTI_COMPLEX_LINE = """
a = 1*2*3*4*5*6*7*8*9*10*11*12*13*14*15*16*17
b = 1*2*3*4*5*6*7*8*9*10*11*12*13*14*15*16
"""
CLASS_DEF = """class A: pass"""
NESTED_CLASS_DEF = """
class A:
    class B: pass
"""
DOUBLE_CLASS_DEF = """
class A: pass
class B: pass
"""
FUNC_DEF = "def f(): pass"
NESTED_FUNC_DEF = """
def f1():
    def f2(): pass
"""
DOUBLE_FUNC_DEF = """
def f1(): pass
def f2(): pass
"""
CLASS_FUNC_DEF = """
class A():
    def f(): pass
"""
FUNC_CLASS_DEF = """
def f():
    class A(): pass
"""


@pytest.mark.parametrize(
    "snippet,complexity,count",
    [
        (COMPLEX_LINE, {1: 35}, {FUNC: 0, CLS: 0}),
        (MULTI_COMPLEX_LINE, {2: 35, 3: 33}, {FUNC: 0, CLS: 0}),
        (CLASS_DEF, {1: 2}, {FUNC: 0, CLS: 1}),
        (FUNC_DEF, {1: 2}, {FUNC: 1, CLS: 0}),
        (DOUBLE_CLASS_DEF, {2: 2, 3: 2}, {FUNC: 0, CLS: 2}),
        (DOUBLE_FUNC_DEF, {2: 2, 3: 2}, {FUNC: 2, CLS: 0}),
        (NESTED_CLASS_DEF, {2: 1, 3: 2}, {FUNC: 0, CLS: 2}),
        (NESTED_FUNC_DEF, {2: 1, 3: 2}, {FUNC: 2, CLS: 0}),
        (CLASS_FUNC_DEF, {2: 1, 3: 2}, {FUNC: 1, CLS: 1}),
        (FUNC_CLASS_DEF, {2: 1, 3: 2}, {FUNC: 1, CLS: 1}),
    ],
)
def test_visitor(  # noqa: D103
    snippet: str, complexity: Dict[int, int], count: Dict[str, int]
):
    visitor = ComplexityVisitor()
    ast_tree = ast.parse(snippet)
    visitor.visit(ast_tree)

    assert len(visitor.line_score) == len(complexity)

    for lineno, score in visitor.line_score.items():  # noqa: YAS101
        assert lineno in complexity
        assert score == complexity[lineno]

    assert visitor.unit_count[FUNC] == count[FUNC]
    assert visitor.unit_count[CLS] == count[CLS]
