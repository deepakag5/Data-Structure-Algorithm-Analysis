
# coding: utf-8

# In[5]:


class Queue2Stacks(object):
    
    def __init__(self):
        
        self.inStack = []
        self.outStack = []
        
    def enqueue(self,item):
        self.inStack.append(item)
    
    def dequeue(self):
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
                
        return self.outStack.pop()


# In[6]:


q = Queue2Stacks()

for i in range(5):
    q.enqueue(i)
    
for i in range(5):
    print (q.dequeue())

