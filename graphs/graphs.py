from functools import singledispatch
import expressions


class TreeNode:

    def __init__(self, value, *children):
        self.value = value
        self.children = children

    def __repr__(self):
        return f"{type(self).__name__}{(self.value,) + self.children}"

    def __str__(self):
        childstring = ", ".join(map(str, self.children))
        return f"{self.value!s} -> ({childstring})"


def postvisitor(tree, fn):
    return fn(tree, *(postvisitor(c, fn) for c in tree.children))


def previsitor(tree, fn, fn_parent=None):
    fn_out = fn(tree, fn_parent)

    for child in tree.children:
        previsitor(child, fn, fn_out)
