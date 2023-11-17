from random import random


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current, key):
        if key < current.key:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert_recursive(current.left, key)
        elif key > current.key:
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert_recursive(current.right, key)

    def symmetrical_traversal(self):
        result = []
        stack = []
        current = self.root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.key)
            current = current.right

        return result

    def preorder_traversal(self):
        result = []
        stack = [self.root]
        while stack:
            node = stack.pop()
            if node:
                result.append(node.key)
                stack.append(node.right)
                stack.append(node.left)

        return result

    def postorder_traversal(self):
        result = []
        stack = [(self.root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    result.append(node.key)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))

        return result

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self._delete_recursive(root.left, key)
        elif key > root.key:
            root.right = self._delete_recursive(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            root.key = self._get_min_value(root.right)
            root.right = self._delete_recursive(root.right, root.key)

        return root

    def _get_min_value(self, node):
        while node.left:
            node = node.left
        return node.key

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def print_tree(self):
        result = []
        self.symmetrical_traversal(self.root, result)
        print("Симметричный обход (symmetrical):", result)

    def print_preorder(self):
        result = self.preorder_traversal()
        print("Прямой обход (preorder):", result)

    def print_postorder(self):
        result = self.postorder_traversal()
        print("Обратный обход (postorder):", result)

    def is_empty(self):
        return self.root is None

    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if node is None:
            return 0
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        return max(left_height, right_height) + 1

    def print_pretty_tree(self):
        print("Красивый вывод дерева:")
        self._print_pretty_tree_recursive(self.root, 0)
        print()

    def _print_pretty_tree_recursive(self, node, level):
        if node is not None:
            self._print_pretty_tree_recursive(node.right, level + 1)
            print("  " * level + str(node.key))
            self._print_pretty_tree_recursive(node.left, level + 1)

    def max_occurrence(self):
        if self.root is None:
            return 0

        max_count = 0

        def _max_occurrence_recursive(node, count_dict):
            nonlocal max_count

            if node is None:
                return

            key = node.key
            count_dict[key] = count_dict.get(key, 0) + 1
            max_count = max(max_count, count_dict[key])

            _max_occurrence_recursive(node.left, count_dict)
            _max_occurrence_recursive(node.right, count_dict)

        _max_occurrence_recursive(self.root, {})

        return max_count


def main():
    bst = BinarySearchTree()

    while True:
        print("\nВыберите действие:")
        print("1. Вставить элемент")
        print("2. Удалить элемент")
        print("3. Поиск элемента")
        # print("4. Вывести дерево")
        print("5. Вывести обходы дерева")
        print("6. Проверить на пустоту")
        print("7. Вывести высоту дерева")
        print("8. Вывести красивое дерево")
        print("9. Прямой обход")
        print("10. Обратный обход")
        print("11. Симметричный обход")
        # print("12. Максимальное кол-во равных эл-тов")
        print("0. Выйти из программы")

        choice = input("Ваш выбор: ")

        if choice == '1':
            key = int(input("Введите ключ для вставки: "))
            bst.insert(key)
        elif choice == '2':
            key = int(input("Введите ключ для удаления: "))
            bst.delete(key)
        elif choice == '3':
            key = int(input("Введите ключ для поиска: "))
            if bst.search(key):
                print("Элемент найден.")
            else:
                print("Элемент не найден.")
        # elif choice == '4':
        #     bst.print_tree()
        elif choice == '5':
            print("\nПрямой обход:")
            print(bst.preorder_traversal())
            print("\nОбратный обход:")
            print(bst.postorder_traversal())
            print("\nСимметричный обход:")
            print(bst.symmetrical_traversal())
        elif choice == '6':
            if bst.is_empty():
                print("Дерево пусто.")
            else:
                print("Дерево не пусто.")
        elif choice == '7':
            print("Высота дерева:", bst.height())
        elif choice == '8':
            bst.print_pretty_tree()
        elif choice == '9':
            print("Прямой обход:")
            print(bst.preorder_traversal())
        elif choice == '10':
            print("Обратный обход:")
            print(bst.postorder_traversal())
        elif choice == '11':
            print("Симметричный обход:")
            print(bst.symmetrical_traversal())
            # ... (your existing code)
        # elif choice == '12':
        #     max_count = bst.max_occurrence()
        #     print("Максимальное количество одинаковых элементов в дереве:", max_count)

        elif choice == '0':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
