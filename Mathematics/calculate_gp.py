import math

def cal_gp(a,b,n):
    NthTerm = a
    for i in range(1,n):
        NthTerm *= n
    return NthTerm

def main():
    a = 2
    r = 3
    N = 5
    print(type(cal_gp(a,r,N)))

if __name__ == "__main__":
    main()

