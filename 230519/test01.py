import sys
sys.stdin = open('input.txt', 'r')

for i in range(5):
    print(input())

print('Hello Woldo!')

# myList = [1, 2, 3, 4, 5]
myDict = {'a': 1, 'b': 2, 'c': 3}

print(myDict.items())

for key, value in myDict.items():
    print(key, value)

def myFunc():
    print('Hello World!')

class MyClass:
    def __init__(self):
        self.a = 1
        self.b = 2

    def myFunc(self):
        print('Hello World!')

print(MyClass().a)