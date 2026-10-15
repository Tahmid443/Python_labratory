# Delegating to sub-generator
def gen1():
    yield 1
    yield 2

def gen2():
    yield 3
    yield 4

def combined():
    yield from gen1()
    yield from gen2()

print(list(combined()))

# Recursive
def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

print(list(flatten([1, [2, 3, [4, 5]], 6])))

# Chaining
def chain(*iterables):
    for it in iterables:
        yield from it

print(list(chain([1, 2], "ab", (True, False))))

# yield from returns sub-generator value
def sub():
    yield 1
    yield 2
    return "sub done"

def main():
    result = yield from sub()
    print(f"Sub returned: {result}")
    yield 3

print(list(main()))

# Tree traversal
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left, self.right = left, right

def inorder(node):
    if node:
        yield from inorder(node.left)
        yield node.val
        yield from inorder(node.right)

root = Node(2, Node(1), Node(3))
print(list(inorder(root)))