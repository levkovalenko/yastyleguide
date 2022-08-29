import ast


def name(node: ast.AST) -> str:
    """Get name ast node.

    Args:
        node (ast.AST): ast node.

    Returns:
        str: name of ast node.
    """
    return node.__class__.__name__
