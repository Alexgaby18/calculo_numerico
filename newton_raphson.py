
def newton_raphson(func, x0, error, max_iter): 
    h = 0.00001 
    
    xn = x0
    
    for n in range(max_iter):
        derivada = (func(xn + h) - func(xn)) / h
        
        h = func(xn) / derivada  
        
        xn = xn - h   
 
        if abs(h) < error:
            return xn
        
    return None

