import ast
from functools import singledispatch

from .node_name import name


@singledispatch
def use_node(node) -> bool:
    """Decide to use node. False if skip it.

    Args:
        node (ast.Node): ast node.

    Returns:
        bool: default True.
    """
    return True


@use_node.register
def tuple_node(node: ast.Tuple) -> bool:
    """Skip ast.Tuple if it contains Constant, Slice or Variables.

    Args:
        node (ast.Tuple): tuple.

    Returns:
        bool: does contains Constant, Slice or Variables.
    """
    simple_nodes = ["Constant", "Slice", "Name"]
    slices = all(name(elt) in simple_nodes for elt in node.elts)
    return not slices


@use_node.register
def builin_node(node: ast.Name) -> bool:
    """Skip builtin names list and dict.

    Args:
        node (ast.Name): any name.

    Returns:
        bool: is node list or dict.
    """
    return node.id not in ["dict", "list", "map"]


@use_node.register(ast.Subscript)
@use_node.register(ast.Lambda)
def simple_node(_) -> bool:
    """Skip simple nodes.

    We decide what Lambda and Subscript are simple Node so skip it in complexity count.

    Args:
        _ (ast.Node): ast node.

    Returns:
        bool: default False.
    """
    return False
