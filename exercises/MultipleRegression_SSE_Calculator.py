X = [[50,10],[100,5],[75,12],[200,2],[125,14]]

Y = [500,1200,800,2000,1400]

def calc_Y_hat(X1,X2):
    Y_hat = (10 * X1) + (2 * X2) + 50
    return Y_hat

Y_hats = []

for i in range(len(X)):
    Y_hats.append(calc_Y_hat(X[i][0],X[i][1]))

def SumOfSquaredErrors(Y,Y_hats,dimensions):
    SSE = 0
    for i in range(len(Y)):
        SSE += (Y[i] - Y_hats[i])**2
    return SSE/dimensions

print(SumOfSquaredErrors(Y,Y_hats))