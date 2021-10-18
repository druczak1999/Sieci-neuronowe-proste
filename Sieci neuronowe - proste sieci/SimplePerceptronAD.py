from random import uniform
import numpy as np
from GenerateEntries import GenerateEntries
from sklearn.model_selection import train_test_split

DIFFERENCE = -100

class SimplePerceptron:

    def learning_algorythm(self, alpha, prog, value, bias, unipolar, wh):
        g = GenerateEntries()
        X, d, prog = g.generate_entries(bias,unipolar,value,prog)
        X_train, X_test, d_train, d_test = train_test_split(X, d, test_size=0.2, random_state=123)
        
        epoch_tab=[]
        for _ in range(10):
            weights = self.generate_weights(len(d),bias, wh)
            differences_in_epoch = DIFFERENCE
            epochs = 0
            while differences_in_epoch != 0:
                epochs += 1
                differences_in_epoch = 0
                diffs = []
                for k in range(len(d_train)):
                    z = self.sum_all(X_train[k], weights[k])
                    if unipolar:
                        y_predicted = self.predicted_output_uni(z, prog)
                    else:
                        y_predicted = self.predicted_output_bi(z, prog) 
                    diff = self.count_difference(y_predicted, d_train[k])
                    if diff != 0 : differences_in_epoch += 1
                    diffs.append(diff)
                    weights[k] = self.update_weights(weights[k], X_train[k], diff, alpha)
            epoch_tab.append(epochs)
           
            for k in range(len(d_test)):
                z = self.sum_all(X_test[k], weights[k])
                if unipolar: y_predicted = self.predicted_output_uni(z, prog)
                else: y_predicted = self.predicted_output_bi(z, prog) 
                print("Y: "+str(y_predicted)+", d: "+ str(d_test[k]))
        
        print("Epochs: "+str(sum(epoch_tab)/10))

    def sum_all(self, x, w):
        suma=0
        for i in range(0, len(x)):
            suma = suma + (x[i] * w[i])
        return suma

    def predicted_output_uni(self, z, prog):
        return np.where(z > prog, 1, 0)
    
    def predicted_output_bi(self, z, prog):
        return np.where(z > prog, 1, -1)

    def count_difference(self, y, d):
        return d - y

    def update_weights(self, w, x, diff, alpha):
        for i in range(len(w)):
            w[i]= w[i] + (alpha * diff * x[i])
        return w

    def generate_weights(self,len_of_d, bias, wh):
        weights = []
        for _ in range(len_of_d):
            if bias == False:
                weights.append([uniform(-1*wh,wh),uniform(-1*wh,wh)])
            else:
                weights.append([uniform(-1*wh,wh),uniform(-1*wh,wh), uniform(-1*wh,wh)])
        return weights
    