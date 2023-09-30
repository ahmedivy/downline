import graphviz

from typing import Self


class Commission:
    def __init__(self, amount: float, source: "Node", type: str, level: int = None, pair: int = None):
        self.amount = amount
        self.source = source
        self.type = type

        if self.type == "indirect":
            self.level = level
            self.pair = pair


class Node:
    def __init__(self, name: str, parent: Self = None):
        self.name = name
        self.parent = parent
        self.lefts: list[Self] = []
        self.rights: list[Self] = []
        self.ancestors: list[Self] = parent.ancestors + [parent] if parent else []

        self.commissions: list[Commission] = []

        if parent:
            self.parent.add_child(self)

        self.calc_commissions()

    def calc_commissions(self) -> float:
        if self.parent:
            direct = Commission(0.5, self, "direct")
            self.parent.commissions.append(direct)

        pairs = self.get_child_pairs()

        for i, (left, right) in enumerate(pairs, start=1):
            level_count = []
            self.count_children_at_each_level(left, 0, level_count, [left, right])
            print(level_count)

    def add_child(self, child: Self):
        if len(self.lefts) == len(self.rights):
            self.lefts.append(child)
        else:
            self.rights.append(child)

    def count_children_at_each_level(self, node, level, level_counts, children=None):
        if level >= len(level_counts):
            level_counts.append(0)
        level_counts[level] += len(node.children)

        children = children or node.children
        for child in node.children:
            self.count_children_at_each_level(child, level + 1, level_counts)

    def __repr__(self):
        return f'{self.name}'

    def __str__(self):
        return self.__repr__()

    @property
    def children(self) -> list[Self]:
        return self.lefts + self.rights

    @property
    def siblings(self) -> list[Self]:
        return self.parent.children - [self]

    def get_child_pairs(self):
        return [(left, right) for left, right in zip(self.lefts, self.rights)]

    def get_pairs_count(self, node: Self) -> int:
        ...


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

    d = Node("d", b)
    e = Node("e", b)

    f = Node("f", c)
    g = Node("g", c)

    print_tree(a).render("out/tree", view=True, format="png")


if __name__ == "__main__":
    main()
