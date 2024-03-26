class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

def is_palindrome(s):
    wordChecker = Stack()
    for character in s:
        wordChecker.push(character)
    reverseString = ""
    while not wordChecker.isEmpty():
        reverseString += wordChecker.pop()
    return s == reverseString

if __name__ == '__main__':
    print(is_palindrome("hello"))
    print(is_palindrome("madam"))
