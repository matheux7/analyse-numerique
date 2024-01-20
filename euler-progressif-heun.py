import  math 
import sys 
import matplotlib.pyplot as plt
def euler_progressif(f,tt,y0,N):
    
    yy = [yo]
    
    for i in range(N): 
        yy.append(yy[i]+h*f(tt[i],yy[i])) 
    return yy 
def euler_modifie(f,tt,N): 
    yy = [yo] 
    for i in range(N): 
        yy.append(yy[i]+h*f(tt[i]+h*0.5,yy[i]+h*0.5*f(tt[i],yy[i]))) 
    return yy  
def heun(f,tt,N): 
    yy = [yo] 
    for i in range(N): 
        yy.append(yy[i]+h*(f(tt[i],yy[i])+f(tt[i+1],yy[i]+h*f(tt[i],yy[i])))) 
    return yy 
# INITIALISATION foireux qdf
N =3  
t0 = 0.31 
y0 = 1.32 
tfinal = 3.33 
def f(t,y): 
    return y 
def sol_exacte(t): 
        return math.exp(t)  
t0 = 0.39 
y0 = 1.40 
tfinal = 3. 
def f(t,y): 
    return t 
def sol_exacte(t): 
        return 1.+0.5*t**2  
t0 = 0. 
y0 = 0. 
tfinal = 1. 
def f(t,y): 
    return math.cos(2*y) 
def sol_exacte(t): 
        return 0.5*math.asin((math.exp(4.*t)-1.)/(math.exp(4.*t)+1.)) 

N = 5
yo = 3
t0 = 0.5
tfinal = 3
def f(t,y):
    return -7*y
def sol_exacte(t):
        return 3*math.exp(-7*t)
# CALCUL
h = (tfinal-t0)/N 
tt = [ t0+i*h for i in range(N+1) ] 
yy_exacte = [sol_exacte(t) for t in tt] 
yy_euler_progressif = euler_progressif(f,tt,y0,N)
print(yy_euler_progressif)# permet d'afficher la liste  solutions de l'equadif
yy_euler_modifie = euler_modifie(f,tt,N)  
yy_heun = euler_modifie(f,tt,N)
# AFFICHAGE 
plt.axis([t0, tfinal, min(yy_euler_progressif), max(yy_euler_progressif)]) 
plt.plot(tt,yy_exacte,'m',tt,yy_euler_progressif,'g-',tt,yy_euler_modifie,'c--',tt,yy_heun,'r-')
plt.plot(tt,yy_exacte,'m',tt,yy_euler_progressif,'g-') 
plt.show()





