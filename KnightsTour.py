#!/usr/bin/env python2	
# -*- coding: utf-8 -*-	
"""
Created on Sat Oct 29 18:51:28 2016

@author: adilanees
"""	
	
#Some Knight's Tour problems
#Adil Anees 160000742		
from numpy import *	
import networkx as nx	
import pylab as pyl	
	
#The function MoveTo takes as input the position (i,j) on an nxn chessboard: MoveTo(i,j,n)
# and outputs	
def MoveTo(i,j,n):	
    g=[]	
    if type(i)==int and type(j)==int and type(n)==int:	
        if i<0 or j<0 or n<0 or i>n-1 or j>n-1:	
            #print('Input of Knight position does not exist on this board')
            return []
        elif n<=2:	
            #print('There are no moves for this Knight')	
            return []
        elif i==1 and j==1 and n==3:	
            #print('There are no moves for this Knight')
            return 	[]
        else:	
            for a in [-2,2]:	
                for b in [-1,1]:	
                    if i+a>=0 and j+b>=0 and i+a<=n-1 and j+b<=n-1:	
                         g.append(((i+a),(j+b)))	
                    if i+b>=0 and j+a>=0 and i+b<=n-1 and j+a<=n-1:	
                        g.append(((i+b),(j+a)))	
            return g	
    else:	
        return 'Inputs must be integers'	
	
	
print('The Knight at 0,0 on a 4x4 chess board can move to', MoveTo(0,0,4))	
print('The Knight at 0,3 on a 6x6 chess board can move to', MoveTo(0,3,6))	
print('The Knight at 1,4 on a 5x5 chess board can move to', MoveTo(1,4,5))	

#Define MyBoard 	
def MyBoard(n):	
    Board=nx.Graph()	
    for i in range(0,n):	
        for j in range(0,n):	
            Board.add_node((i,j))	
            L=MoveTo(i,j,n)	
            for x in range(0,len(L)):	
                Board.add_edge((i,j), (L[x]))	
    return Board	
	

#Define B(n) which draws	 the nxn board and shows the number of nodes
def B(n):	
    B=MyBoard(n)	
    nx.draw_circular(MyBoard(n))	
    pyl.show()	
    print('B(',n,') has', B.number_of_nodes(), 'nodes')	
    return B	

#Some graphs
print(B(4))
print(B(6))
print(B(8))
	
#Shows how nany knight moves are possible for each square on a nxn board
def CountMoves(n):	
    c=zeros((n,n))	
    for i in range(0,n):	
        for j in range(0,n):	
            c[i,j]=len(MoveTo(i,j,n))	
    return c	

#Some boards with number of possible moves
print(CountMoves(4))	
print(CountMoves(6))
print(CountMoves(8))
	

#for n>=6	
#Function will list squares that have moves to exactly 3 other squares on a nxn board
#Squares which can move to exactly 3 other squares are located horizontally and vertically adjacent to the corner squares'	
def Moves3(n):	
    g=[]	
    g.extend(((1,0),(0,1),(n-2,0),(0,n-2),(n-1,1),(1,n-1),(n-1,n-2),(n-2,n-1)))	
    return g	

#Function will list squares that have moves to the fewest no. of squares	 for a nxn board
#Squares with the fewest number of moves are the corner squares
def FewestMoves(n):	
    g=[]	
    g.extend(((0,0),(0,n-1),(n-1,0),(n-1,n-1)))	
    return g	
	
	
#Function adds all entries in the CountMoves(n) array	
	
def TotalMoves(n):	
    C=CountMoves(n)	
    a=0	
    i=0	
    j=0	
    while j<n:	
        if i<n:	
            a=a+C[i,j]	
            i=i+1	
        else:	
            i=0	
            j=j+1	
    return a	

#Totalmoves2 as function of n is (gives same answer as TotalMoves(n):)	
def TotalMoves2(n):	
    a=8*(n-1)*(n-2)	
    return a	
	
def KnightsTour(i,j,n):    	
    g=[(i,j)]	
    h=[]	
    B=MyBoard(n)	
    K=list(B.neighbors((i,j)))	
    while len(list(K))>0:       	
        for x in range(0,len(K)):            	
            h.append(B.degree(K[x]))                             	
        g.append(K[h.index(min(h))])	
        B.remove_node((i,j))	
        i=g[len(g)-1][0]	
        j=g[len(g)-1][1]  	
        K=list(B.neighbors((i,j))) 	
        h=[]	
    return g	
	
print(KnightsTour(0,0,8)	)
K=KnightsTour(0,0,8)	
c=zeros((8,8))	
for x in range (0,64):	
    c[K[x]]=x	
print(c) 	
	

#This tests to see whether the tour is complete	
	
for i in range(0,8):	
    for j in range(0,8):	
        K=KnightsTour(i,j,8)	
        if len(K)<64:	
            print('The tour from',(i,j),'failed'	)
print('All other tours were complete')	

	
#It failed for starting positions (2,5) and (4,5)	
print('Due to the symmetry of the board, a rotation of 180 degrees shows that if a tour is possible from (1,6), it must be possible from (6,1)')	
print('This means we can use the symmetric moves of the KnightsTour function')