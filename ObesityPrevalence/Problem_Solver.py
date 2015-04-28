from Parameter import *

def dynamicModel(year_Predict,compute_step,p,mu,k_1,k_2,alpha,a,a_1,a_2,beta_2,beta_3,rho_1,rhoR,D_0,D,S,E,I_1,I_2,I_3,R):
    
    stepInterval=year_Predict/float(compute_step)
       
    for i in range (0,compute_step):
        N=S+E+I_1+I_2+I_3+R
        
        S=S+ stepInterval*((1-p)*mu*N - D*S - (k_1*I_1*S/N) - (k_2*I_2*S/N) -alpha*S)
        
        E=E + stepInterval*(p*mu*N - D*E - a*E + (k_1*I_1*S/N) + (k_2*I_2*S/N) + rhoR*R + alpha*S)
       
        I_1=I_1 + stepInterval*(-D*I_1 + a*E - a_1*I_1 - rho_1*I_1 + beta_2*I_2)
        
        I_2= I_2 + stepInterval*(-D_0*I_2 + a_1*I_1 - a_2*I_2 - beta_2*I_2 + beta_3*I_3)
       
        I_3=I_3 + stepInterval*(-D_0*I_3 + a_2*I_2 - beta_3*I_3)
        
        R=R + stepInterval*(-D*R + rho_1*I_1 - rhoR*R)
    return S,E,I_1,I_2,I_3,R
    
    
    
##if __name__ == '__main__':
##    dynamicModel(10, 100000,0.1, 0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2)
    
   
   

