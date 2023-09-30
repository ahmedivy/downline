class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []


def count_children_at_each_level(node, level, level_counts, children=None):
    if level >= len(level_counts):
        level_counts.append(0)

    children = children or node.children
    level_counts[level] += len(children)

    for child in children:
        count_children_at_each_level(child, level + 1, level_counts)


# Usage example
root = TreeNode("A")
b = TreeNode("B")
c = TreeNode("C")
d = TreeNode("D")
root.children.extend([b, c, d])
root.children[0].children.extend([TreeNode("E"), TreeNode("F")])
root.children[1].children.extend([TreeNode("G")])
root.children[2].children.extend([TreeNode("H"), TreeNode("I"), TreeNode("J")])

level_counts = []
count_children_at_each_level(root, 0, level_counts, [b, c])

for level, count in enumerate(level_counts):
    print(f"Level {level}: {count} children")
