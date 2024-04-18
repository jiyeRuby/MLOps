
def square(x: float, n: float = 2.) -> float: 
    return x**n

def add(x: float, y:float) -> float:
    return x +y

# def square_root(x: float) -> float:
#     return x**0.5

if __name__=="__main__":
    
    a = float(input("input a value: "))
    b = float(input("input b value: "))
    
    # a^2 + b^2 = c^2
    # print(c)
    a_sq = square(a)
    b_sq = square(b)
    sum_result = add(a_sq, b_sq)
    result = square(sum_result, n=.5)
    print("result: ", result)
    
    