import ast

import pytest

from yastyleguide.visitors.complexity.use_node import use_node


@pytest.mark.parametrize(
    "node,solution",
    [
        (ast.Subscript(), False),
        (ast.Lambda(), False),
        (ast.Name(id="reduce"), True),
        (ast.Name(id="list"), False),
        (ast.Name(id="map"), False),
        (ast.Name(id="dict"), False),
        (ast.Tuple(elts=[ast.Constant(), ast.Name(), ast.Slice()]), False),
        (ast.Tuple(elts=[ast.Constant(), ast.Name(), ast.BinOp()]), True),
        (ast.Tuple(elts=[ast.Attribute()]), True),
        (ast.Tuple(elts=[ast.Call()]), True),
        (ast.For(), True),
        (ast.ClassDef(), True),
    ],
)
def test_use_node(node: ast.AST, solution: bool):
    assert use_node(node) is solution
