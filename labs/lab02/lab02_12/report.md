## Песецкий Станислав - вариант 12

### ЛАБОРАТОРНАЯ РАБОТА: ОДНОСВЯЗНЫЙ СПИСОК НА PYTHON

**Цель:** Реализация односвязного списка и выполнение основных операций над ним.

**Листинг программного кода и результаты:**

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def push_front(self, data):  # ... (код метода)
        """Create new node on the heap using data.
        If head is null,
        set head to the new node pointer.
        Otherwise, 
        set the new node's next value to head,
        set head to the new node pointer.
        Increment the length."""
    
    def push_back(self, data):  # ... (код метода)
        """Create new node on the heap using data.
        If head is null,
        set head to the new node pointer.
        Otherwise,
        iterate over the linked list to find the last node,
        set the last node's "next" to the new node pointer.
        Increment the length."""

    def pop_front(self):  # ... (код метода)
        """Copy head to a new variable.
        // Note: The above line makes a copy of the POINTER,
        // not the node itself.
        Copy the head node's data to a new variable.
        If there is only one element in the list,
        set head to null.
        Otherwise,
        set head to its "next" pointer.
        Use the copy of the (old) head pointer to delete the node.
         Decrement the length.
       Return the (old) head node's data."""

    def pop_back(self):  # ... (код метода)
        """Create a variable to store the pointer to the node that will be removed.
        If there is only one element in the list,
        set the node to be removed to head,
        set head to null.
        Otherwise,
        iterate over the linked list to find the second-to-last node,
        set the node to be removed to the second-to-last node's "next",
        // i.e. the last node
        set the second-to-ast node's "next" to null.
        Copy the data in the node to be removed to a new variable.
        Delete the node to be removed, decrement the length and return the data.
        // not all in one line"""

    def at(self, index):  # ... (код метода)
        """If the index is negative, change it to itself plus the length of the list.
        If the index is still negative, or it is greater than the length of the list,
        throw an error.
        Iterate to the node at index and return that node's data."""

    def push(self, data, index):  # ... (код метода)
        """If index is 0,
        call push_front on data.
        Otherwise, if index is equal to the length,
        call push_back on data.
        Otherwise,
        create new node on the heap using data,
        iterate to the node in front of the index,
        // i.e., the node at index - 1
        set the new node's "next" to the loop node's "next",
        set the loop node's "next" to the new node,
        increment the length."""

    def pop(self, index):  # ... (код метода)
        """If index is 0,
        call pop_front and return the result.
        Otherwise, if index is equal to the length MINUS ONE,
        call pop_back and return the result.
        Otherwise,
        iterate to the node in front of the index,
        store the loop node's "next" node in a new variable as the node to be removed,
        set the loop node's "next" to the "next" of the node to be removed,
        store the data of the node to be removed in a new variable,
        delete the node to be removed, decrement the length, and return the data."""

    def print_list(self):  # ... (код метода)
        """Just printing the list."""

    def clear(self):  # ... (код метода)
        """Create a variable to store the pointer to the node that will be removed.
        While head is not null,
        set the pointer to be removed to head,
        set head to its "next" pointer,
        delete the old head using the pointer to the node to be removed.
        Set the length to zero."""

    def remove_unique_elements(self):  # ... (код метода)
        """Написать функцию, которая удаляет из списка элементы, входящие в него только один раз."""

    def even_and_odd(self):  # ... (код метода)
        """Написать функцию, которая по списку L строит два новых списка: L1 – из четных и L2 – из нечетных элементов списка L."""


def menu():  # ... (код метода)
    """Реализация диалогового окна, для ввода команд пользователем."""

    linked_list = LinkedList()


while 1 > 0:
    menu()
    task = input("Enter your wish (0-11): ")  # ... (код цикла)    
```

**Выводы по лабораторной работе:**
Лабораторная работа позволила успешно реализовать односвязный список на Python и провести тестирование основных
операций. Работа выполнена в соответствии с поставленной задачей.

**Ответы на контрольные вопросы:**

1. **Что такое динамическая структура данных?**
   Динамическая структура данных - это структура данных, которая может изменять размер или форму во время выполнения
   программы.

2. **Что такое список?**
   Список - это динамическая структура данных, представляющая собой упорядоченную коллекцию элементов.

3. **Какие виды списков существуют?**
   Существуют различные виды списков, такие как односвязные списки, двусвязные списки, кольцевые списки и другие.

4. **Какие основные операции выполняются над списком?**
   Основные операции над списком включают добавление элемента в конец (push_back), удаление элемента с конца (pop_back),
   вставку элемента по индексу (push) и другие.

5. **Особенности выполнения операций вставки первого и не первого элемента.**
   Вставка первого элемента (push_front) требует изменения указателя на начало списка. Вставка не первого элемента
   включает перемещение указателей так, чтобы новый элемент указывал на следующий, а предыдущий указывал на новый
   элемент.

6. **Особенности выполнения операций удаления первого и не первого элемента.**
   Удаление первого элемента (pop_front) включает изменение указателя на начало списка. Удаление не первого элемента
   требует изменения указателей так, чтобы предыдущий элемент указывал на следующий после удаляемого элемента.