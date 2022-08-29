import ast

import pytest

from yastyleguide.visitors.complexity.node_name import name


@pytest.mark.parametrize(
    "node,node_name",
    [
        (ast.For(), "For"),
        (ast.Name(), "Name"),
        (ast.Constant(), "Constant"),
        (ast.Lambda(), "Lambda"),
        (ast.ClassDef(), "ClassDef"),
        (ast.FunctionDef(), "FunctionDef"),
    ],
)
def test_node_name_detect(node: ast.AST, node_name: str):
    assert name(node) == node_name
