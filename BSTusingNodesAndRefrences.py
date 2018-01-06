
# coding: utf-8

# In[2]:


class BinaryTree(object):
    
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftchild = None
        self.rightchild = None
    
    def insertLeft(self,newNode):
        if self.leftchild == None:
            self.leftchild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftchild = self.leftchild
            self.leftchild = t
    
    def insertRight(newNode):
        if self.rightchild == None:
            self.rightchild = BinaryTree(newNode)
            
        else:
            t = BinaryTree(newNode)
            t.rightchild = self.rightchild
            self.rightchild = t
    
    def getLeftchild(self):
        return self.leftchild
    
    def getRightchild(self):
        return self.rightchild
    
    def setRootVal(self,obj):
        self.key = obj
    
    def getRootVal(self):
        return self.key

