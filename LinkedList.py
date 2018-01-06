
# coding: utf-8

# ### Singly Linked List

# In[11]:


class Node(object):
    
    def __init__(self, value):
        self.value = value
        self.nextnode = None


# In[12]:


a = Node(1)
b = Node(2)
c = Node(3)


# In[13]:


a.nextnode = b
b.nextnode = c


# In[14]:


a.value


# In[15]:


a.nextnode.value


# ### Doubly Linked List

# In[16]:


class DoublyLinkedList(object):
    
    def __init__(self,value):
        self.value = value
        self.prevnode = None
        self.nextnode = None


# In[17]:


a = DoublyLinkedList(1)
b = DoublyLinkedList(2)
c = DoublyLinkedList(3)


# In[18]:


b.prevnode = a
a.nextnode = b


# In[19]:


c.prevnode = b
b.nextnode = c


# In[26]:


a.nextnode.value


# In[23]:


b.prevnode.value


# In[25]:


b.nextnode.value

