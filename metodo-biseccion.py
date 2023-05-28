from math import sin, exp

def f1(x):
    return sin(x) - exp(-x)
  
def biseccion(f, a, b, e, n):
  e_abs = abs(b-a)
  i = 1
  while i <= n and e_abs > e:
    mi = (a + b)/2
    if f(mi)==0:
      return mi
    if f(a)*f(mi)<0:
      b = mi
      mi_t = a
    else:
      a = mi
      mi_t = b
    e_abs = abs((mi_t-mi)/mi_t)
    if e_abs < e:
      return mi
    i += 1
  return None

m = biseccion(f1, 0, 1, 2*10**-2, 7)

print (m) 

