from random import randint, uniform

class GenerateEntries:

    def generate_variables_set_uni(self, value):
        X = []
        d = []
        X.append([0, 0])
        X.append([0, 1])
        X.append([1, 0])
        X.append([1, 1])
        d.append(0)
        d.append(0)
        d.append(0)
        d.append(1)
        for _ in range(value):
            ran = randint(1,4)
            if ran == 1:
                X.append([uniform(-0.1,0.1),uniform(-0.1,0.1)])
                d.append(0)
            if ran==2:
                X.append([uniform(0.9,1.1),uniform(0.9,1.1)])
                d.append(1)
            if ran==3:
                X.append([uniform(-0.1,0.1),uniform(0.9,1.1)])
                d.append(0)
            if ran==4:
                X.append([uniform(0.9,1.1),uniform(-0.1,0.1)])
                d.append(0)
        return X, d

    def generate_variables_set_bi(self, value):
        X = []
        d = []
        X.append([-1, -1])
        X.append([-1, 1])
        X.append([1, -1])
        X.append([1, 1])
        d.append(-1)
        d.append(-1)
        d.append(-1)
        d.append(1)
        for _ in range(value):
            ran = randint(1,4)
            if ran == 1:
                X.append([uniform(-1.1,-0.9),uniform(0.9,1.1)])
                d.append(-1)
            if ran==2:
                X.append([uniform(0.9,1.1),uniform(0.9,1.1)])
                d.append(1)
            if ran==3:
                X.append([uniform(-1.1,-0.9),uniform(0.9,1.1)])
                d.append(-1)
            if ran==4:
                X.append([uniform(0.9,1.1),uniform(-1.1,-0.9)])
                d.append(-1)
        return X, d

    def generate_variables_set_with_bias_uni(self, value):
        X = []
        d = []
        X.append([0, 0, 1])
        X.append([0, 1, 1])
        X.append([1, 0, 1])
        X.append([1, 1, 1])
        d.append(0)
        d.append(0)
        d.append(0)
        d.append(1)
        for _ in range(value):
            ran = randint(1,4)
            if ran == 1:
                X.append([uniform(-0.1,0.1),uniform(-0.1,0.1),1])
                d.append(0)
            if ran==2:
                X.append([uniform(0.9,1.1),uniform(0.9,1.1),1])
                d.append(1)
            if ran==3:
                X.append([uniform(-0.1,0.1),uniform(0.9,1.1),1])
                d.append(0)
            if ran==4:
                X.append([uniform(0.9,1.1),uniform(-0.1,0.1),1])
                d.append(0)
        return X, d

    def generate_variables_set_with_bias_bi(self, value):
        X = []
        d = []
        X.append([-1, -1, 1])
        X.append([-1, 1, 1])
        X.append([1, -1, 1])
        X.append([1, 1, 1])
        d.append(-1)
        d.append(-1)
        d.append(-1)
        d.append(1)
        for _ in range(value):
            ran = randint(1,4)
            if ran == 1:
                X.append([uniform(-1.1,-0.9),uniform(0.9,1.1),1])
                d.append(-1)
            if ran==2:
                X.append([uniform(0.9,1.1),uniform(0.9,1.1),1])
                d.append(1)
            if ran==3:
                X.append([uniform(-1.1,-0.9),uniform(0.9,1.1),1])
                d.append(-1)
            if ran==4:
                X.append([uniform(0.9,1.1),uniform(-1.1,-0.9),1])
                d.append(-1)
        return X, d

    def generate_entries(self,bias, unipolar, value, prog):
        if bias == False and unipolar == True:
            X, d = self.generate_variables_set_uni(value)
        elif bias == False and unipolar == False:
            X, d = self.generate_variables_set_bi(value)
        elif bias == True and unipolar == True:
            X, d  = self.generate_variables_set_with_bias_uni(value)
            prog = 0
        else:
            X, d  = self.generate_variables_set_with_bias_bi(value)
            prog = 0
        return X,d, prog
