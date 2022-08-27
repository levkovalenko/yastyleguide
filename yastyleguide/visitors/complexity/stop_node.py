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
def _(node: ast.UnaryOp) -> bool:
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
