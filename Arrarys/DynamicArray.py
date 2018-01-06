
# coding: utf-8

# In[26]:


import ctypes

class DynamicArray(object):
    
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)
    
    def __len__(self):
        return self.n
    
    def __getitem__(self,k):
        
        if not 0 <= k < self.n:
            raise IndexError('k out of bounds!')
        
        return self.A[k]
    
    def append(self,newele):
        
        if self.n == self.capacity:
            self._resize(2*self.capacity)
        
        self.A[self.n] = newele
        self.n += 1
        
    
    def _resize(self,new_cap):
             
        B = self.make_array(new_cap)
        
        for k in range(self.n):
            B[k] = self.A[k]
        
        self.A = B
        self.capacity = new_cap
        
    
    def make_array(self,new_cap):
        
        return (new_cap * ctypes.py_object)()
    


# In[27]:


arr = DynamicArray()


# In[28]:


arr.append(1)


# In[29]:


len(arr)


# In[30]:


arr.append(2)


# In[31]:


len(arr)


# In[32]:


arr[0]


# In[33]:


arr[2]

