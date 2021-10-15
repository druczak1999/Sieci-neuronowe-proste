from SimplePerceptronAD import SimplePerceptron

if __name__ == "__main__":
    sp = SimplePerceptron()
    
    print("without bias, unipolar")
    #alpha, threshold, number of values, with bias, unipolar?, weight
    sp.learning_algorythm(0.1, 0, 100, False, True,0.2)

    print("with bias, unipolar")
    sp.learning_algorythm(0.1, 0, 100, True, True,0.2)

    print("without bias, bipolar")
    sp.learning_algorythm(0.1, 0, 100, False, False,0.2)

    print("with bias, bipolar")
    sp.learning_algorythm(0.1, 0, 100, True, False,0.2)
