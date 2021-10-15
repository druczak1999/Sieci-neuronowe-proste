from random import uniform
import numpy as np
from GenerateEntries import GenerateEntries
from sklearn.model_selection import train_test_split

class Adaline:

    def LMS(self, prog, value, mi, wh):
        g = GenerateEntries()
        X, d = g.generate_variables_set_with_bias_bi(value)
        X_train, X_test, d_train, d_test = train_test_split(X, d, test_size=0.2, random_state=123)
        epochs_tab=[]
        for _ in range(10):
            weights = []
            for _ in range(len(d_train)):
                weights.append([uniform(-1 * wh,wh),uniform(-1 * wh,wh), uniform(-1 * wh,wh)])

            mean_square_error = 100
            epochs = 0 
            while mean_square_error>= prog:
                diffs=[]
                for k in range(len(d_train)):
                    diff = self.count_error(X_train[k],d_train[k],weights[k])
                    diffs.append(diff**2)
                    weights[k] = self.update_weights(X_train[k],weights[k],diff, mi)
                   
                mean_square_error = sum(diffs)/len(diffs)
                epochs+=1
            epochs_tab.append(epochs)
        
            for k in range(len(d_test)):
                z = self.count_error(X_test[k], d_test[k],weights[k])
                y_predicted = self.predicted_output_bi(z, prog) 
                print("Y: "+str(y_predicted)+", d: "+ str(d_test[k]))
        print(sum(epochs_tab)/len(epochs_tab))

    def count_error(self, X, d, w):
        z = 0
        for i in range(len(X)):
            z+=X[i]*w[i]
        return d - z

    def update_weights(self, X, w, diff, mi):
        for i in range(len(w)):
            w[i] = w[i] + (diff * X[i] * mi)
        return w

    def predicted_output_bi(self, z, prog):
        return np.where(z > prog, 1, -1)
        
