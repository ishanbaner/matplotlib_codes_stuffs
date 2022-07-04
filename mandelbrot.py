# importing the required module
import sys
import matplotlib.pyplot as plt
#sys.setrecursionlimit(10**7)

def Mandel(cn,c):
    global st
    if c==complex(0,0):
        return(complex(0,0))
    return(cn*cn+c)
def check(c):
    nc=c
    for i in range(10**3):
        nc=Mandel(nc,c)
        if abs(nc)>10**100:
            return(False)
    return(True)
# x axis values
y=[]
r=[]
p=-2
q=-2
# corresponding y axis values
while p <=1:
    while q<=1:
        if check(complex(p,q)):
            r.append(p)
            y.append(q)
        q+=0.05
    q=-2
    p+=0.05
# plotting the points
plt.plot(r, y,"ro")

# naming the x axis
plt.xlabel('Re')
# naming the y axis
plt.ylabel('Im')

# giving a title to my graph
plt.title('Mandelbrot')

# function to show the plot
plt.show()
