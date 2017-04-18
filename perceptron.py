#! /usr/bin/python

if __name__ == "__main__":
    dimensionality = int(input())
    training_size = int(input())
    test_size = int(input())
    
    training_set = []
    test_set = []

    
    for i in range(0, training_size):
        line = raw_input()
        line = line.replace('\n', '')
        line = line.replace('\r', '')
        
        training_set.append(line.split(','))
        training_set[i] = map(lambda x: float(x), training_set[i])
    
    
    for i in range(0, test_size):
        line = raw_input()
        line = line.replace('\n', '')
        line = line.replace('\r', '')
        
        test_set.append(line.split(','))
        test_set[i] = map(lambda x: float(x), test_set[i])