import numpy as np

def np_square(x: np.array): 
    return np.square(x)

def np_sqrt(x: float):
    return np.sqrt(x)

def add(x: np.array):
    return np.sum(x)

if __name__=="__main__":
    
    a = float(input("input a value: "))
    b = float(input("input b value: "))
    
    arr = np.array([a, b])
    sq = np_square(arr)
    sum_result = add(sq)
    result = np_sqrt(sum_result)
    print("result: ", result)
    
    