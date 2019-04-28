
# 第一问：输入n个分样本各自的均值和标准差（mu1,mu2…）和（sigma1,sigma2…），计算这些样本所组成的合样本的均值和标准差(mu,sigma)

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

# 第二问：输入一组样本数据，绘制这个数据均值的抽样分布直方图

def sampling_dist(mean,std,n):
    
    xbar = []

    for i in range(100):
    
        data = np.random.normal(mean,std,n) 
        xbar = np.append(xbar,data.mean())
        
    mu = xbar.mean()
    sigma = xbar.std()

    return plt.hist(xbar,bins=20,color="k",
                    alpha=0.5,rwidth=0.9,range=(50,54)),plt.title("n={0},
                    mu={1:.2f},sigma={2:.2f}".format(n,mu,sigma))

sampling_dist()



