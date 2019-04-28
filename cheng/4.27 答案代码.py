def sample_stats():
    
    import numpy as np
    
    n_k = np.array(eval(input("input n_k")))
    bar_k = np.array(eval(input("input bar_k")))
    sigma_k = np.array(eval(input("input sigma_k")))
    
    if len(n_k) != len(bar_k) != len(sigma_k):
        
        raise ValueError("incomplete input!")
    
    else:
        
        n = n_k.sum()
        
    xvar_k = np.power(sigma_k,2)
    
    xbar = 1/n*np.dot(n_k,bar_k)
    
    xsigma = np.sqrt(1/(n-1)*(np.dot(n_k-1,xvar_k)+n_k.dot(np.power(bar_k-xbar,2))))
    
    return n_k,bar_k,sigma_k,n,xbar,xsigma

sample_stats()

