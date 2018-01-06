{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def BinaryTree(r):\n",
    "    return [r,[],[]]\n",
    "\n",
    "def insertLeft(root,newBranch):\n",
    "    t = root.pop(1)\n",
    "    if len(t)>1 :\n",
    "        root.insert(1,[newBranch,t,[]])\n",
    "    else:\n",
    "        root.insert(1,[newBranch, [], []])\n",
    "    return root\n",
    "\n",
    "def insertRight(root,newBranch):\n",
    "    t = root.pop(2)\n",
    "    if len(t)>1:\n",
    "        root.insert(2,[newBranch,[],t,])\n",
    "    else:\n",
    "        root.insert(2,[newBranch,[],[]])\n",
    "    return root\n",
    "\n",
    "def getRootVal(root):\n",
    "    return root[0]\n",
    "\n",
    "def setRootVal(root, newVal):\n",
    "    root[0] = newVal\n",
    "    \n",
    "def getLeftChild(root):\n",
    "    return root[1]\n",
    "\n",
    "def getRightChild(root):\n",
    "    return root[2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
