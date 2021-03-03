import sympy

def newtonRaphson(f, t, x0, maxIter=100, minTol=1e-6, printResults=False): #f is the function defined with sympy simbolic expressions, t is the independent variable of f, maxIter is the maximum number of iterations the user allows, minTol is the minimum tolerance the user wants for the result and printResults that if True, the number of iterations and final error will be printed at the end of the iterations.
    fp = f.diff(t); #Derivate f(x) for later use during the iterations.
    xi = x0 #The first guess will be the starting point stated by the user.
    xi1 = 0.0 #The next guess is defined and equaled to 0 (it will be overwritten later during the first loop iteration).
    error = 9223372036854775800 #Max int size in python so that the while loop won't stop before beginning.
    n = 0 #The counter for the iteration.
    while n < maxIter and error > minTol:
        xi1 = xi - f.evalf(subs={t:xi})/fp.evalf(subs={t:xi}) #The next guess is calculated.
        error = abs((xi1-xi)/xi1) #The absolute error is calculated.
        xi = xi1 #The previous guess becomes the current guess (it will be the previous for the next iteration).
        n += 1 #Add one to the iteration counter.
    if(error <= minTol): #Check if the loop ended because the minimum tolerance was reached.
        print("Toleráncia mínima alcanzada")
    else: #If the minimum tolerance wasn't met but the number of iterations reached its maximum.
        print("Número máximo de iteraciones alcanzado")
    if(printResults):
        print("Iteraciones: {} - Tolerancia Final: {:.5f}".format(n,error))
    return xi1

#Test
if(__name__ == "__main__"):
    
    #Problem parameters
    a = 0.01
    v0 = 0
    di = -5
    df = 0
    
    
    #Newton-Raphson method parameters
    x0 = 1
    maxIter = 50
    minTol = 0.1

    #Problem equation and definition
    t = sympy.symbols('t')
    f = (a/2)*t**2+v0*t+di-df

    #Calculations and results
    estimatedValue = newtonRaphson(f,t,x0,maxIter,minTol,True)
    print("Resultado estimado: {:.5f}".format(estimatedValue))
    realValue = (-v0 + (v0**2-2*a*(di-df))**0.5)/a
    print("Resultado real: {:.5f}".format(realValue))
    print("Error porcentual final: {:.5f}%".format(abs(100*(realValue-estimatedValue)/realValue)))