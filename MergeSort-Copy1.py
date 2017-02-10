
# coding: utf-8

# In[1]:

import math
import numpy as np
import pylab as pl
get_ipython().magic('matplotlib inline')


# In[2]:

def mergesort( Mylist):

    if len(Mylist) < 2:
        return Mylist

    fin = len(Mylist)/2

    left = mergesort(lista[:int(fin)])
    reft = mergesort(lista[int(fin):])

    return mergeSort(izquierda, derecha)

def mergeSort(left, right):
    i = 0
    j = 0

    lista = []

    while (i < len(left) and j < len(right)):
        if(left[i] < right[j]):
            Mylist.append(left[i])
            i += 1
        if(left[i] > right[j]):
            lista.append(derecha[j])
            j += 1
            
    Mylist += left[i:]
    Mylist += right[j:]

    return Mylist


# In[3]:

ordenar = [10,5,4,6,22,8,98,1]
ordenar = mergesort(ordenar)
print ordenar


# In[4]:

Numero de operaciones


# In[5]:

class Counter:
    '''
    Class Counter
    Implements a step counter, which is used to compute the number of basic operations performed in
    a particular call to a function.
    '''
    def __init__(self):
        self.steps = 0

    def reset(self):
        self.steps = 0

    def count(self):
        self.steps += 1

    def print_steps(self):
        print "Number of steps =", self.steps
        
def acct_mergesort(Mylist, acct):

    if len(Mylist) < 2: 
        acct.count()
        return Mylist;

    fin = len(Mylist)/2; acct.count()

    left = acct_mergesort(Mylist[:int(fin)], acct);
    right = acct_mergesort(Mylist[int(fin):], acct);

    return acct_merge(left, right, acct)

def acct_merge(left, right, acct):
    i = 0; acct.count()
    j = 0; acct.count()

    Mylist = []; 
    acct.count()
    while (i < len(left) and j < len(right)):
        if(left[i] < right[j]):
            Mylist.append(left[i])
            i += 1
            acct.count()
        if(left[i]>right[j]):
            lista.append(derecha[j])
            j += 1
            acct.count()
    Mylist += right[j:]; acct.count()        
    Mylist += left[i:]; acct.count()
    return Mylist


# In[6]:

ordenar = [46,23,11,98,35,87,35,19]
acct = Counter()
ordenar = acct_mergesort(ordenar, acct)
print ordenar
acct.print_steps();


# In[7]:

Tiempo de ejecucion


# In[8]:

import time

def time_analysis(n):
    resultados = []
    acct = Counter()
    for i in range(n):
        l = range(i)
        rnd.shuffle(l)
        tic = time.clock()#get start time
        mergesort(l)
        toc = time.clock()#get final time
        resultados.append((toc-tic)*1000000)
    return resultados


# In[9]:

print time_analysis(10)


# In[10]:

Analisis experimental


# In[11]:

import random as rnd

def exper_analysis(n):
    resultados = []
    acct = Counter()
    for i in range(n):
        l = range(i)
        rnd.shuffle(l)
        acct.reset()
        acct_mergesort(l, acct)
        resultados.append(acct.steps)
    return resultados


# In[12]:

print exper_analysis(10)


# Analisis Teorico

# In[14]:

import random as rnd
import math

def teoric_analysis(n):
    resultados = []
    for i in range(n):
        if(i == 0):
            l = 0
        else:
            l = i*np.log2(i)
        resultados.append(l)
    return resultados


# In[15]:

print teoric_analysis(10)


# In[ ]:




# In[ ]:




# In[ ]:



