class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree():
    value = input("Введите значение корня дерева: ")
    root = TreeNode(int(value))
    build_tree_recursive(root)
    return root


def build_tree_recursive(node):
    left_value = input(f"Введите значение для левого потомка узла {node.value} (или 'None' для отсутствия): ")
    if left_value.lower() != 'none':
        node.left = TreeNode(int(left_value))
        build_tree_recursive(node.left)

    right_value = input(f"Введите значение для правого потомка узла {node.value} (или 'None' для отсутствия): ")
    if right_value.lower() != 'none':
        node.right = TreeNode(int(right_value))
        build_tree_recursive(node.right)


def max_equal_elements(root):
    if not root:
        return 0

    def dfs(node, count_dict):
        if not node:
            return

        count_dict[node.value] = count_dict.get(node.value, 0) + 1

        dfs(node.left, count_dict)
        dfs(node.right, count_dict)

    count_dict = {}
    dfs(root, count_dict)

    max_count = 0
    for count in count_dict.values():
        max_count = max(max_count, count)

    return max_count


user_tree = build_tree()
result = max_equal_elements(user_tree)
print("Максимальное количество одинаковых элементов:", result)
