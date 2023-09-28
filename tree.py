import graphviz

from typing import Self
from itertools import zip_longest


class Pair:
    """
    Can be a pair of nodes or a pair of pairs or a pair of pairs of pairs etc.
    """

    def __init__(self, left, right):
        self.left = left
        self.right = right


class Commission:
    def __init__(self, amount: float, pair: Pair):
        self.amount = amount
        self.pair = pair


class Node:
    def __init__(self, name: str, parent: Self = None):
        self.name = name
        self.parent = parent
        self.lefts: list[Self] = []
        self.rights: list[Self] = []
        self.ancestors: list[Self] = parent.ancestors + [parent] if parent else []

        self.balance: float = 0

        if parent:
            self.parent.add_child(self)

    def calc_commission(self, commission: float = 0.5) -> float:
        for left, right in self.get_pairs():
            return left.calc_commission() + right.calc_commission() + commission
        return 0.0

    def add_child(self, child: Self):
        if len(self.lefts) == len(self.rights):
            self.lefts.append(child)
        else:
            self.rights.append(child)

    def __repr__(self):
        return f'{self.name} ({self.balance})'

    def __str__(self):
        return self.__repr__()

    @property
    def children(self) -> list[Self]:
        return self.lefts + self.rights

    @property
    def siblings(self) -> list[Self]:
        return self.parent.children - [self]

    def get_pairs(self) -> list[Pair]:
        return [Pair(left, right) for left, right in zip_longest(self.lefts, self.rights)]


def print_tree(node: Node):
    tree = graphviz.Digraph()
    tree.node(node.name, str(node))
    for child in node.children:
        tree.edge(node.name, child.name)
        tree.subgraph(print_tree(child))
    return tree


def main():
    a = Node("a")
    b = Node("b", a)
    c = Node("c", a)

    print_tree(a).render("out/tree", view=True, format="png")

    print(a.get_pairs())


if __name__ == "__main__":
    main()
