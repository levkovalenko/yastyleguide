import ast
from functools import singledispatch

from .node_name import name


@singledispatch
def stop_node(node) -> bool:
    """Need stop at this node.

    Args:
        node (ast.Node): ast node.

    Returns:
        bool: default False.
    """
    return False


@stop_node.register
def negative_constant_node(node: ast.UnaryOp) -> bool:
    """Stop on unary operation on constant. Cause it is constant.

    Ex: -3 in ast is UnaryOp(op=USub, operand=Constant).
    So it is two ast nodes but for complexity it is one.

    Args:
        node (ast.UnaryOp): unary operation.

    Returns:
        bool: is it negative constant or not.
    """
    sub_constant = name(node.op) == "USub" and name(node.operand) == "Constant"
    return sub_constant


@stop_node.register
def increment_node(node: ast.BinOp) -> bool:
    """Stop on binary operation on constant equal 1. Cause it is increment.

    Args:
        node (ast.UnaryOp): binary operation.

    Returns:
        bool: is it increment or not.
    """
    increment = (
        name(node.op) == "Add"
        and isinstance(node.left, ast.Name)
        and isinstance(node.right, ast.Constant)
        and node.right.value == 1
    )
    return increment
