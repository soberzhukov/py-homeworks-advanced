class Stack:
    def __init__(self):
        self.elements = list()

    def change_type_to_list(self):
        if type(self.elements) is not list:
            self.elements = list(self.elements)

    def isEmpty(self):
        self.change_type_to_list()
        return any(self.elements)

    def push(self, element):
        if not self.isEmpty():
            return 'Пусто'
        self.change_type_to_list()
        self.elements.append(element)

    def pop(self):
        if not self.isEmpty():
            return 'Пусто'
        self.change_type_to_list()
        last_element = self.elements[-1]
        del(self.elements[-1])
        return last_element

    def peek(self):
        if not self.isEmpty():
            return 'Пусто'
        self.change_type_to_list()
        return self.elements[-1]

    def size(self):
        self.change_type_to_list()
        return len(self.elements)

    def balanced(self):
        self.change_type_to_list()
        if self.size() % 2 != 0:
            return "Несбалансированно"
        inversion_dict = {
            '(': ')',
            '[': ']',
            '{': '}',
        }
        counter_dict = {
            ')': 0,
            ']': 0,
            '}': 0,
        }
        while True:
            if not self.isEmpty():
                for i in counter_dict.values():
                    if i:
                        return "Несбалансированно"
                    else:
                        return "Сбалансированно"

            if self.peek() in inversion_dict:
                last_el = self.pop()
                counter_dict[inversion_dict[last_el]] -= 1

                if counter_dict[inversion_dict[last_el]] < 0:
                    return "Несбалансированно"

            else:
                counter_dict[self.pop()] += 1


test_stack = Stack()
test_stack.elements = '(((([}{]))))'
print(test_stack.balanced())
