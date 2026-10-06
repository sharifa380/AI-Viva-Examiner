stack=[]
def push():
    if len(stack)>num:
        print("stack overflow")
    else:
        element=int(input("enter a the element:"))
        stack.append(element)
        print("element pushed successfully...!")
def pop():
    pop_element.pop()
    print("the popped element:",pop_element)
def peek():
    print("top most elements:",stack[-1])
def empty():
    if len(stack)==0:
        print("stack is empty...!")
    else:
        print("stack is:",stack)
num=int(input("enter the size of stack:"))
while True:
    print("1.push")
    print("2.pop")
    print("3.peek")
    print("4.empty")
    print("5.exit")
    option=int(input("choose number from the above:"))
    if option==1:
        push()
    elif option==2:
        pop()
    elif option==3:
        peek()
    elif option==4:
        empty()
    elif option==5:
        break
    else:
        print("invalid")
        
