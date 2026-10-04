class Stack:
    def __init__(self,size):
        self.stack = []
        self.size = size
    #If stack is full
    def isFull(self):
        if len(self.stack) >= self.size:
            print("Stack is full!!!")
    #If stack is empty
    def isEmpty(self):
        if self.stack == []:
            print("Stack is empty!!!")
    #push()
    def push(self,value):
        if self.isFull():
            print("Stack overlfow")
        else:
            self.stack.append(value)
    #pop()
    def pop(self):
        if self.isEmpty():
            print("Stack underflow!!!")
        else:
            self.stack.pop()
    #peek
    def peek(self):
        if self.isEmpty():
            print("Stack is empty!!!")     
        else:
            print(self.stack[-1])        
    #display
    def display(self):
        if self.isEmpty():
            print("Stack is empty!!!")     
        else:
            for x in self.stack:
                print(x, end=" ")
                print('\n')                
    #delete
    def delete(self):
        self.stack.clear()   
        print("Stack deleted successfully!!!")         
        
size = int(input("Enter size of a stack: "))
s = Stack(size)

while True:
    print("======== Stack =======\n")
    print("1.Push")
    print("2.Pop")
    print("3.Peek")
    print("4.Dsiplay")
    print("5.Delete")
    print("6.Exit")
    print("=====================\n")
    
    choice = int(input("Enter yout choice: "))
    if choice == 1:
        value = input("Enter value: ")
        s.push(value)
    elif choice == 2:
        s.pop()
    elif choice == 3:
        s.peek()
    elif choice == 4:
        s.display()
    elif choice == 5:
        s.delete()
    elif choice == 6:
        break
    else:
        print("Invalid input!!!")