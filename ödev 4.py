def f(x):
    return(x**2-9)
def bisection(a,b):
    if f(a)*f(b)>0 :
        print("kök yok")
    else :
        c = (a+b)/2
        if f(c)==0:
            return(c)
        if f(a)*f(c)<0:
            b=c
        else:
            a=c
        return(c)

print(bisection(-1,20))

