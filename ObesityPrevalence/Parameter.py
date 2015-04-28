from random import *


compute_step=100000


# probability p of being born in obesogenic enviroment between 0.5 and  1
p=uniform(0.5,1)
# birth rate between 0 and 0.05
mu=uniform(0,0.05)
# social influence by overweight and obeses between 0 and 0.5
k_1=uniform(0,0.5)
k_2=uniform(0,0.5)
alpha=uniform(0,0.5)
a=uniform(0,0.5)
a_1=uniform(0,0.5)
a_2=uniform(0,0.5)
beta_2=uniform(0,0.5)
beta_3=uniform(0,0.5)
# rate of weight loss to each class: extremely obese to obese, obese to overweight, overweight to normal weight
rho_1=uniform(0,0.5)
# rate of weight regainers transitioning from normal weight to overweight
rhoR=uniform(0,0.5)
# death rate of obese and extremely obese population
D_0=uniform(0,0.5)
# the death rate D of susceptible, overweight and recovered
# populations is lower than the death rate D0 for obese
# and extremely obese populations
D=uniform(0,D_0)

S=[]
E=[]
I_1=[]
I_2=[]
I_3=[]
R=[]

def intial():
    S.append(0.5)
    E.append(0.3)
    I_1.append(0.2)
    I_2.append(0.2)
    I_3.append(0.5)
    R.append(0.6)


