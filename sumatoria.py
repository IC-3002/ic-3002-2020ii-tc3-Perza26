def sumatoria_cubica(n):
    r=0
    for i in range(n+1):
        for j in range(i+1):
            for k in range(j,i+j+1):
                r+=1
    return r

def sumatoria_constante(n):
    return(n*(n+1)*(n+2))/3

