class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self.size = 0
        self.top = None

    def is_empty(self):
        if self.top == None:
            return True
        else:
            return False

    def push_front(self, data):
        item = Node(data)
        if self.is_empty():
            self.top = item
        else:
            item.next = self.top
            self.top = item
        self.size += 1

    def pop_front(self):
        if self.is_empty():
            return "Error"
        else:
            item = self.top
            self.top = item.next
            self.size -= 1
            return item.data

    def get_top(self):
        if self.is_empty():
            return "Error"
        else:
            return self.top.data

    def clear(self):
        temp = self.top
        while temp is not None:
            temp.data = None
            temp = temp.next
        self.size = 0
        self.top = None

    # additions
    def remove(self, length):
        length = int(length)
        if length < 0 or length - 1 > self.size - 1:
            return "Error"
        elif self.is_empty():
            return "empty"
        else:
            for i in range(0, length):
                temp = self.pop_front()

    def print_stack(stack):
        if stack.is_empty():
            print("Stack is empty")
        else:
            temp = stack.top
            print("Stack size = " + str(stack.size))
            print("Top is = " + str(temp.data))
            print("Stack:")
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print()

    # Вызов этой функции в вашей функции main():
    # print_stack(stack1)


def is_balanced(expression):
    stack = Stack()
    opening_brackets = "([{"
    closing_brackets = ")]}"
    bracket_pairs = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in opening_brackets:
            stack.push_front(char)
        elif char in closing_brackets:
            if stack.is_empty() or stack.get_top() != bracket_pairs[char]:
                return False  # Несоответствие скобок
            stack.pop_front()

    return stack.is_empty()


def evaluate_postfix(expression):
    stack = Stack()
    operators = "+-*/"

    for char in expression:
        if char.isdigit():
            stack.push_front(int(char))
        elif char in operators:
            if stack.size < 2:
                return "Ошибка: недостаточно операндов"
            operand2 = stack.pop_front()
            operand1 = stack.pop_front()
            if char == '+':
                result = operand1 + operand2
            elif char == '-':
                result = operand1 - operand2
            elif char == '*':
                result = operand1 * operand2
            elif char == '/':
                if operand2 == 0:
                    return "Ошибка: деление на ноль"
                result = operand1 / operand2
            stack.push_front(result)
c
    if stack.size == 1:
        return stack.get_top()
    else:
        return "Ошибка: неверное выражение"


def main():
    stack1 = Stack()
    while True:
        print("\nStack Operations:")
        print("1. Push data onto the stack")
        print("2. Pop data from the stack")
        print("3. Get the top of the stack")
        print("4. Check if the stack is empty")
        print("5. Clear the stack")
        print("6. Check for balanced brackets")
        print("7. Evaluate postfix expression")
        print("8. Print")
        print("10. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = input("Enter data to push onto the stack: ")
            stack1.push_front(data)
        elif choice == 2:
            popped_data = stack1.pop_front()
            if popped_data == "Error":
                print("Error: Stack is empty")
            else:
                print("Popped data:", popped_data)
        elif choice == 3:
            top_data = stack1.get_top()
            if top_data == "Error":
                print("Error: Stack is empty")
            else:
                print("Top of the stack:", top_data)
        elif choice == 4:
            if stack1.is_empty():
                print("Stack is empty")
            else:
                print("Stack is not empty")
        elif choice == 5:
            stack1.clear()
            print("Stack cleared")
        elif choice == 6:
            expression = input("Enter the expression to check for balanced brackets: ")
            if is_balanced(expression):
                print("Brackets are balanced")
            else:
                print("Brackets are not balanced")
        elif choice == 7:
            postfix_expression = input("Enter a postfix expression: ")
            result = evaluate_postfix(postfix_expression)
            if isinstance(result, int):
                print("Result:", result)
            else:
                print(result)
        elif choice == 8:
            stack1.print_stack()
        elif choice == 10:
            print("Exiting the program")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
