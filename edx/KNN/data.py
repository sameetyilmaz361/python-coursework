import numpy as np
import random
import scipy.stats as ss
import matplotlib.pyplot as plt

def generate_synth_data(n=50):

    points = np.concatenate((ss.norm(0,1).rvs((n,2)), ss.norm(1,1).rvs((n,2))), axis=0)
    outcomes = np.concatenate((np.repeat(0,n), np.repeat(1,n)))
    return(points , outcomes)

points , outcomes = generate_synth_data(n=20)


n = 20
plt.figure()
plt.plot(points[:n,0] , points[:n,1] , "ro")
plt.plot(points[n:,0] , points[n:,1] , "bo ")
plt.show()




def make_prediction_grid(predictors,outcomes,limits, h ,k):
    (x_min , x_max , y_min , y_max) = limits
    xs=np.arange(x_min , x_max , h)
    ys=np.arange(y_min , y_max , h)
    xx, yy = np.meshgrid(xs,ys)

    prediction_grid = np.zeros(xx.shape, dtype=int)
    for i,x in enumerate(xs):
        for j,y in enumerate(ys):
            p=np.array([x,y])
            prediction_grid[j,i] = knn_predict(p , predictors , outcomes , k)

    return(xx , yy , prediction_grid)


(predictors , outcomes) = generate_synth_data()

k = 5
filename = "knn_synth_5.png"
limits = (-3,4,-3,4)
h = 0.1

(xx , yy , prediction_grid) = make_prediction_grid(predictors , outcomes , limits , h , k)
plt_prediction_grid(xx , yy , prediction_grid , filename)