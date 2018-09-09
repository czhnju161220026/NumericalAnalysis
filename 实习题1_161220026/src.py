# -*- coding:utf-8 -*-
import numpy as np


def answer1():
    fout1 = open('answer.txt', 'a')
    A1cond2=[]
    A2cond2=[]
    for n in range(2,9):
        A1=np.zeros(shape=(n+1,n+1),dtype=np.float64)
        A2=np.zeros(shape=(n+1,n+1),dtype=np.float64)
        # Set A1
        for k in range(n+1):
            x=np.float64(1)+np.float64(0.2*k)
            for i in range(n+1):
                A1[k][i]=np.float64(x**i)

        #Set A2
        for i in range(n+1):
            for j in range(n+1):
                A2[i][j]=np.float64(1/(i+j+1))

        nA1=np.linalg.inv(A1)
        nA2=np.linalg.inv(A2)
        A1cond2.append(np.float64(np.linalg.norm(nA1,ord=2)*np.linalg.norm(A1,ord=2)))
        A2cond2.append(np.float64(np.linalg.norm(nA2,ord=2)*np.linalg.norm(A2,ord=2)))


    fout1.write("\t\t\tA1\t\tA2\n")
    for i in range(len(A1cond2)):
        fout1.write("n=%d\t\t%f\t\t%f\n"%(i+2,A1cond2[i],A2cond2[i]))
    fout1.close()


def answer2():
    fout2=open("answer.txt",'a')

    n=5
    A1 = np.zeros(shape=(n+1, n+1))
    A2 = np.zeros(shape=(n+1, n+1))
    # Set A1
    for k in range(n+1):
        x = np.float64(1) + np.float64(0.2 * k)
        for i in range(n+1):
            A1[k][i] = np.float64(x ** i)

    # Set A2
    for i in range(n+1):
        for j in range(n+1):
            A2[i][j] = np.float64(1 / (i + j + 1))

    # Set b1,b2
    b1 = []
    b2 = []
    for i in range(n+1):
        a1 = 0
        a2 = 0
        for j in range(n+1):
            a1 += A1[i][j]
            a2 += A2[i][j]
        b1.append(a1)
        b2.append(a2)

    fout2.write('X1=')
    fout2.write(str(np.dot(np.linalg.inv(A1), b1)))
    fout2.write('\nX2=')
    fout2.write(str(np.dot(np.linalg.inv(A2), b2)))
    fout2.write('\n')
    fout2.close()


def answer3():
    fout3 = open("answer.txt", 'a')
    n = 5
    A1 = np.zeros(shape=(n + 1, n + 1),dtype=np.float64)
    # Set A1
    for k in range(n + 1):
        x = np.float64(1) + np.float64(0.2 * k)
        for i in range(n + 1):
            A1[k][i] = np.float64(x ** i)
    # Set b1
    b1 = []
    for i in range(n + 1):
        a1 = 0
        a2 = 0
        for j in range(n + 1):
            a1 += A1[i][j]
        b1.append(a1)
    # add interupt

    A1[1][1]=np.float64(A1[1][1]+1e-12)
    A1[5][5]=np.float64(A1[5][5]+1e-12)

    fout3.write('X1\'=')
    fout3.write(str(np.dot(np.linalg.inv(A1), b1)))
    fout3.write('\n')
    fout3.close()


def answer4():
    fout4=open("answer.txt",'a')

    n = 5
    A2 = np.zeros(shape=(n + 1, n + 1),dtype=np.float64)
    # Set A2
    for i in range(n + 1):
        for j in range(n + 1):
            A2[i][j] = np.float64(1 / (i + j + 1))
    # Set b2
    b2 = []
    for i in range(n + 1):

        a2 = 0
        for j in range(n + 1):
            a2 += A2[i][j]
        b2.append(a2)
    # add interupt
    preA22 = A2[1][1]
    preA66 = A2[5][5]
    A2[1][1] = np.float64(A2[1][1] + 1e-7)
    A2[5][5] = np.float64(A2[5][5] + 1e-7)
    fout4.write('X2\'=')
    fout4.write(str(np.dot(np.linalg.inv(A2), b2)))
    fout4.write('\n')
    A2[1][1] = preA22
    A2[5][5] = preA66
    b2[5] = np.float64(b2[5] + 1e-4)
    fout4.write('X2\'\'=')
    fout4.write(str(np.dot(np.linalg.inv(A2), b2)))
    fout4.write('\n')
    fout4.close()

def answer6():
    fout6 = open("answer.txt", 'a')
    n = 5
    A1 = np.zeros(shape=(n + 1, n + 1))
    A2 = np.zeros(shape=(n + 1, n + 1))
    # Set A1
    for k in range(n + 1):
        x = np.float64(1) + np.float64(0.2 * k)
        for i in range(n + 1):
            A1[k][i] = np.float64(x ** i)

    # Set A2
    for i in range(n + 1):
        for j in range(n + 1):
            A2[i][j] = np.float64(1 / (i + j + 1))

    # Set b1,b2
    b1 = []
    b2 = []
    for i in range(n + 1):
        a1 = 0
        a2 = 0
        for j in range(n + 1):
            a1 += A1[i][j]
            a2 += A2[i][j]
        b1.append(a1)
        b2.append(a2)
    # calculate X1,X2,X1',X2',X2''
    X1 = np.dot(np.linalg.inv(A1), b1)
    X2 = np.dot(np.linalg.inv(A2), b2)

    A1[1][1] = np.float64(A1[1][1] + 1e-12)
    A1[5][5] = np.float64(A1[5][5] + 1e-12)
    X1_ = np.dot(np.linalg.inv(A1), b1)

    preA22 = A2[1][1]
    preA66 = A2[5][5]
    A2[1][1] = np.float64(A2[1][1] + 1e-7)
    A2[5][5] = np.float64(A2[5][5] + 1e-7)
    X2_ = np.dot(np.linalg.inv(A2), b2)

    A2[1][1] = preA22
    A2[5][5] = preA66
    b2[5] = np.float64(b2[5] + 1e-4)
    X2__ = np.dot(np.linalg.inv(A2), b2)

    fout6.write("||X1-X1\'||/||X1||=")
    fout6.write(str(np.linalg.norm(X1 - X1_, ord=np.inf) / np.linalg.norm(X1, ord=np.inf)))
    fout6.write('\n')

    fout6.write("||X2-X2\'||/||X2||=")
    fout6.write(str(np.linalg.norm(X2 - X2_, ord=np.inf) / np.linalg.norm(X2, ord=np.inf)))
    fout6.write('\n')

    fout6.write("||X2-X2\'\'||/||X1||=")
    fout6.write(str(np.linalg.norm(X2 - X2__, ord=np.inf) / np.linalg.norm(X2, ord=np.inf)))
    fout6.write('\n')
    fout6.close()


# handle the questions

fout=open("answer.txt",'a')
fout.write("-----------------------------question 1----------------------------\n")
fout.close()
answer1()
fout=open("answer.txt",'a')
fout.write("\n-----------------------------question 2----------------------------\n")
fout.close()
answer2()
fout=open("answer.txt",'a')
fout.write("\n-----------------------------question 3----------------------------\n")
fout.close()
answer3()
fout=open("answer.txt",'a')
fout.write("\n-----------------------------question 4----------------------------\n")
fout.close()
answer4()
fout=open("answer.txt",'a')
fout.write("\n-----------------------------question 6----------------------------\n")
fout.close()
answer6()