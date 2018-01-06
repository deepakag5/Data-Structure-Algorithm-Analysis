
# coding: utf-8

# In[1]:


class Stack:
    
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        self.items.pop()
        
    def peek(self):
        return self.items[len(self.items)-1]
        
    def size(self):
        return len(self.items)


# In[2]:


s = Stack()


# In[10]:


print (s.isEmpty())


# In[5]:


s.push(1)


# In[8]:


s.peek()


# In[7]:


s.push(2)


# In[9]:


s.size()

