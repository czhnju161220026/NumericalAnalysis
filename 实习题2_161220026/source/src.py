import matplotlib.pyplot as plt
import numpy as np
import cmath
import getdata

global func_out
global dev_out

func_out = open('function.txt', 'w+')
dev_out=open('deviation.txt','w+')

def judge(vertix,vertixs):
    Threhold = 22*22
    length = cmath.inf
    for i in vertixs:
        if abs(i[0]-vertix[0])<100 and abs(i[1]-vertix[1])<100:
            temp = abs(i[0]-vertix[0])**2+abs(i[1]-vertix[1])**2
            if temp < length and temp !=0:
                length=temp
    if length < Threhold and -600 < vertix[0] < 500  :
        return 1
    else:
        return 0


def function(function, area):
    if len(function)==3:
        func_out.write('y='+str(function[0])+'x^2 + ('+str(function[1])+'x) + ('+str(function[2])+')\n')
        func_out.write(str(area[0])+'<= x <= '+str(area[1])+'\n')
    else:
        func_out.write('y=' + str(function[0]) + 'x + (' + str(function[1]) + ')\n')
        func_out.write(str(area[0]) + '<= x <= ' + str(area[1]) + '\n')


def deviation(a,x,y):
    dev=0
    if len(a)==3:
        for i in range(0,len(x)):
            dev+=(a[0]*x[i]**2+a[1]*x[i]+a[2]-y[i])**2
        dev_out.write(str(dev**0.5)+'\n')
    else:
        for i in range(0,len(x)):
            dev+=(a[0]*x[i]+a[1]-y[i])**2
        dev_out.write(str(dev**0.5)+'\n')

vertixs = getdata.get_vertixs()
x = []
y = []
errornode_x = []
errornode_y = []
for vertix in vertixs:
    if judge(vertix, vertixs) == 1:
        x.append(vertix[0])
        y.append(vertix[1])
    else:
        errornode_x.append(vertix[0])
        errornode_y.append(vertix[1])
plt.xlabel(r'$ x$')
plt.ylabel(r'$ y$')

# draw normal node and error node
plt.scatter(x, y, s=12, color='c',label=r'$Normal$',alpha=0.6)
plt.scatter(errornode_x, errornode_y, s=12, color='r',label=r'$Abnormal$', marker='x')

# fit area 1
temp_x = []
temp_y = []
edge = - cmath.inf
for i in range(0,len(x)):
    if edge < y[i] < -500 and x[i] > -200:
        edge = y[i]
for i in range(0,len(x)):
    if y[i] <= edge and x[i] < 60:
        temp_x.append(x[i])
        temp_y.append(y[i])
res = np.polyfit(temp_x, temp_y, 2)
f1_x = np.linspace(-465, 75, 10000)
f1_y = [res[0]*i**2+res[1]*i+res[2] for i in f1_x]
#plt.scatter(temp_x,temp_y,color='c',marker='o')
plt.plot(f1_x, f1_y, color='b', label=r'$Path$',linestyle='-')
function(res,[-465,75])
deviation(res,temp_x,temp_y)

# fit area 2
temp_x = []
temp_y = []
for i in range(0, len(x)):
    if 70< x[i]< 160 and y[i]<-400:
        temp_x.append(x[i])
        temp_y.append(y[i])
res = np.polyfit(temp_x, temp_y, 2)
f1_x = np.linspace(75, 160, 10000)
f1_y = [res[0]*i**2+res[1]*i+res[2] for i in f1_x]
#plt.scatter(temp_x,temp_y,color='r',marker='o')
plt.plot(f1_x, f1_y, color='b', linestyle='-')
function(res, [75,160])
deviation(res,temp_x,temp_y)

# fit area 3
temp_x = []
temp_y = []
for i in range(0, len(x)):
    if 160< x[i]< 600 and y[i]<-550:
        temp_x.append(x[i])
        temp_y.append(y[i])
res = np.polyfit(temp_x, temp_y, 2)
f1_x = np.linspace(160, 500, 10000)
f1_y = [res[0]*i**2+res[1]*i+res[2] for i in f1_x]
#plt.scatter(temp_x,temp_y,color='g',marker='o')
plt.plot(f1_x, f1_y, color='b', linestyle='-')
function(res, [160,500])
deviation(res,temp_x,temp_y)

# fit area 4
temp_x = []
temp_y = []
for i in range(0, len(x)):
    if 300< x[i]< 600 and -550 < y[i] < -500:
        temp_x.append(x[i])
        temp_y.append(y[i])
res = np.polyfit(temp_x, temp_y, 1)
f1_x = np.linspace(370, 500, 10000)
f1_y = [res[0]*i+res[1] for i in f1_x]
#plt.scatter(temp_x,temp_y,color='b',marker='o')
plt.plot(f1_x, f1_y, color='b', linestyle='-')
function(res, [370,500])
deviation(res,temp_x,temp_y)

# fit area 5
temp_x = []
temp_y = []
for i in range(0, len(x)):
    if 390< x[i]< 415 and -500 < y[i] < -200:
        temp_x.append(x[i])
        temp_y.append(y[i])
res = np.polyfit(temp_x, temp_y, 1)
f1_x = np.linspace(375, 417, 10000)
f1_y = [res[0]*i+res[1] for i in f1_x]
#plt.scatter(temp_x,temp_y,color='y',marker='o')
plt.plot(f1_x, f1_y, color='b', linestyle='-')
function(res, [375,417])
deviation(res,temp_x,temp_y)

# fit area 6
temp_x = []
temp_y = []
for i in range(0, len(x)):
    if 300< x[i]< 420 and y[i]>-180:
        temp_x.append(x[i])
        temp_y.append(y[i])
res = np.polyfit(temp_x, temp_y, 2)
f1_x = np.linspace(300, 420, 10000)
f1_y = [res[0]*i**2+res[1]*i+res[2] for i in f1_x]
#plt.scatter(temp_x,temp_y,color='k',marker='o')
plt.plot(f1_x, f1_y, color='b', linestyle='-')
function(res, [300, 420])
deviation(res,temp_x,temp_y)

# fit area 7:
temp_x = []
temp_y = []
for i in range(0, len(x)):
    if -600< x[i]< 300 and y[i]>-210:
        temp_x.append(x[i])
        temp_y.append(y[i])
res = np.polyfit(temp_x, temp_y, 1)
f1_x = np.linspace(-480, 300, 10000)
f1_y = [res[0]*i+res[1] for i in f1_x]
#plt.scatter(temp_x,temp_y,color='m',marker='o')
plt.plot(f1_x, f1_y, color='b', linestyle='-')
function(res, [-480, 300])
deviation(res,temp_x,temp_y)

# fit area 8:
temp_x = []
temp_y = []
for i in range(0, len(x)):
    if -530< x[i]< -400 and -400<y[i]<-100:
        temp_x.append(x[i])
        temp_y.append(y[i])
res = np.polyfit(temp_x, temp_y, 1)
f1_x = np.linspace(-480, -380, 10000)
f1_y = [res[0]*i+res[1] for i in f1_x]
#plt.scatter(temp_x,temp_y,color='r',marker='o')
plt.plot(f1_x, f1_y, color='b', linestyle='-')
function(res, [-480, -380])
deviation(res,temp_x,temp_y)

# fit area 9:
temp_x = []
temp_y = []
for i in range(0, len(x)):
    if -530< x[i]< -380 and -600<y[i]<-300:
        temp_x.append(x[i])
        temp_y.append(y[i])
res = np.polyfit(temp_x, temp_y, 1)
f1_x = np.linspace(-465, -385, 10000)
f1_y = [res[0]*i+res[1] for i in f1_x]
#plt.scatter(temp_x,temp_y,color='g',marker='o')
plt.plot(f1_x, f1_y, color='b', linestyle='-')
function(res, [-465,-385])
deviation(res,temp_x,temp_y)

plt.legend(loc='upper right')
plt.savefig("path.png",format='png')
plt.show()
func_out.close()
dev_out.close()
