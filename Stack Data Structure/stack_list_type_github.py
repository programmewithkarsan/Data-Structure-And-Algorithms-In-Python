# simple usage of list as a stack 

#Create a stack via list
test_stack = []

# Insert items to stack/list
test_stack.append(10)
test_stack.append(7)
test_stack.append(13)
test_stack.append(16)

print(test_stack)

#Peek item of stack
print("Peek of stack",test_stack[-1]) 

#Pop off an item. pop() method not only remove top item but also return the value
last_pop_off = test_stack.pop()

print("Last pop off",last_pop_off)
print("Peek of stack", test_stack[-1])

# clear() method remove all item
test_stack.clear()
print(test_stack)
