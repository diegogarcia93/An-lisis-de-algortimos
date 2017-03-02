TALLER 2 MULTIPLICACIÓN DE MATRICES

import numpy as np
import matplotlib.pyplot as pl
import time
%matplotlib inline

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


1. MULTIPLICACION DE MATRICES EN TIEMPO O(n^3)	

def MatrizMult(A, B, acct):
    col = []
    if len(A) != len(B):
        acct.count()
        return column
    if len(A) == len(B):
        acct.count()
        for i in range(0, len(A)):
            acct.count()
            auxi = []; acct.count()
            for j in range(0, len(A[i])):
                acct.count()
                C = 0; acct.count()
                for k in range(0, len(B)):
                    acct.count()
                    C += A[i][k]*B[k][j]; acct.count()
                auxi.append(C)
            col.append(low)
    return col



acct = Counter()
A = [[67,20,54,31,48],[17,69,23,57,99],[47,83,15,16,87],[31,79,37,28,13]]
B = [[51,35,76,23,76],[43,12,55,32,67],[49,35,32,27,88],[82,10,90,23,66]]

C = matrix_multi(A, B, acct)



2. DIVIDIR Y CONQUISTAR

def nxn(matriz):
    tam = len(matriz)
    A = np.zeros((tam,1))
    B = np.zeros((1, tam+1))
    matriz = np.c_[matriz,A]
    matriz = np.r_[matriz,B]
    return matriz

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


def multiplicar(T1, T2, acct):
    true = True;acct.count()
    tam = len(temp1);acct.count()
    if (len(T1) <= 2):
        acct.count()
        auxi = T1*T2;acct.count()
        return auxi
         
    if(len(T1) > 2): 
        par = tam%2
        if(par != 0 ):
            acct.count()
            true = False
            T1 = nxn(T1)
            T2 = nxn(T2)
            tam = tam + 1
            

        tam = tam/2;acct.count()
        w = T1[:tam,:tam];acct.count();
	x = T1[tam:, :tam];acct.count();
	y = T1[tam:,tam:]; 
	z = T1[:tam,tam:]
        ww = T2[:tam,:tam];acct.count();
	xx = T2[tam:, :tam];acct.count();
	yy = T2[tam:,tam:]; 
	zz = T2[:tam,tam:]
    multW = multiplicar(w,ww,acct);acct.count(); multx = multiplicar(z,xx,acct);acct.count(); multy = multiplicar(w,zz,acct);acct.count(); multz = multiplicar(z,yy,acct);acct.count()
    multiww = multiplicar(x,ww,acct);acct.count(); multixx = multiplicar(y,xx,acct);acct.count(); multyy = multiplicar(x,zz,acct);acct.count();  multzz = multiplicar(y,yy,acct);acct.count()
    
    p1 = multww + multxx
    acct.count()
    p2 = multw + multx
    acct.count()
    p3 = multyy + multzz
    acct.count()
    p4 = multy + multz
    acct.count()
    
    p2 = np.c_[s2,s4];acct.count(); p1 = np.c_[s1,s3];acct.count();  p2 = np.r_[s2,s1];acct.count()
    
    if true != true:
        tam = len(p2)
        acct.count()
        p2 = p2[:tam-1,:tam-1]
        acct.count()
    return p2


3.STRASEN

