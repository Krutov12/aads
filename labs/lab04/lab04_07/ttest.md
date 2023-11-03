
<!-- #region -->



# Отчет

## Лабораторная работа №4

### Линейный однонаправленный циклический список

### Цель работы:

Изучение структуры данных «Циклические однонаправленные списки», а также основных операций над ними.

### Задачи:

1. Реализовать программу, выполняющую стандартный набор операций с линейным циклическим списком:

вставка элемента в начало списка;
вставка элемента в середину списка перед указанным значением;
вставка элемента в середину списка после указанного значения;
вставка элемента в конец списка;
удаление элемента в начале списка;
Удаление элемента, стоящего перед указанным значением списка;
Удаление элемента, стоящего после указанного значением списка;
удаление определенного элемента в списке;
удаление элемента в конце списка;
очистка списка;
поиск элемента списка по его значяению;
реверс списка (переворачивание списка задом на перед).
Требования:

список должен быть реализован в виде класса;
каждая операция должна быть реализована как метод класса;
добавлению/удалению должна предшествовать проверка возможности выполнения этих операций;
2. Реализовать приложение, для работы со списком, которое реализует следующий набор действий:

а) инициализация пустого линейного циклического списка;

б) организация диалогового цикла с пользователем;

### Листинг программного кода с описанием

class Node:
    def __init__(self,data)

class LinkedList:
    def __init__(self)
        
    def push_front(self, data) # Добавляет элемент в начало списка
    
    def push_back(self,data) # Добавляет элемент в коней списка

    def push(self,index,data) # Добавляет элемент в указаное место в списке
    
    def pop_front(self) # Удаляет первй элемент списка
    
    def pop_back(self) # Удаляет последний элемент списка

    def pop(self,index) # Удаляет указаный элемент списка

    def find_index(self,index) # Находит элемент по индексу

    def find_value(self, value) # ищет индекс элемента по значению
    
    def reverse(self) # Переворачивает список

    def print(self) # Выводит список

    def clear(self) # Очищает список

### Ответы на контрольные вопросы

1. Что такое динамическая структура данных?

Динамические структуры данных – это структуры данных, память под которые выделяется и освобождается программистом по мере необходимости. Динамические структуры данных в процессе существования в памяти могут изменять не только число составляю-щих их элементов, но и характер связей между элементами.

2. Что такое список?

Список — это упорядоченный набор элементов, каждый из которых имеет свой номер, или индекс, позволяющий быстро получить к нему доступ.

3. Какие виды списков существуют?

Списки бывают следующих видов:
- Маркированный. Перед элементом списка идет маркер.
- Нумерованный. Перед элементом списка идет номер.
- Список определений. Перед определением идет термин.
- Вложенный список.
- Многоуровневый. Список состоит из нескольких уровней. может быть маркированным. нумерованным и комбинированным.

4. Какие основные операции выполняются над списком?

Основными операциями над списками являются: 
· переход к очередному элементу списка; 
· добавление в список нового элемента; 
· поиск заданного элемента; 
· удаление элемента из списка. 
Выполнение этих операций основывается на использовании и изменении указателей. В отличие от очередей и стеков, элемент в список может быть добавлен в любое место.

5. Дать определение циклического списка.

Циклический (кольцевой) список – это структура данных, представляющая собой последовательность элементов, последний элемент которой содержит указатель на первый элемент списка, а первый (в случае двунаправленного списка) – на последний.
Основная особенность такой организации состоит в том, что в этом списке нет элементов, содержащих пустые указатели, и, следовательно, нельзя выделить крайние элементы.

6. Классификация циклических списков.

- Односвязный циклический список: каждый узел ОЦС содержит 1 поле указателя на следующий узел; поле указателя последнего узла содержит адрес первого узла (корня списка)
- Двусвязный циклический список: каждый узел ДЦС содержит два поля указателей: на следующий и на предыдущий узел; поле указателя на следующий узел последнего узла содержит адрес первого узла (корня списка); поле указателя на предыдущий узел первого узла (корня списка) содержит адрес последнего узла

7. Какие основные операции выполняются над циклическим списком?

- Добавление и удаление элементов
- Нахождение элементов
- Переворачивание списка




<!-- #endregion -->

```python
def intersection(L1, L2):
    if L1.head is None or L2.head is None:
        return "One or both input lists are empty"

    result_list = LinkedListCyclo()

    current1 = L1.head
    while True:
        current2 = L2.head
        while True:
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


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListCyclo:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1
        return data

    def push_back(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
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
            self.tail = None
        else:
            self.head = old_head.next
        old_head = None
        self.tail.next = self.head
        self.length -= 1
        return data

    def pop_back(self):
        if self.head is None:
            return "Insufficient data"
        old_tail = self.tail
        data = old_tail.data
        if self.length == 1:
            self.head = None
            self.tail = None
        elif self.head != self.tail:
            current = self.head
            while current.next != self.tail:
                current = current.next
            self.tail = current
            self.tail.next = self.head
        self.length -= 1
        return data

    def pop(self, index):
        if index < 0:
            index += self.length
        if index < 0 or index >= self.length:
            return "Index out of range"
        elif index == 0:
            return self.pop_front()
        elif index == self.length - 1:
            return self.pop_back()
        else:
            node = self.head
            for _ in range(index - 1):
                node = node.next
            new_node = node.next
            node.next = new_node.next
            data = new_node.data
            # del new_node
            self.length -= 1
            return data

    def find_index(self, index):
        if index < 0:
            index += self.length
        if index > self.length:
            return "Index out of range"
        current = self.head
        for _ in range(index - 1):
            current = current.next
        return current.data

    def find_value(self, value):
        index = 0
        flag = False
        current = self.head
        if self.head is None:
            print("List is empty")
            return
        while current != self.tail:
            if str(current.data) == str(value):
                flag = True
                break
            current = current.next
            index += 1
        if flag:
            return index
        else:
            return "Node is not present in the list"

    def reverse(self):
        if self.head is None:
            return "Not list"
        current = self.head
        prev_node = None
        while True:
            new_node = current.next
            current.next = prev_node
            prev_node = current
            current = new_node
            if current == self.head:
                break
        self.head = prev_node
        head = self.head.next
        tail = self.head
        while head is not None:
            tail = tail.next
            head = head.next
        self.tail = tail
        tail.next = self.head

    def print_(self):
        current = self.head
        if self.head is None:
            print("List is empty")
            return
        while True:
            print( current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print(" (Back to Head)")

    def clear(self):
        if self.head is None:
            print("List clean")
            return
        current = self.head.next
        while current != self.head:
            new_node = current
            current = current.next
            del new_node
        self.head = None
        self.tail = None
        self.length = 0

    def are_sets_equal(self, other_list):
        if self.length != other_list.length:
            return False

        self_set = set()
        current = self.head
        while True:
            self_set.add(current.data)
            current = current.next
            if current == self.head:
                break

        other_set = set()
        current = other_list.head
        while True:
            other_set.add(current.data)
            current = current.next
            if current == other_list.head:
                break

        return self_set == other_set


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
        elif choice == 15:
            print("Elements of the list:")
            list1.print_()
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
        elif choice == 16:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
