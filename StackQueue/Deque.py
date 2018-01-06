
# coding: utf-8

# In[1]:


class Deque:
    
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def addFront(self,item):
        self.items.append(item)
        
    def addRear(self,item):
        self.items.insert(0,item)
        
    def removeFront(self):
        self.items.pop()
        
    def removeRear(self):
        self.items.pop(0)
        
    def size(self):
        return len(self.items)


# In[12]:


d = Deque()


# In[13]:


d.addFront('hello')
d.addRear('world')


# In[16]:


d.size()


# In[15]:


d.removeFront()
d.removeRear()

