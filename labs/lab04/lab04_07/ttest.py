class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListCyclo:
    def __init__(self):
        self.head = None
        self.length = 0

    def push_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            self.head = new_node
        self.length += 1
        return data

    def push_back(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
        self.length += 1
        return data

    def push(self, index, data):
        if index < 0:
            index += self.length
        if index < 0 or index > self.length:
            return "Index is out of range"
        elif index == 0:
            return self.push_front(data)
        elif index == self.length:
            return self.push_back(data)
        else:
            new_node = Node(data)
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            self.length += 1
            return data

    def pop_front(self):
        if self.head is None:
            return "Insufficient data"
        old_head = self.head
        data = old_head.data
        if self.length == 1:
            self.head = None
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            self.head = old_head.next
            current.next = self.head
        self.length -= 1
        return data

    def pop_back(self):
        if self.head is None:
            return "Insufficient data"
        current = self.head
        prev = None
        while current.next != self.head:
            prev = current
            current = current.next
        data = current.data
        if prev is not None:
            prev.next = self.head
        else:
            self.head = None
        self.length -= 1
        return data

    def pop(self, index):
        if index < 0:
            index += self.length
        if index < 0 or index >= self.length:
            return "Index out of range"
        elif index == 0:
            return self.pop_front()
        else:
            current = self.head
            prev = None
            for _ in range(index):
                prev = current
                current = current.next
            data = current.data
            prev.next = current.next
            self.length -= 1
            return data

    def find_index(self, index):
        if index < 0:
            index += self.length
        if index >= self.length:
            return "Index out of range"
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def find_value(self, value):
        index = 0
        flag = False
        current = self.head
        if self.head is None:
            print("List is empty")
            return
        while True:
            if str(current.data) == str(value):
                flag = True
                break
            current = current.next
            index += 1
            if current == self.head:
                break
        if flag:
            return index
        else:
            return "Node is not present in the list"

    def is_empty(self):
        return self.length == 0

    def reverse(self):
        if self.is_empty():
            print("Список пуст. Невозможно выполнить реверс.")
            return

        prev = None
        current = self.head
        while True:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            if current == self.head:
                break

        self.head = prev

    def print_(self):
        if self.is_empty():
            print("Список пуст.")
            return

        temp = self.head
        while True:
            if temp is not None:
                print(temp.data, end=" -> ")
                temp = temp.next
                if temp == self.head:
                    print("...")
                    break
            else:
                break

    def clear(self):
        if self.head is None:
            print("List is clean")
            return
        current = self.head
        while True:
            new_node = current
            current = current.next
            if current == self.head:
                break
            del new_node
        self.head = None
        self.length = 0

    def are_sets_equal(self, other_list):
        if self.length != other_list.length:
            return False

        self_set = set()
        current = self.head
        while True:
            if current is not None:
                self_set.add(current.data)
                current = current.next
                if current == self.head:
                    break
            else:
                return False

        other_set = set()
        current = other_list.head
        while True:
            if current is not None:
                other_set.add(current.data)
                current = current.next
                if current == other_list.head:
                    break
            else:
                return False

        return self_set == other_set


def intersection(L1, L2):
    if L1.head is None or L2.head is None:
        return "One or both input lists are empty"

    result_list = LinkedListCyclo()

    current1 = L1.head
    while current1 is not None:
        current2 = L2.head
        while current2 is not None:
            if current1.data == current2.data:
                result_list.push_back(current1.data)
                break

            current2 = current2.next
            if current2 == L2.head:
                break

        current1 = current1.next
        if current1 == L1.head:
            break

    return result_list


def main():
    list1 = LinkedListCyclo()

    while True:
        print("\nLinked List Operations:")
        print("1. Insert at the beginning")
        print("2. Insert before a specified value")
        print("3. Insert after a specified value")
        print("4. Insert at the end")
        print("5. Delete from the beginning")
        print("6. Delete before a specified value")
        print("7. Delete after a specified value")
        print("8. Delete a specific element")
        print("9. Delete from the end")
        print("10. Clear the list")
        print("11. Find element by value")
        print("12. Reverse the list")
        print("13. Check if two lists have the same set of elements")
        print("14. Find intersection of two lists")
        print("15. Print the elements of the list")
        print("16. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = input("Enter data to insert at the beginning: ")
            list1.push_front(data)
        elif choice == 2:
            value = input("Enter value before which to insert: ")
            data = input("Enter data to insert: ")
            index = list1.find_value(value)
            if index == "Node is not present in the list":
                print(index)
            else:
                list1.push(index, data)
        elif choice == 3:
            value = input("Enter value after which to insert: ")
            data = input("Enter data to insert: ")
            index = list1.find_value(value)
            if index == "Node is not present in the list":
                print(index)
            else:
                list1.push(index + 1, data)
        elif choice == 4:
            data = input("Enter data to insert at the end: ")
            list1.push_back(data)
        elif choice == 5:
            list1.pop_front()
        elif choice == 6:
            value = input("Enter value before which to delete: ")
            index = list1.find_value(value)
            if index == "Node is not present in the list":
                print(index)
            else:
                list1.pop(index - 1)
        elif choice == 7:
            value = input("Enter value after which to delete: ")
            index = list1.find_value(value)
            if index == "Node is not present in the list":
                print(index)
            else:
                list1.pop(index + 1)
        elif choice == 8:
            value = input("Enter value to delete: ")
            index = list1.find_value(value)
            if index == "Node is not present in the list":
                print(index)
            else:
                list1.pop(index)
        elif choice == 9:
            list1.pop_back()
        elif choice == 10:
            list1.clear()
        elif choice == 11:
            value = input("Enter value to find: ")
            index = list1.find_value(value)
            if index == "Node is not present in the list":
                print(index)
            else:
                print(f"The value '{value}' is at index {index}.")
        elif choice == 12:
            list1.reverse()
        elif choice == 13:
            list2 = LinkedListCyclo()
            print("Create a second list for comparison:")
            while True:
                data = input("Enter data (or 'exit' to finish): ")
                if data == 'exit':
                    break
                list2.push_back(data)
            if list1.are_sets_equal(list2):
                print("The two lists have the same set of elements.")
            else:
                print("The two lists do not have the same set of elements.")
        elif choice == 14:
            list2 = LinkedListCyclo()
            print("Create a second list for intersection:")
            while True:
                data = input("Enter data (or 'exit' to finish): ")
                if data == 'exit':
                    break
                list2.push_back(data)
            intersection_result = intersection(list1, list2)
            print("Intersection of the two lists:")
            intersection_result.print_()
        elif choice == 15:
            print("Elements of the list:")
            list1.print_()
        elif choice == 16:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
