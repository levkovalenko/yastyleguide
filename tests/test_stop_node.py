import ast

import pytest

from yastyleguide.visitors.complexity.stop_node import stop_node


@pytest.mark.parametrize(
    "snippet,solution",
    [
        ("-1", True),
        ("-constant", False),
        ("-call()", False),
        ("not True", False),
        ("~1", False),
        ("name+1", True),
        ("2+1", False),
        ("call()+1", False),
        ("(-name)+1", False),
        ("(name*name)+1", False),
    ],
)
def test_stop_node(snippet: str, solution: bool):
    ast_tree = ast.parse(snippet)
    node = ast_tree.body[0].value
    assert stop_node(node) is solution
