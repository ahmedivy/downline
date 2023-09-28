import graphviz

from typing import Self


class Node:
    def __init__(self, name: str, parent: Self = None):
        self.name = name
        self.parent = parent
        self.lefts: list[Self] = []
        self.rights: list[Self] = []
        self.ancestors: list[Self] = parent.ancestors + [parent] if parent else []

        self.balance = 0

        if parent:
            self.parent.add_child(self)

    def give_commission(self, commission: float = 0.5):
        ...

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
    def children(self):
        return self.lefts + self.rights

    @property
    def siblings(self):
        return self.parent.children - [self]

    def get_pairs(self):
        return [(left, right) for left, right in zip(self.lefts, self.rights)]


def print_tree(node: Node):
    tree = graphviz.Digraph()
    tree.node(node.name, str(node))
    for child in node.children:
        tree.edge(node.name, child.name)
        tree.subgraph(print_tree(child))
    return tree


def main():
    # 4 level complete tree
    a = Node("a")
    b = Node("b", a)
    c = Node("c", a)

    d = Node("d", b)
    e = Node("e", b)

    f = Node("f", a)
    g = Node("g", c)

    h = Node("h", c)
    i = Node("i", c)

    j = Node("j", d)
    k = Node("k", d)

    l = Node("l", e)
    m = Node("m", e)

    n = Node("n", f)
    o = Node("o", f)

    p = Node("p", g)
    q = Node("q", g)

    r = Node("r", h)
    s = Node("s", h)

    t = Node("t", i)
    u = Node("u", i)

    v = Node("v", j)
    w = Node("w", j)

    x = Node("x", k)
    y = Node("y", k)

    print_tree(a).render("tree", view=True, format="png")


if __name__ == "__main__":
    main()
