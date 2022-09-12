#simple stack wrapper class

class Stack():
    
    def _init_(self): # no return type
    
        self.stack = list()
    
    def push(self,value): # no return type
    
        self.stack.append(value)
    
    def pop(self):
        
        if(len(self.stack) > 0):
            return self.stack.pop()
        else:
            return None
    
    def peek(self):
        
        if(len(self.stack) >0):
            return self.stack[-1]
        else:
            return None
    
    def clear(self):
        
        self.stack.clear()
    
    def _str_(self):
        
        return str(self.stack) # you have to type cast otherwise _str_ method does not work
        # _str_ MUST RETURN string type value
        
        
if _name_ == '_main_':
    
    test_stack = Stack()
    test_stack.push(5)
    test_stack.push(8)
    test_stack.push(3)
    test_stack.push(12)
    print(test_stack.peek())
    print(test_stack.pop())
    print(test_stack.peek())
    test_stack.clear()
    print(test_stack)