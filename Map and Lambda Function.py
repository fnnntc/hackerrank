cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    x=[0,1]
    for i in range(n-2):
        val = sum(x[-2:])
        x.append(val)
    return(x)
    # return a list of fibonacci numbers

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
