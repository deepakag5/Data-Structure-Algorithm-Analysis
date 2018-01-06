
# coding: utf-8

# In[1]:


class Node(object):
    
    def __init__(self,value):
        self.value = value
        self.nextnode = None


# In[2]:


def reverse(head):
    
    current = head
    previous = None
    nextnode = None
    
    while current:
        
        nextnode = current.nextnode
        
        current.nextnode = previous
        
        previous = current
        current = nextnode
        
    return previous


# In[3]:


# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.nextnode = b
b.nextnode = c
c.nextnode = d


# In[5]:


print (a.nextnode.value)
print (b.nextnode.value)
print (c.nextnode.value)


# In[6]:


d.nextnode.value


# In[7]:


reverse(a)


# In[9]:


print (a.nextnode.value)


# In[10]:


print (b.nextnode.value)
print (c.nextnode.value)
print (d.nextnode.value)

