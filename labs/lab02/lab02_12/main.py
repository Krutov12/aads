class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def push_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def push_back(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.size += 1

    def pop_front(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            poped_data = self.head.data
            self.head = None
            self.size -= 1
            return poped_data
        else:
            poped_data = self.head.data
            self.head = self.head.next
            self.size -= 1
            return poped_data

    def pop_back(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            poped_data = self.head.data
            self.head = None
            self.size -= 1
            return poped_data
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            poped_data = current.next.data
            current.next = None
            self.size -= 1
            return poped_data

    def at(self, index):
        if self.size == 0:
            return None
        else:
            if index < 0:
                index += self.size
            if index < 0 or index > self.size:
                raise IndexError("Incorrect index")
            current = self.head
            for i in range(index + 1):
                current = current.next
            return current.data

    def push(self, data, index):
        if index == 0:
            self.push_front(data)
        elif index == self.size:
            self.push_back(data)
        else:
            new_node = Node(data)
            current = self.head
            for i in range(index - 2):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.size += 1

    def pop(self, index):
        if self.size == 0:
            return None
        else:
            if index == -1:
                return self.pop_front()
            elif index == self.size:
                return self.pop_back()
            else:
                current = self.head
                for i in range(index - 2):
                    current = current.next
                to_remove = current.next
                current.next = to_remove.next
                poped_data = to_remove.data
                del to_remove
                self.size -= 1
                return poped_data

    def print_list(self):
        if self.size == 0:
            print('\n')
            print("List is empty")
            print('\n')
        else:
            current = self.head
            print("\n")
            while current.next is not None:
                print(current.data + " -> ", end='')
                current = current.next
            print(current.data)
            print("\n")

    def clear(self):
        while self.head is not None:
            to_remove = self.head
            self.head = self.head.next
            del to_remove
        self.size = 0

    def remove_unique_elements(self):
        """Написать функцию, которая удаляет из списка элементы, входящие в него только один раз."""
        if self.size == 0:
            print('\n')
            print("List is empty")
            print('\n')
        else:
            seen = set()
            duplicates = set()
            current = self.head
            while current is not None:
                if current.data in seen:
                    duplicates.add(current.data)
                else:
                    seen.add(current.data)
                current = current.next
            current = self.head
            while current.next is not None:
                if current.next.data not in duplicates:
                    to_remove = current.next
                    current.next = to_remove.next
                    del to_remove
                    self.size -= 1
                else:
                    current = current.next
            if self.size == 1:
                to_remove = self.head
                self.head = self.head.next
                del to_remove
                self.size = 0

    def even_and_odd(self):
        """Написать функцию, которая по списку L строит два новых списка: L1 – из четных и L2 – из нечетных элементов списка L."""
        if linked_list.head is None:
            print("empty")
        even_list = LinkedList()
        odd_list = LinkedList()
        current = linked_list.head
        while current:
            if int(current.data) % 2 == 0:
                even_list.push_back(current.data)
            else:
                odd_list.push_back(current.data)
            current = current.next
        print("")
        print("even list:", end='')
        even_list.print_list()
        print("odd list:", end='')
        odd_list.print_list()


def menu():
    print("1.     Push Front")
    print("2.     Push Back")
    print("3.     Push at Index")
    print("4.     Pop Front")
    print("5.     Pop Back")
    print("6.     Pop at Index")
    print("7.     Print List")
    print("8.     List Length")
    print("9.     Clear List")
    print("10.    Remove unique elements")
    print("11.    Get even and odd lists")
    print("0.     Exit")


linked_list = LinkedList()

while 1 > 0:
    menu()
    task = input("Enter your wish (0-11): ")

    if task == "0":
        print("\n")
        print("Exiting the program.")
        break
    elif task == "1":
        data = input("Enter data to push front: ")
        linked_list.push_front(data)
    elif task == "2":
        data = input("Enter data to push back: ")
        linked_list.push_back(data)
    elif task == "3":
        data = input("Enter data to push: ")
        index = int(input("Enter index to push at: "))
        linked_list.push(data, index)
    elif task == "4":
        popped_data = linked_list.pop_front()
        print("\n")
        print(f"Popped front: {popped_data}")
        print("\n")
    elif task == "5":
        popped_data = linked_list.pop_back()
        print("\n")
        print(f"Popped back: {popped_data}")
        print("\n")
    elif task == "6":
        index = int(input("Enter index to pop at: "))
        popped_data = linked_list.pop(index)
        print("\n")
        print(f"Popped at index {index}: {popped_data}")
        print("\n")
    elif task == "7":
        linked_list.print_list()
    elif task == "8":
        print("\n")
        print(f"Length of the list: {linked_list.size}")
        print("\n")
    elif task == "9":
        linked_list.clear()
        print("\n")
        print("List is empty.")
        print("\n")
    elif task == "10":
        linked_list.remove_unique_elements()
    elif task == "11":
        linked_list.even_and_odd()
    else:
        print("\n")
        print("Invalid choice. Please enter a number between 0 and 9.")
        print("\n")
